---
name: Writing a polyglot script
date: 2020-01-08
tags: code, python
---

So here's the thing - I'm relatively good at Python. I somewhat know Ruby.
Not good enough to write something complex, but enough to understand
that it's "a bit" different from Python. Yet both of the languages
have similar syntaxes, which made me think whether I could come up with a script
that's valid in both languages.

The shortest valid script could be:

```
print("hello world")
```

I thought that was too easy, so I set a goal to write a script that would
print the exact language used. After a bit of tinkering, I came up with this:

```
print(["ruby", "python"][(0 or 1)])
```

I've remembered that one of the main surprises the developers who switched
from one language to another encountered was the fact that `0` is *falsey* in Python,
whereas in Ruby it is *truthy*. So the expression `0 or 1` evaluates to 0 and 1
in Ruby and Python, accordingly. And if we use just that to get the value at
the corresponding index of the specially crafted list, we can achieve the given task.
As a side note, we would need to enclose the boolean expression in parentheses,
because otherwise it'll throw a syntax error in Ruby.

I could have settled here, but I decided to raise the bar higher. What if I try to come up 
with a script that could do more sophisticated things
than just printing some values?
Now that's where things get more complicated,
since you can't just do anything in one languages
that would be also correct in another. But I've finally managed to come up with
a somewhat decent solution with a few neat tricks:

```
(0 and eval("""
3.times {
  puts 'ruby code goes here'
}
true
""")) or eval(compile("""
for i in range(3):
    print('python code goes here')
""", "", "exec"))
```

So what's happening in here:

1. The code above is a single statement of the form `(0 and <expr1>) or <expr2>`.
   Both Python and Ruby support short-circuiting for boolean expressions,
   therefore `expr1` evaluates in Ruby and `expr2` in Python only.
2. It heavily relies on metaprogramming, by evaluating only a single function
   that could contain more complex code inside a string.
   Ruby's `eval` needs to have a *truthy* value as the last statement,
   which is returned as the function's value. If we fail to do so,
   Ruby will try to execute `expr2`. For Python we could have used `expr`, but
   I realised that it's not available in Python 2 (which had not reached the EOL at
   the time when I was experimenting, so as a well-mannered Pythonista
   I had to support it as well).
3. Using triple-quote strings is a nice addition to write more readable code
   without providing escape sequences for newlines where necessary.
   In Python it's the only way to create multiline strings.
   Ruby, on the other hand, supports multiline strings by default
   with single and double quoted strings, and treats `"""foo"""`
   as three separate strings `"" "foo" ""` which then get concatenated to one.
   This, however, makes using double (or single) quote characters
   tricky in the code placeholders.

