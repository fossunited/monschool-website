---
title: Hello Python
include_in_preview: false
---

## Running the Python Interpreter

Python comes with an interactive interpreter. When you type `python3` in your shell or command prompt, the python interpreter becomes active with a `>>>` prompt and waits for your commands.

```
$ python3
Python 3.9.5 (default, May 19 2021, 11:32:47)
[GCC 10.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Now you can type any valid python expression at the prompt. python reads the typed expression, evaluates it and prints the result.

```
>>> 1 + 2
3
```

Congratulations. You've written your first python program!

The Python interpreter, or the Python REPL (Read-Eval-Print-Loop) is a quick way to use Python for doing simple computations.

## Running the Python Scripts

Often, we write programs and run them mutliple times. Let's see how to do that with Python.

Open your text editor and type the following text and save it as `hello.py`.

```
print("hello, world!")
```

And run the program from your terminal or command-prompt by typing `python hello.py`.

```
$ python hello.py
hello, world!
```

The program calls a `print`, a function to display a message on screen and whatever we have between the double quotes is the input to the `print` function.

Try changing the program to print your name instead of `hello, world!`.

## The Course Environment

In this course we'll use a live coding environment where you can try the examples online.

Run the following example, by clicking on the `Run` button.

```{.python .example}
print("Hello, world!")
```

## Variables


It is very easy to use variables in Python.

```{.python .example}
x = 10
y = 20
z = x + y
print(z)
```

In the above example `x`, `y` and `z` are variables.

Unlike other static typed languages like C or Java, variables in Python don't have any type associated with them.

```{.python .example}
x = 10
print(x)

x = "hello"
print(x)
```

As you can see, the value of x was intially an integer and then x was reassigned to a string value. This is prefectly valid in Python.

Often, beginner programmers get confused about strings and variables. Strings are the text values that we enclose in quotes and variables are names that refer to some values.

The following program is supposed to print `Python`, but it is printing text "name". Can you identify what is the mistake in this program?

```{.python .example}
name = "Python"
print("name")
```

## Comments

