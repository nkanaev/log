---
name: Writing a triple polyglot script
date: 2020-01-28
tags: code, python
---

In the previous post I've described how to write a script
that's both valid Ruby and Python.
Then I came up with the idea of adding Perl on top if it.

So, the basic form of the polyglot code (with slight modifications) is this:

```
(0 and eval("puts 1") or 1) or eval(compile("print(2)", "", "exec"))
```

Now, if I could find a value that sets Perl apart from Ruby & Python
and add it to the expression above, I'd be able to run some code via `eval`.
Luckily, quick google search revealed that `"0"` is *falsey* in Perl.
After a bit of tinkering I've managed to construct something like this:

```
(0 and (eval("puts 1") or 1)) or ("0" and (eval(compile("print(2)", "", "exec")) or 1)) or eval("print 3;")
```

That's quite a lot of brackets to make non-lisper's eyes bleed,
so here's the brief summary of what's going on:

```
(0 and (<ruby_expr> or 1))
  or ("0" and (<python_expr> or 1))
    or <perl_expr>
```

* Ruby treats `0` as *truthy*, runs the first expression and discards the rest.
* Python ignores the first expression (`0` is *falsey*),
  and runs the second expression only (non-empty strings are *truthy*)
* Perl ignores the first and the second expressions (`0` and `"0"` as *falsey*),
  running only the last expression.
* `or 1` is a "safe-guard" to make sure that the short-circuiting
  stops after executing the expression prior to that.
  
## making code "readable"

Again, this is still not enough for me,
since I wanted placeholders that would let me
write more "readable" code inside `eval` calls (read: multiline strings).

And this is where I encountered a small problem.
Python supports multiline strings *only* via triple-quotes.
Perl (unlike Ruby) raises syntax error on that. So I needed some workaround.

The solution was to use `q` "function" in Perl:

```
substr(q("""
<perl_stmts>
"""), 3, -3)
```

Syntax is still valid in 3 languages.
But there's a catch -  `q` function does not exist in Ruby and Python,
but defining it should be easy using the same techniques described earlier:

```
(0 and eval("def q(x) x end", binding)) or ("0" and (eval(compile("def q(x):\n return x", "", "exec")) or 1));
```

Now we can wrap the rest of the strings in `q` identity function, and we're done.

## creating a "practical" application

I didn't spend so much time just for nothing, so here's a working fizzbuzz example:

```
(0 and eval("def q(x) x end", binding)) or ("0" and (eval(compile("def q(x):\n return x", "", "exec")) or 1));

(0 and (eval(q("""
1.upto(100){|i|puts ('fizzbuzz '[n=i**4%-15,n+13] || i.to_s).rstrip}
""")) or 1)) or ("0" and (eval(compile(q("""
for i in range(1,101): print('fizz'*(i%3==0) + 'buzz'*(i%5==0) or i)
"""), "", "exec")) or 1)) or eval(substr(q('''
print "fizz"x!($_ % 3) . "buzz"x!($_ % 5) || $_ , "\n" for 1 .. 100;
'''), 3, -3))
```

Triple-hirable.
