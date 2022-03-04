---
title: Datatypes
include_in_preview: false
---

Python, like any other programming language, supports multiple datatypes. In this lesson, we'll review the most common datatypes used in Python.

## Integers

Python has integers.

```{.python .example}
print(1 + 2)
```

We can do the usual arthemetic operators `+`, `-`, `*` and `/`.

```{.python .example}
print(7 + 2)
print(7 - 2)
print(7 * 2)
print(7 / 2)
```

There is a special operator `//` is used for integer division.

```{.python .example}
print(7 // 2)
```

And the `**` operator is used to exponentiation or to raise a number to a power.

```{.python .example}
print(2 ** 10)
```

It is fun to play with large numbers in Python.

```{.python .example}
print(2 ** 1000)
```

## Floating Point Numbers

Python has floating point numbers. All operators that work on integers work on float point numbers too.

```{.python .example}
print(0.1 + 0.2)
```

You may be surprised why the answer is not `0.3`. That is a do with how the number of represented internally. We are not going into those details for now, you can google for `0.1 + 0.2` to find more about it.

## Strings

Python has string to represent text. Strings are enclosed in single quotes or double quotes.

```{.python .example}
name = "Python"
print("Hello", name)
```

We can use the `+` operator to concatinate two strings.

```{.python .example}
x = "hello" + "python"
print(x)
```

The `*` operator can be used to repeat a string multiple times.

```{.python .example}
print("hello" * 4)
print("=" * 20)
```

The built-in function `len` can be used to find the length of a string.

```
name = "Python"
print(len(name))
```

Python supports writing multi-line strings. They are enclosed in three single quotes of three double-quotes. They are typically used to write multi-line messages that we want to print or send an email etc.

```{.python .example}
message = """
Hello everyone,

Welcome to the Python Primer course!
"""

print(message)
```

Python supports the usual escape codes. The new line character is represented as `\n` and the tab character is represented as `\t`.

```{.python .example}
print("a\nb\nc")
print("1\t2\t3")
```

The strings also support unicode strings. The following example demonstrates strings written in multiple Indian languages.

```{.python .example}
print("అ ఆ ఇ ఈ") # Telugu
print("ಅ ಆ ಇ ಈ") # Kannada
print("அ ஆ இ ஈ") # Tamil
print("അ ആ ഇ ഈ") # Malayalam
print("अ आ इ ई") # Hindi
```

The unicode characters can also be written using their unicode code points.

```{.python .example}
print("\u0c05 \u0c06 \u0c07 \u0c08") # Telugu
print("\u0c85 \u0c86 \u0c87 \u0c88") # Kannada
print("\u0b85 \u0b86 \u0b87 \u0b88") # Tamil
print("\u0d05 \u0d06 \u0d07 \u0d08") # Malayalam
print("\u0905 \u0906 \u0907 \u0908") # Hindi
```

## Bytes

Python has a `bytes` datatype to represent binary data.

The bytes are written just like strings, but with  `b` prefix.

```{.python .example}
data = b'abcd \x01\x02\x03\x04'
print(data)
```

In the above example, the letter `a` corresponds to a byte with value `97`, which is the ascii code of the letter `a`. The `\x01` is presents byte with value `1`, written as two-digit hexadecimal number using prefix `\x`.

We'll learn more about bytes in the later lessons.

## Lists

Python has a lists to represent a collection of values.

```{.python .example}
x = ['a', 'b', 'c']
print(x)
```

A list can contain values of different types, including other lists.

```{.python .example}
x = ['a', 'b', 1, 2, ['p', 10]]
print(x)
```

Individual elements of a list can be accessed by indexing it using the `[]` operator. The index starts with `0`.

```{.python .example}
x = ['a', 'b', 'c']
print(x[0]) # the first element is at index 0
print(x[1]) # the second element is at index 1
print(x[2]) # the third element is at index 2
```

The built-in function `len` is used to find the length of a list.

```{.python .example}
x = ['a', 'b', 'c']
print(len(x))
```

## Dictionaries

Dictionaries are used to represent name-value pairs. The dictionaries are very hand datastrcutures in Python and learning to use them effectively is a great asset.

```{.python .example}
person = {
    "name": "Alice",
    "email": "alice@example.com",
    "phone": "1234",
    "verified": True
}

print(person)
print(person['email'])
```

The values in a dictionary can be accessed using the key. In the previous example, we've printed the value of entry associated with the key `email`.

We'll learn more about dictionaries in the latter chapters.

## Boolean Values

Python has boolean values too. The keywords `True` and `False` represent the boolean truth and false.

```{.python .example}
print(True)
print(False)
```

The conditional expressions are evalued to boolean values.

```{.python .example}
filesize = 100
print(filesize > 50)
print(filesize > 200)
```

## Other Datatypes

Python have some other interesting datatypes as well.

The `None` is special value use to indicate nothing.

Python has another datatype called `tuple` for representing fixed width records. Tuples behave just like lists, but they are immutable.

```{.python .example}
point = (2, 3)
print(point)
print(point[0], point[1])
```

Python allows multiple-assignment also and it is handly to unpack tuples.

```{.python .example}
point = (2, 3)
x, y = point
print(x, y)
```

When writing tuples, the parenthesis can be omitted most of the times.

```{.python .example}
point = 2, 3
print(point)
print(point[0], point[1])
```

Python has a `set` datatype too. A set is an unordered collection of elements.

```{.python .example}
x = {1, 2, 3}
print(x)
```

## Summary

In this lesson, we've seen various commonly used datatypes of Python. While they look very simple, mastering them takes a bit of practice. Make sure you go through all the examples and the practice problems in the subsequent lessons.
