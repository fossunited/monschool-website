---
title: Modules
include_in_preview: false
---

Python comes with many built-in modules.

A module is imported using the `import` statement.

The following example imports the time module and prints the current time using the `asctime` function defined in that module.

```{.python .example}
import time
print(time.asctime())
```

The `os` module provides functions related to files and processes.

The following example prints the current working directory.

```{.python .example}
import os
print(os.getcwd())
```

The `listdir` funtion lists all the files in a given directory.

```{.python .example}
import os

print(os.listdir("."))
```

Python comes with many built-in modules. We'll explore lot more modules in the upcoming lessons.

## Reading Command-line arguments

The `sys` module keeps trak of the command-line arguments passed to a program.

<span id="livecode-options-args1" data-args="hello world"></span>

```{#args1 .python .example .show-args}
import sys
print(sys.argv)
```

The above example prints all the command-line arguments passed to the program. As you can see the `sys.argv` will always be a list with the program name as first argument, followed by all the arguments passed to it.

Please note that the elements of `sys.argv` will always be strings.

Try changing the arguments to something else.

### Example: echo

Let's try to implement a simple version of the `echo` command of unix.

The echo command prints the command-line arguments passed to it.

```
$ echo hello
hello

$ echo hello world
hello world
```

We'll implement a simple version that just prints the first argument.

<span id="livecode-options-args2"
    data-args="hello"
    data-source-file="echo.py"></span>

```{#args2 .python .example .show-args .multi-file}
=== echo.py
import sys
print(sys.argv[1])
```

Command-line arguments are most common way to take user inputs. We are going to use this a lot more in the examples of upcoming lessons.

**Problem:** Write a program `square.py` that takes a number as command-line argument and prints its square.

```
$ python square.py 2
4
$ python square.py 5
25
```
