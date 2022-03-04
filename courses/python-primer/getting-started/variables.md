---
title: Variables
include_in_preview: false
---

It is very easy to use variables in Python.

```
x = 10
y = 20
z = x + y
print(z)
```

In the above example `x`, `y` and `z` are variables.

Unlike other static typed languages like C or Java, variables in Python don't have any type associated with them.

```
x = 10
print(x)

x = "hello"
print(x)
```

As you can see, the value of x was intially an integer and then x was reassigned to a string value. This is prefectly valid in Python.

Often, beginner programmers get confused about strings and variables. Strings are the text values that we enclose in quotes and variables are names that refer to some values.

The following program is supposed to print `Python`, but it is printing text "name". Can you identify what is the mistake in this program?

```
name = "Python"
print("name")
```

