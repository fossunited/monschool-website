---
title: Mypy configuration
include_in_preview: false
---

As of now, we've seen two "modes" for mypy to operate in, regular mode and
"strict" mode. Regular mode seems to be a lot more lax, but it doesn't catch as
many errors as it possibly can.

But there's a whole spectrum of in-between that you can set mypy to find or
ignore, to suit your needs or your project's needs. We're going to take a look
at that right now.

## So what is `--strict` really?

`mypy --strict somefile.py` is actually the same as:

```console
mypy --disallow-subclassing-any
     --disallow-untyped-calls
     --disallow-untyped-defs
     --disallow-incomplete-defs
     --check-untyped-defs
     --disallow-untyped-decorators
     --no-implicit-optional
     --warn-redundant-casts
     --warn-unused-ignores
     --warn-return-any
     --no-implicit-reexport
     --strict-equality
     somefile.py
```

Each of these flags makes mypy a little bit more strict. Let's look at some of
the more important ones:

### `--disallow-incomplete-defs` and `--disallow-untyped-defs`

The `--disallow-incomplete-defs` flag makes mypy raise an error whenever it sees
a function that has partial annotations.

Here's some example code:

```python
def untyped(x):
    print(x)

def incomplete(x: int):
    print(x)

def complete(x: int) -> None:
    print(x)
```

Running mypy with `--disallow-incomplete-defs` on this code gives us:

```console
$ mypy --disallow-incomplete-defs mycode.py
mycode.py:4: error: Function is missing a return type annotation
Found 1 error in 1 file (checked 1 source file)
```

`--disallow-untyped-defs` is a stricter version of this, where functions with no
type hints are also flagged:

```console
$ mypy --disallow-untyped-defs mycode.py
mycode.py:1: error: Function is missing a type annotation
mycode.py:4: error: Function is missing a return type annotation
Found 2 errors in 1 file (checked 1 source file)
```

### `--check-untyped-defs`

Since mypy doesn't check the code inside untyped functions, you can run into
situations like:

```python
def foo():
    return "abc" + 42
```

`mypy` is fine with this by default:

```console
$ mypy mycode.py
Success: no issues found in 1 source file
```

But you can start checking the bodies of untyped functions by doing:

```console
$ mypy --check-untyped-defs mycode.py
mycode.py:2: error: Unsupported operand types for + ("str" and "int")
Found 1 error in 1 file (checked 1 source file)
```

### `--strict-equality`

Mypy also doesn't shout about "impossible" conditionals, like these:

```python
x = 40
x += 2

if x == "foo":
    print('x is foo')
```

Since `x` can never be a string, it's a weird conditional. But it's not flagged
by default:

```console
$ mypy mycode.py
Success: no issues found in 1 source file
```

But you can do this:

```console
$ mypy --strict-equality mycode.py
mycode.py:4: error: Non-overlapping equality check (left operand type: "int", right operand type: "Literal['foo']")
Found 1 error in 1 file (checked 1 source file)
```

## Using a config file

The easiest way to create a config file for mypy is to make a `mypy.ini` file,
and add your configuration to it. Like, if you use the following flags:

`mypy --disallow-incomplete-defs --strict-equality mycode.py`

You can make this config file:

```ini
[mypy]
disallow_incomplete_defs = True
strict_equality = True
```

And then simply running `mypy mycode.py` will use the configuration.

A general config that I recommend, and use in my projects is this:

```ini
[mypy]
strict = True
exclude = setup.py|venv|build
```

`exclude` sets the paths to ignore during a mypy run. This avoids mypy type
checking the `venv` folder for example, when you do `mypy .` in your project.
