---
title: Control Flow
include_in_preview: false
---

In this lesson we'll look at constructs for control flow in Python, including conditional expressions, `if` statement, `while` loop and `for` loop.

## Conditional Expressions

Conditionals expressions are expressions with boolean operators check certain condition and they evaluates to `True` of `False`.

The usual comparision operators `>`, `>=`, `<`, `<=`, `==` and `!=` can be used to compare numbers.

```{.python .example}
price = 70

print(price > 50)
print(price < 50)
```

We can use the `in` and `not in` operators to check a substring is present in a string.

```{.python .example}
message = "hello"
print("el" in message)
print("hell" in message)
print("hell" not in message)
```

The `in` and `not in` operators can also be used to check an element is present in a collection like a list or a dictionary.

```{.python .example}
value = "a" in ["a", "e", "i", "o", "u"]
print(value)

value = 3 in [1, 2, 3, 4]
print(value)

value = "x" in {"x": 1, "y": 2}
print(value)
```

We can also use the methods `startswith` and `endswith` on strings.

```{.python .example}
filename = "hello.py"
print(filename.endswith(".py"))

filename = "hello.c"
print(filename.endswith(".py"))
```

### Combining Conditional Expressions

The `not` operator can be used to negate a boolean expression.

```{.python .example}
filename = "hello.py"
print(filename.endswith(".py"))
print(not filename.endswith(".py"))
```

Multiple conditional expressions can be combined using the `and` and `or` operators.

```{.python .example}
filename = "hello.txt"
value = ".." not in filename and filename.endswith(".txt")
print(value)
```

Note that `and` and `or` are short-circuit operators.

In `a and b`, `b` is evaluted only if `a` is True.
In `a or b`, `b` is evaluted only if `a` is False.


```{.python .example}
filename = "hello.txt"

# the second expressions doom() is not executed
# because the first expression of and is False
value = filename.endswith(".py") and doom()
print(value)

# the second expression doom() is not executed
# because the first expression of or is True
value = filename.endswith(".txt") or doom()
print(value)
```

In the above example, the function `doom`, which is not defined at all is not called becuase the reasons mentioned in the comments.

## The `if` Statement

The `if` statement is used to make decisions in code.

```{.python .example}
n = 33

if n % 2 == 0:
    print("even")
else:
    print("odd")
```

The above example prints whether the number `n` is even or odd.

Please note that the block of code that is part of `if` clause or `else` clause is indented.

We can use `elif` clause when we need to check multiple condition.

```{.python .example}
n = 56

if n < 10:
    print(n, "is a single-digit number")
elif n < 100:
    print(n, "is a two-digit number")
else:
    print(n, "is a big number")
```

## The `while` statement

The `while` statement is used to execute a loop.

```{.python .example}
n = 1
while n <= 10:
    print(n, n*n)
    n = n + 1
```

Just like `if`, the body of `while` is indented.

## The `for` statement

The `for` statement is used to iterate over a list of values.

```{.python .example}
numbers = ["one", "two", "three", "four", "five"]
for n in numbers:
    print(n)
```

We'll learn more about for loops in the upcoming lessons.
