---
name: Treating JSON as Python
date: 2020-12-15
tags: python
---

It just occured to me that JSON (with some exceptions)
can be a subset of Python, and parsed as such without the help of `json` module.

Say, if we have a sample JSON, which includes all of the value types
(object/array/string/numbers/true/false/null):

```
{
  "numbers": [123, 123.456],
  "booleans": [true, false],
  "null": null,
  "string": "string"
}
```

we can parse it using `eval`, by complementing
`null`/`true`/`false` with corresponding variables:

```
# `sample` is a string representation of the above example
eval(sample, {}, {'null': None, 'true': True, 'false': False})
```

which results in a proper Python object:

```
{'booleans': [True, False],
 'null': None,
 'numbers': [123, 123.456],
 'string': 'string'}
```

This, of course, doesn't handle certain cases, like string escape sequences.
And the solution overall isn't safe, and shouldn't be used in a production code.
Nevertheless, I find the trick interesting.
