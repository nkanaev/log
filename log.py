#!/usr/bin/env python3
import argparse
import collections
import commonmark
import datetime
import functools
import glob
import http.server
import misai
import os
import re
import shlex
import shutil
import subprocess
import textwrap
import threading
import time
import webbrowser
import yaml


BASEDIR = os.path.dirname(os.path.abspath(__file__))


def path(*parts):
    return os.path.join(BASEDIR, *parts)


def command_newpost(args):
    date = datetime.date.today()
    fullname = path('posts/{date}-{name}.md'.format(
        date=date.strftime('%Y%m%d'), name=args.filename))
    with open(fullname, 'w') as f:
        f.write(textwrap.dedent('''
            ---
            name: Post Title
            slug: {name}
            tags: []
            ---

            Post content
        '''.format(name=args.filename)).strip())
    print('done')


def command_compile(args):
    Post = collections.namedtuple(
        'Post',
        'name slug date date_pretty date_rfc822 guid tags body link'.split())

    def read_post(filepath):
        with open(filepath) as f:
            _, meta, body = re.split('(^-{3,}.+?)^-{3,}', f.read(), flags=re.M | re.S)

        meta = yaml.safe_load(meta)
        body = commonmark.commonmark(body.lstrip())

        basename, _ = os.path.splitext(os.path.basename(filepath))
        date, slug = basename.split('-', 1)
        date = datetime.datetime.strptime(date, '%Y%m%d')
        link = '/posts/' + slug + '/'

        return Post(
            name=meta['name'], tags=meta['tags'], slug=slug,
            date=date,
            date_pretty=date.strftime('%B %d, %Y'),
            date_rfc822=date.strftime('%a, %d %b %Y %H:%M:%S UT'),
            guid=os.path.basename(filepath),
            body=body, link=link)

    posts = [read_post(filepath) for filepath in glob.glob(path('posts/*.md'))]
    posts.sort(key=lambda p: p.date, reverse=True)

    sitemeta = {
        'host': 'https://nkanaev.github.io',
        'root': '',
        'posts': posts,
        'title': None,
        'sitetitle': 'nkanaev',
    }

    templateloader = misai.Loader(path('theme'), locals=sitemeta)
    template = templateloader.get('main.html')
    feed = templateloader.get('feed.xml')

    def copy(src, dst):
        print(' *', os.path.relpath(src, BASEDIR))
        shutil.copy(src, os.path.join(BASEDIR, dst))

    def save(filename, content):
        print(' *', filename)
        file_path = path('_out', filename)
        os.makedirs(os.path.dirname(file_path), exist_ok=1)
        with open(file_path, 'w') as f:
            f.write(content)

    save('index.html', template.render(page='index', posts=posts[:10]))
    save('feed.xml', feed.render(posts=posts[:10]))
    save('posts/index.html', template.render(title='Archive', page='archive'))
    for post in posts:
        content = template.render(title=post.name, page='post', post=post)
        save('posts/{}/index.html'.format(post.slug), content)

    for pagepath in glob.glob(path('pages', '*')):
        slug, _ = os.path.splitext(os.path.basename(pagepath))
        with open(pagepath) as f:
            body = commonmark.commonmark(f.read())
        content = template.render(page='page', body=body)
        save('{}/index.html'.format(slug), content)

    # copy assets
    print('copying assets:')

    copy('theme/main.css', path('_out'))
    copy('theme/favicon.ico', path('_out'))
    copy('theme/avatar.jpg', path('_out'))
    copy('theme/CNAME', path('_out'))

    print('copying files:')

    os.makedirs(path('_out', 'files'), exist_ok=True)
    for dirpath, dirnames, filenames in os.walk(path('files')):
        for dirname in dirnames:
            reldirpath = os.path.relpath(os.path.join(dirpath, dirname), path('files'))
            os.makedirs(path('_out', 'files', reldirpath), exist_ok=True)
        for filename in filenames:
            if filename.startswith('.'):
                continue
            # /full/path/to/files/foo/bar.txt
            filepath = os.path.join(dirpath, filename)
            # files/foo/bar.txt
            relpath = os.path.relpath(filepath, BASEDIR)
            # files/foo
            dirname = os.path.dirname(relpath)
            copy(relpath, path('_out', dirname))


def command_preview(args):
    def watchfiles():
        lasttime = 0
        while True:
            for dirname in ['files', 'pages', 'posts', 'theme']:
                for filepath in glob.iglob(path(dirname, '*'), recursive=True):
                    if os.stat(filepath).st_mtime > lasttime:
                        command_compile(None)
                        lasttime = time.time()
                        break
            time.sleep(1)

    watchthread = threading.Thread(target=watchfiles, daemon=True)
    watchthread.start()
    address = ('127.0.0.1', 8000)
    handler = functools.partial(
        http.server.SimpleHTTPRequestHandler,
        directory=path('_out'))
    print('** starting server on http://%s:%d' % address)
    webbrowser.open('http://localhost:8000/')
    httpd = http.server.HTTPServer(address, handler)
    httpd.serve_forever()


def command_publish(args):
    command_compile(None)

    os.chdir(path('_out'))

    message = datetime.datetime.now().strftime('%c')
    author = 'Nazar Kanaev <nkanaev@live.com>'
    run = lambda cmd: subprocess.call(shlex.split(cmd))
    run('git init')
    run('git add .')
    run('git commit -m "{}" --author "{}"'.format(message, author))
    run('git remote add origin git@github.com:nkanaev/nkanaev.github.io.git')
    run('git push origin -uf master')


def main():
    parser = argparse.ArgumentParser()

    cmds = parser.add_subparsers()

    cmd_newpost = cmds.add_parser('newpost')
    cmd_newpost.add_argument('filename')
    cmd_newpost.set_defaults(func=command_newpost)

    cmd_compile = cmds.add_parser('compile')
    cmd_compile.set_defaults(func=command_compile)

    cmd_preview = cmds.add_parser('preview')
    cmd_preview.set_defaults(func=command_preview)

    cmd_publish = cmds.add_parser('publish')
    cmd_publish.set_defaults(func=command_publish)

    args = parser.parse_args()
    if not getattr(args, 'func', None):
        parser.print_usage()
        return
    args.func(args)


if __name__ == '__main__':
    main()
