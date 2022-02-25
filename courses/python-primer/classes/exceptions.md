---
title: Exception Handling
include_in_preview: false
---

We’ve already seen exceptions in various places.

Python gives `NameError` when we try to use a variable that is not defined.

```{.python .example}
print(no_such_variable)
```

We get a `ValueError` when we convert convert an invalid value to integer.

```{.python .example}
n = int("bad-number")
```

We get a `FileNotFoundError` error when try to open a file that doesn't exist.

```{.python .example}
contents = open("no-file").read()
```

In all these above cases, Python is raising an exception and the default behavior on exceptions is to crash. However, it is possible to except these exceptions and recover from them.

Python uses `try-except` statements to handle exceptions. It is typically used this way:

```
try:
    somecode_that_can_raise_exceptions()
except SomeException:
    recover_from_exception()
```

For example, the following code has a `toint` function that returns `0` when a bad value is given as input.


```{.python .example}
def toint(strvalue):
    try:
        return int(strvalue)
    except ValueError:
        print("Bad number:", strvalue)
        return 0

a = "5"
b = "bad-number"
c = toint(a) + toint(b)
print(c)
```

We can also use optional `else` and `finally` clauses with `try-except`.

The `else` clause is used to specify code whe no exception happens and `finally` is used to specify code that need to run whether or not exception happens. The `finally` is typically used to close the resources created.

```{.python .example}
value = 'a'
# value = '10'

try:
    int(value)
except ValueError:
    print("Bad value", value)
else:
    print("in else")
finally:
    print("in finally")
```


## Understanding Tracebacks

When an exception happens, Python prints the traceback execution. Let's look at an example to understand it better.

```{.python .example}
def read_file(filename):
    return open(filename).read()

def read_words(filename):
    contents = read_file(filename)
    return contents.split()

def main():
    filename = "bad-file"
    words = read_words(filename)
    print(f"found {len(words)} words")

main()
```

You can see that the traceback has the following:

```
Traceback (most recent call last):
  File "/app/main.py", line 13, in <module>
    main()
  File "/app/main.py", line 10, in main
    words = read_words(filename)
  File "/app/main.py", line 5, in read_words
    contents = read_file(filename)
  File "/app/main.py", line 2, in read_file
    return open(filename).read()
FileNotFoundError: [Errno 2] No such file or directory: 'bad-file'
```

You can see the flow of execution that caused the error, including the actual line of code that have contributed to the error. Here is quick summary of the traceback:

* `main` function was called in line 13
* that called `read_words` in line 10
* that called `read_file` in line 5
* that called `open` in line 2 and that failed

Whenever you see a traceback, usually the last entry is the most interesting one. But sometimes, the last few entries would be in standard library modules and we need to move up to see which code written by us is contributing to the error.

## Raising Exceptions

We can raise an exception using the `raise` statement.

```{.python .example}
def withdraw(amount):
    if amount < 0:
        raise ValueError("Can't withdraw a negative amount")

withdraw(-10)
```

We can also create our exceptions. The following example creates a new exception `BankException` and raised it when

```{.python .example}
class BankException(Exception):
    pass

balance = 100

def withdraw(amount):
    global balance
    if amount > balance:
        raise BankException("Insufficient balance")
    balance = balance - amount
    print(f"{amount} withdrawn. Current balance is {balance}.")

withdraw(50)
withdraw(80)
```
