---
title: Using mypy to type-check your code
include_in_preview: false
---

Now that we have mypy set up, let's figure out how to use it for your files and
projects.

Running it on a single file is the most straightforward way. Let's make one and
test it:

<span
    id="livecode-options-mypy1"
    data-stdin='Alice\n8\n'
    ></span>

```{#mypy1 .python .example}
def greet(name):
    print(f"Hello, {name}!")

if __name__ == '__main__':
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    greet(name)
    print(f"You will be {age + 1} years old next year.")
```

Saving it as a file named `code.py`. To type check it, just do:

```console
$ mypy code.py
code.py:9: error: Unsupported operand types for + ("str" and "int")
Found 1 error in 1 file (checked 1 source file)
```

Mypy says there's a problem in line 9, and yeah, we forgot to cast `age` to an
integer. So let's do that:

<span
    id="livecode-options-mypy2"
    data-stdin='Alice\n8\n'
    ></span>


```{#mypy2 .python .example}
def greet(name):
    print(f"Hello, {name}!")

if __name__ == '__main__':
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    greet(name)
    print(f"You will be {age + 1} years old next year.")
```

Now let's see what mypy says:

```console
$ mypy code.py
Success: no issues found in 1 source file
```

You've already seen that `mypy` has a "strict mode", and a non-strict mode. Mypy
by default won't complain about functions that don't have type annotations. To
use mypy in strict mode, you just have to pass the `--strict` flag:

```console
mypy --strict code.py
code.py:1: error: Function is missing a type annotation
code.py:8: error: Call to untyped function "greet" in typed context
Found 2 errors in 1 file (checked 1 source file)
```

It says accordingly, that we are missing type annotations on `def greet()`.
Let's fix that:

<span
    id="livecode-options-mypy3"
    data-stdin='Alice\n8\n'
    ></span>

```{#mypy3 .python .example}
def greet(name):
    print(f"Hello, {name}!")

if __name__ == '__main__':
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    greet(name)
    print(f"You will be {age + 1} years old next year.")
```

And now `mypy` is happy again.

### Using mypy on a project

You can pass an entire folder for `mypy` to check, and it will find every single
python file inside it and check it.

Say you have a folder structure like this:

```console
myproject
├── setup.py
└── src/
    ├── bar.py
    └── foo.py
```

Using the command `mypy <folder name>` will check all the 3 files:

```console
$ mypy myproject
Success: no issues found in 3 source files
```

Notice that it says "3 source files". Similarly, you can also do
`mypy --strict myproject` to run it in strict-mode on all files.

Now that you have mypy set-up and running locally, you can run and type check
your code on your own machine as well.
