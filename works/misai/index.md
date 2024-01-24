---
name: misai
desc: template engine
---

_misai_ is a simple template engine for the Python programming language.
It's loosely inspired by [Jinja] and [mustache]. Sample code is shown below:

```
{{ #if logged_in }}
    {{ #for user : users }}
        {{ "Hello: " | concat: user.name }}
    {{ #end }}
{{ #end }}
```

_misai_ features:

* loops: `{{ #for i : items }}{{i}}{{ #end }}`
* conditionals: `{{ #if a }} a {{# elif b }} b {{ #else }} c {{ #end }}`
* variable assignment: `{{ #set i = 123 }}`
* filters: `{{ title | capitalize }}`
* comparison operators (==, !=, <=, >=, <, >): `{{ a > b }}`
* logical operators (and, or): `{{ red or (green and solid) }}`
* variables: `{{ foo }} {{ foo.bar }} {{ foo["bar"] }}`
* literals (floats, integers, strings): `{{ "str" }} {{ 42 }} {{ 3.14 }}`

The project is under 500 LOC, and comes with no external dependencies.
It implements a context sensitive lexer and a one-pass compiler
that transforms template to Python bytecode internally.

_misai_ is currently used to render a [web version][zen101] of [101 Zen Stories][zen101wiki],
a collection of stories compiled by Nyogen Senzaku in the early 20th century.

Source code: https://github.com/nkanaev/misai

[mustache]: https://en.wikipedia.org/wiki/Mustache_(template_system)
[Jinja]: https://en.wikipedia.org/wiki/Jinja_(template_engine)
[zen101]: https://nkanaev.github.io/zen101/en/
[zen101wiki]: https://en.wikipedia.org/wiki/101_Zen_Stories
