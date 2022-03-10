---
title: Installing mypy on your machine, and in your code editor
include_in_preview: true
---

Before we move ahead with the rest of the course, I want to explain how you can
install mypy on your machine and code editor.

## Installing mypy locally

To run `mypy` locally, you need to have Python installed.

- If you're running Windows 10, you can open Command Prompt, and type `python`,
  which should either start Python, or open up Windows Store, where you can
  install it.
- On a Mac or linux machine, you probably already have Python installed, under
  the name `python3`. Simply open a terminal and type `python3` to confirm.

Now to install mypy, you need to run `pip`, a package manager which comes with
Python:

```console
$ python -m pip install mypy
Collecting mypy
[...]
Successfully installed mypy-0.x typing-extensions-4.x
```

Now you should have access to the `mypy` command:

```console
$ mypy
usage: mypy [-h] [-v] [-V] [more options; see below]
            [-m MODULE] [-p PACKAGE] [-c PROGRAM_TEXT] [files ...]
mypy: error: Missing target module, package, files, or command.
```

To test it, pass it the name of any Python file:

```console
$ mypy code.py
Success: no issues found in 1 source file
```

## Editor integration

While mypy and the other type checkers can be used directly through the command line, it is a bit more convenient for IDE users if the type checking errors integrate directly with their editor. There are two popular editors for Python users which can do this, Visual Studio Code and PyCharm. Let’s take a look at them.

### Visual Studio Code

VSCode has a Python extension that comes with an official language server called “Pylance”, which provides type information out of the box.

You can however, enable mypy support in VSCode as well, by adding the following to your settings.json file:

```json
  ...
  "python.linting.mypyEnabled": true,
  "python.linting.mypyArgs": [
    "--ignore-missing-imports",
    "--follow-imports=silent",
    "--show-column-numbers",
    "--strict"
  ],
...
```

You should then be able to see type checking issues directly in your code:

{{ Image("vscode.png") }}

If you don’t, restart your editor and that should resolve any issues.

### PyCharm

PyCharm has created its own type inference and refactoring system that works quite well and provides things like attribute auto-completion in the IDE by default. If you want to integrate `mypy` however, a Plugin called “Mypy” made by Roberto Leinardi exists in the JetBrains Marketplace. Simply installing it should enable mypy checks for you:

{{ Image("pycharm.png") }}
