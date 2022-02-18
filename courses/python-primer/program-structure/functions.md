---
title: Functions
include_in_preview: false
---

In this lesson we'll learn about how to use built-in functions, methods and writing our own functions.

## Functions

Python has many built-in functions. We've seen some of the already.

```{.python .example}
print("Python")

n = len("Python")
print(n)
```

In the above example, `print` and `len` are built-in functions. The built-in functions are available to all programs.

For example, `abs` is another built-in function that computes the absolute value of a number.

```{.python .example}
a = abs(3)
b = abs(-3)
print(a, b)
```

You may have noticed that Python doesn't allow operations on incompatible datatypes.

```
>>> 1 + '2'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

If you want to add an integer to a string, you need convert the integer to a string or the string to an integer. The built-in functions `int` and `str` come handy in this case.

```{.python .example}
x = 1 + int('2')
y = str(1) + '2'

print(x, y)
```

### Example: Counting the number of digits in a number

How to count the number of digits in a number?

The following example shows some really big numbers. What does it take to count the number of digits in them?

```{.python .example}
print(12345)
print(2**100)
print(2**1000)
```

We know that we can use the `len` function to compute the length of a string, but here we have an integer, not a string. So we need to convert the integer to a string first using the `str` function and then apply `len`.

```{.python .example}
n = len(str(2**1000))
print(n)
```

## Writing Custom Functions

While using built-in functions is handy in a lot of cases, sometimes we want to define our own functions to avoid repeating the same code again and again.

Let's define a function to compute square of a number.

```{.python .example}
def square(x):
    return x*x

n = square(4)
print(n)
```

Notice that the body of the function is indented, typically by 4 spaces. Python uses indentation to identify the code that is part of the function body.

We could write the same function as follows:

```{.python .example}
def square(x):
    y = x*x
    return y

n = square(4)
print(n)
```

#### _print_ vs _return_

Often beginners get confused between `print` and `return`.

Consider the following two functions.

```{.python .example}
def square1(x):
    return x*x

def square2(x):
    print(x*x)

print(square1(4))
square2(4)
```

The function `square1` is returning a value where as the function `square2` is printing the value instead of returning. When we run the program, both functions seems to be working exactly in the same way. Is that really true? Can we find a case where they work quite differently?

Let's say we want to add the number 1 to the square. It is possible to do it using `square1` as it is returning the value, which can be used in other computations.

```{.python .example}
def square1(x):
    return x*x

n = square1(4) + 1
print(n)
```

It is not possible to do that same with `square2` without changing the definition of that function because it is printing the value directly and not returning anything back to the caller.

## Functions are values too!

Functions are first-class objects in Python. Funtions are like any other variables with the value being of datatype function. They can be assigned to other variables, or passed as arguments to other functions or can even returned from functions.

```{.python .example}
def square(n):
    return n*n

print(square(4))
print(square)

f = square
print(f(4))
```

If you see the second print statement, it is printing the value of the function itself. Don't worry about the hexadecimal value after the function name. It is printing that it is a function with a particular name.

In the last part of the program, we've assigned to the value of `square` to a variable `f`, which means `f` has exactly the same value as of `square`, which is the square function. So we were able to call `f` like a function in the last line.

While this may sound absurd. Why would anyone want to do it?

Well, there are many use cases and you'll be surprised how powerful this feature is.

Let's say we want to compute sum of squares of two numbers.

```{.python .example}
def square(n):
    return n*n

def sum_of_squares(x, y):
    return square(x) + square(y)

n = sum_of_squares(3, 4)
print(n)
```

What if I want to do the same thing for cubes instead of squares? One way to do that would be to copy the code and replace square with cube.

```{.python .example}
def cube(n):
    return n*n*n

def sum_of_cubes(x, y):
    return cube(x) + cube(y)

n = sum_of_cubes(3, 4)
print(n)
```

If you compare the above two programs, they are almost identical. Can be generalize both `sum_of_squares` and `sum_of_cubes` into a single function?

```{.python .example}
def sumof(f, x, y):
    # print("sumof", f, x, y)
    return f(x) + f(y)

def square(n):
    return n*n

def cube(n):
    return n*n*n

print(sumof(square, 3, 4))
print(sumof(cube, 3, 4))

print(sumof(len, 'hello', 'python'))
```

As you can see the `sumof` function is taking three arguments. The first one is a function and the remaining two are the arguments that are passed to that function.

If we call `sumof` with `square` as first argument and pass two numbers as other arguments, it would call the function `square` for each of those numbers, adds the results and return it back. The same applies when we pass `cube` as the first argument.

This feature of passing functions as arguments to other functions is so useful that there are many built-in functions that accept functions as arguments.

For example, Python has a built-in function `max` to compute maximum of two values or a list of values.

```{.python .example}
n = max(3, 4)
print(n)

n = max([3, 4, 5, 2])
print(n)
```

What do you think would be the value of `max(['one', 'two', 'three', 'four', 'five'])`?

```{.python .example}
x = max(['one', 'two', 'three', 'four', 'five'])
print(x)
```

Why is this giving `two`? Why not `three`? Why not `five`?

The way it works is it compares the words by the dictionary ordering and `two` comes at the end in the dictionary ordering.

What if we want to find the longest word instead?

```{.python .example}
numbers = ['one', 'two', 'three', 'four', 'five']
n = max(numbers, key=len)
print(n)
```

The built-in function `max` accepts an optional argument `key`, which is a function when passed, used to compute the value used for comparison.

The following example demonstrates what really happens. We are using a function `mylen` instead of `len`, which works like `len`, but prints the value it is called with.

```{.python .example .show-output}
def mylen(x):
    print("mylen", x)
    return len(x)

numbers = ['one', 'two', 'three', 'four', 'five']
n = max(numbers, key=mylen)
print(n)
```

As you can see, the `mylen` function is called with every element of the list `numbers` as argument, which is done by the `max` function when computing the maximum.

## Methods

Methods are special kind of functions that work on an object.

Let's look at the following example:

```{.python .example}
x = "Hello"
print(x.upper())
print(x.lower())
```

Notice that we are calling `upper` as `x.upper()`. In this case, `upper` is a method called on object `x`, which is a string. The `upper` method is defined in the `str` type and is available to all  values of that type.

Let's look at some more methods available on strings.

```{.python .example}
n = "mathematics".count("mat")
print(n)

x = "mathematics".replace("mat", "rat")
print(x)
```

As you can see, the count method computes the number of occurances of a substring in a string and the `replace` method returns a new string after replacing the occurances of a substring specified as the first argument with the second one.

Let's look at some more interesting methods on strings.

The `split` method splits a string on a delimiter.

```{.python .example}
sentence = "Anything that can go wrong, will go wrong"
words = sentence.split() # split on any white space
print(words)

parts = sentence.split(",")
print(parts)
```

When the `split` method is called without any arguments, it considers any whitespace (including tab and new line) as delimiter.

We've seen how to split a string. Now, let's see how to join them back.

```{.python .example}
s1 = " ".join(["a", "b", "c"])
print(s1)

s2 = "-".join(["a", "b", "c"])
print(s2)

s3 = "::".join(["a", "b", "c"])
print(s3)
```

The `join` method is called on the delimiter and it takes a list of strings as argument and returns the string generated by combining all the elements of the list with the delimiter.

