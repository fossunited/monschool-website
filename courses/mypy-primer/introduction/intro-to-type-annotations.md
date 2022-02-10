---
title: Introduction to Python's type annotation syntax
include_in_preview: false
---

Here's a Python function:

```{.python .example}
age = 18

def is_adult(age):
    if age >= 18:
        return True

    return False

print(is_adult(25))
```

Compare this code to the same code in the Go programming language:

```{.go .example}
var age int = 18

func is_adult(age int) bool {
  if age >= 18 {
    return true
  }

  return false
}
```

The annotations of `int` and `bool` are what allow Go's compiler to validate the
types. So we need some way to add type annotations to our Python code.

The annotations have to be added in a way that doesn't affect how the Python
code works, but it should still be easy and flexible to add the annotations.

Since they shouldn't affect the actual code, one obvious possibility is to use
comments, maybe something like this?

```{.python .example}
age = 18  # type: int
```

This could technically _work_, but this way of writing types would get cluttered
and hard to read very quickly.

Fortunately for us, Python 3.0 had anticipated the idea of code annotations, and
tit added a way to add extra information on things like function definitions,
that are _completely ignored_ by the interpreter itself, but can be inspected by
other tools.

It looks like this:

```{.python .example}
age: int = 18

def is_adult(age: int) -> bool:
    if age >= 18:
        return True

    return False
```

The annotations `: int` and `-> bool` here don’t do anything. They’re ignored
when the code is run, almost like comments. In fact, you can use these
annotations for pretty much anything else, like documentation for example:

```{.python .example}
def compile(
    source: "something compilable",
    filename: "where the compilable thing comes from",
    mode: "is this a single statement or a suite?"
):
   ...
```

> There’s more examples of this syntax, as well as its specification provided in
> [PEP-3107](https://python.org/dev/peps/pep-3107).

But in our case, we are going to use this code annotation feature that Python
gives us, to define data types for all of our code. And as we do that, we will
use a type checking tool like `mypy` to validate the types added.

## Type Checking Our Python Code

Let’s start with a simple piece of code that doesn’t have any type annotations,
and try to get a bit familiar with mypy.

Here’s the code:

```{.python .example}
def double(n):
    return n * 2

num = double(21)
print(num)
```

If you run it, it prints out 42, simple enough. And although the code doesn't
have any type annotations yet, if you try to type-check it, you get this output:

```text
Success: no issues found in 1 source file
```

Now, that might seem a bit weird. Somehow, without any type annotations, our
code still passes the type check. But that’s intended behavior – the types are
_optional_. Since the code didn’t have any types, it didn’t check anything by
default.

We can, however, force mypy to check all your code, by using the `--strict`
parameter:

[TODO: strict mode]

```{.python .example}
def double(n):
    return n * 2

num = double(21)
print(num)
```

And now we can see what mypy has to say about the file: It doesn’t have types.
So let’s add the type annotations to make mypy happy in this case. The
annotations (sometimes called type hints) are a vast topic and there’s a lot to
cover about it, but in this case the types are really simple. We just have to
tell the function double(n), what the type of “n” is. Like so:

```{.python .example}
def double(n: int) -> int:
    return n * 2

num = double(21)
print(num)
```

With these annotations, mypy now knows that the function double(n) wants to
accept an integer, and when it gets an int, it also returns an int (`-> int` is
the function’s return-type annotation). And sure enough, mypy is happy, and the
code still runs just fine.

Your code is now 100% type checked! To confirm, let’s try to call the function
with something other than an integer:

```{.python .example}
def double(n: int) -> int:
    return n * 2

value = double("some text")
```

Mypy is able to tell that something is wrong with the code. The error message
states that the function double expected an integer, but got a string instead.

Isn’t this amazing? Now you have a tool that, with just a little bit of extra
work of adding type hints in a few places, can catch a lot of the bugs in your
code, even before you run it.
