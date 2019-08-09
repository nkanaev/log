#!/usr/bin/env python3
import argparse
import commonmark
import collections
import datetime
import glob
import misai
import os
import re
import textwrap
import yaml
import shutil
import webbrowser


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
            name: {name}
            tags: []
            ---

            content
        '''.format(name=args.filename)).strip())
    print('done')


def command_compile(args):
    Post = collections.namedtuple('Post', 'name slug date date_pretty tags body link'.split())

    def read_post(filepath):
        with open(filepath) as f:
            _, meta, body = re.split('(^-{3,}.+?)^-{3,}', f.read(), flags=re.M | re.S)

        meta = yaml.safe_load(meta)
        body = commonmark.commonmark(body.lstrip())

        basename, _ = os.path.splitext(os.path.basename(filepath))
        date, slug = basename.split('-', 1)
        date = datetime.datetime.strptime(date, '%Y%m%d')
        link = 'posts/' + slug + '/'

        return Post(
            name=meta['name'], tags=meta['tags'],
            slug=slug, date=date, date_pretty=date.strftime('%B %d, %Y'),
            body=body, link=link)

    posts = [read_post(filepath) for filepath in glob.glob(path('posts/*.md'))]
    posts.sort(key=lambda p: p.date, reverse=True)

    sitemeta = {
        'root': '',
        'posts': posts,
        'title': '256 shades of gray',
    }
    template = misai.Loader(path('theme'), locals=sitemeta).get('main.html')

    def copy(pattern, dst):
        for f in glob.glob(path(pattern)):
            print(' *', os.path.relpath(f, BASEDIR))
            shutil.copy(f, os.path.join(BASEDIR, dst))

    def save(filename, content):
        print(' *', filename)
        file_path = path('_out', filename)
        os.makedirs(os.path.dirname(file_path), exist_ok=1)
        with open(file_path, 'w') as f:
            f.write(content)

    save('index.html', template.render(page='index', posts=posts[:10]))
    save('posts/index.html', template.render(page='archive'))
    for post in posts:
        content = template.render(page='post', post=post)
        save('posts/{}/index.html'.format(post.slug), content)

    # copy assets
    print('copying assets:')

    copy('theme/main.css', path('_out'))
    copy('theme/favicon.ico', path('_out'))
    copy('theme/avatar.jpg', path('_out'))


def command_preview(args):
    webbrowser.open('http://localhost:8000/')


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

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
