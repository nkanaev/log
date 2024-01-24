---
name: yarr
desc: web feed aggregator
type: work
---

_yarr_ (yet another rss reader) is a web-based feed aggregator.
It can be used both as a desktop application and a personal self-hosted server.

![Screenshot of Yarr's GUI](promo.png)

This is my personal feed reader that I use regularly that became popular with others as well.
It's written with simplicity in mind, both internally and from UI/UX perspective.
It's main features:

* Cross-platform: Windows, MacOS and Linux (GUI mode) + any OS/arch Go supports
* Responsive design suitable for desktop, tablet and mobile
* Support for all feed formats: Atom, RSS, RDF and JSON
* _Readability_ for clutter-free reading experience
* Intuitive interface with minimal settings
* Themes (White/Beige/Dark)
* OPML import/export
* Keyboard shortcuts
* Full-text search

The project is written in Go, and the frontend is powered by Vue.js and Bootstrap.
It's very light on dependencies,
with `golang.org/x/net`, `golang.org/x/sys` and mattn's `go-sqlite3` being
the only external (vendored) dependencies. The rest (apart from Go's builtin packages)
is implemented from scratch. These include:

* RSS/Atom/JSON feed parsers
* subset of CSS selector
* Web router and middlewares
* HTML sanitizer and readability library (borrowed and modified from [miniflux])

Source code: https://github.com/nkanaev/yarr

[miniflux]: https://github.com/miniflux/v2
