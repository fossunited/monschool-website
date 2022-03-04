---
title: Lists
include_in_preview: false
---

We've already seen lists in the datatypes lesson. Lets learn more about them.

As you already know, the `len` function can be used to find the length of a list.

```{.python .example}
x = ["a", "b", "c", "d"]
print(x)
print(len(x))
```

Individual elements of a list can be accessed using the `[]` operator. The indexing starts with `0`. It is also possible modify the elements of a list by assigning a new value to them.

```{.python .example}
x = ["a", "b", "c", "d"]
print(x[0], x[1])

x[0] = 'aa'
print(x)
```

## For loop

The `for` loop is used to iterate over a list of elements.

```{.python .example}
names = ["Alice", "Bob", "Charlie", "Dave"]

for name in names:
    print("Hello", name)
```

Please note that the body of the for loop is indented.

If we use the for loop in a function, then the loop itself will be indented to place it inside the function and the body of the for loop will be indented by one more level.

```{.python .example}
def welcome_all(names):
    for name in names:
        print("Hello", name)

names = ["Alice", "Bob", "Charlie", "Dave"]
welcome_all(names)
```

Let's take up a small problem. How to print words of sentence, each in a seperate line?

```{.python .example}
sentence = "when in doubt, use brute force"

words = sentence.split()
# print(words)

for word in words:
    print(word)
```

We can also combine the split and the loop into a single line.

```{.python .example}
sentence = "when in doubt, use brute force"
for word in sentence.split():
    print(word)
```

### Example: sum

Python has a built-in function `sum`.

```{.python .example}
a = sum([1, 2, 3, 4])
b = sum(range(10))
c = sum(range(100))

print(a, b, c)
```

Let's try to implement our own sum function.

```{.python .example}
def my_sum(numbers):
    # initialize the result to the initial value
    result = 0

    # update the result in every iteration of the loop
    for n in numbers:
        result = result + n

    # finally, return the result
    return result


a = my_sum([1, 2, 3, 4])
b = my_sum(range(10))
c = my_sum(range(100))

print(a, b, c)
```

## The `range` function

The `range` function is used to create a sequence of numbers.

For example, `range(5)` creates 5 numbers starting from 0. That includes 0, 1, 2, 3 and 4. Please note that the number 5 is not included in it.

We can use the for loop to iterate over a range.

```{.python .example}
for i in range(5):
    print(i)
```

We can use the `list` function to quickly see the elements of a range.

The `range` function can also be used with 2 or 3 arguments as shown in the example below.

```{.python .example}
# numbers from 0 to 5 (last is not included)
print(list(range(5)))

# number from 2 to 5
print(list(range(2, 5)))

 # number from 2 to 20 in steps of 3
print(list(range(2, 20, 3)))
```

If we want to print a message `n` times, we can do that using a `range`.

```{.python .example}
for i in range(3):
    print("hello")
```

## Growing Lists

Let's see how to grow a list by adding new elements to it.

Lists have a method `append` that add a new element to a list at the end.


```{.python .example}
x = ['a', 'b', 'c']
print(x)

x.append('d')
print(x)

x.append('e')
print(x)
```

### Example: squares

Let's write a function `squares`, that takes a list of numbers as argument and computes squares of each one of them.

Here is what we expect when we run the `square` function.

```
>>> squares([1, 2, 3, 4])
[1, 4, 9, 16]
>>> squares([2, 3])
[4, 9]
```

Let's see how to implement it.

```{.python .example}
def squares(numbers):
    result = []
    for n in numbers:
        result.append(n*n)
    return result

a = squares([1, 2, 3, 4])
print(a)

b = squares([2, 3])
print(b)

c = squares(range(10))
print(c)

# sum of squares of all integers below one million
d = sum(squares(range(1000000)))
print(d)
```

## List Comprehensions

List comprehensions are very expressive way to transform a list into another.

```{.python .example}
numbers = [1, 2, 3, 4, 5, 6]

a = [n*n for n in numbers]
print(a)

b = [n*n for n in numbers if n %2 == 0]
print(b)
```

Let's try to understand the pattern clearly:

```
[expr for a_var in a_list]
[expr for a_var in a_list if some_condition]
```
Let's see the same as for loop:

```
result = []
for a_var in a_list:
    result.append(expr)

result = []
for a_var in a_list:
    if some_condition:
        result.append(expr)
```

How to find all the python files in the current directory?


```{.python .example}
import os
files = [f for f in os.listdir(".") if f.endswith(".py")]
print(files)
```

How to find the total size of all the python files in the current directory?

```{.python .example}
import os
size = sum([os.path.getsize(f)
            for f in os.listdir(".")
            if f.endswith(".py")])
print(size)
```

## Iteration Patterns

Let's review the common iteration patterns used in Python.

### Iterating over a list

The most commonly used iterating pattern is iterating over a list of values.

```{.python .example}
x = ['a', 'b', 'c', 'd']

for a in x:
    print(a, a.upper())
```

We can also use this pattern in a list comprehension.

```{.python .example}
x = ['a', 'b', 'c', 'd']
y = [a.upper() for a in x]
print(y)
```

### Iterate over a sequence of numbers

The `range` function is used whenever  we need to iterate over a sequence of numnbers.

```{.python .example}
for i in range(5):
    print(i, i*i)
```

And here is the list comprehension version of the same pattern.

```{.python .example}
squares = [i*i for i in range(5)]
print(squares)
```

### Iterating over two lists together

Sometimes we need to iterate over two lists together, and the built-in function `zip` takes care of that.

```{.python .example}
fruits = ['Apple', 'Banana', 'Mango', 'Orange']
prices = [10, 20, 30, 40]

for fruit, price in zip(fruits, prices):
        print(fruit, price)
```

### Iterating over the index and the elements together

Sometimes we need to the index of the element we are accessing. Python covered you there too using the built-in function `enumerate`.

For example, consider the following program where we are trying to print the index and the title of every chapter in a book.

```{.python .example}
chapters = [
    "Getting Started",
    "Functions",
    "Lists",
    "Dictionaries"
]

for i, title in enumerate(chapters):
    print(f"Chapter {i+1}: {title}")
```

## List Indexing

We've already seen how to index a list, but there is more to indexing.

The common way to index a list using the index starting with 0.

```{.python .example}
x = ['a', 'b', 'c', 'd']
print(x[0])
print(x[1])
```

Python also supports indexing from the other end using negative indexes.

```
+----+----+----+----+
|  a |  b |  c |  d | list
+----+----+----+----+
|  0 |  1 |  2 |  3 | --> regular index
+----+----+----+----+
| -4 | -3 | -2 | -1 | <-- negative index
+----+----+----+----+
```

```{.python .example}
x = ['a', 'b', 'c', 'd']
print(x[-1]) # last element
print(x[-2]) # second last element
```

We could use this to find the last element of a sentence.


```{.python .example}
def get_last_word(sentence):
    return sentence.split()[-1]

w = get_last_word("one two three")
print(w)
```

### List Slicing

List slicing allows us to create a slice or part of a list very eaily.


```{.python .example}
x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

print("x ->", x)

# from index 0 unto index 2 (end is not included)
print("x[0:2] ->", x[0:2])

# upto index 2
print("x[:2] ->", x[:2])

# from index 1 upto 6
print("x[1:6] ->", x[1:6])

# from index 2 onwards
print("x[2:] ->", x[2:])

# every alternative element, from index 0 to 6th in steps of 2
print("x[:6:2]", x[:6:2])`

# from index 1 upto 6, take every 2nd element
print("x[1:6:2]", x[1:6:2])

# all except the last element
print("x[:-1]", x[:-1])

# How to get the last two elements?
print("x[:-2]", x[:-2])

# copy of x
print("x[:]", x[:])

# how to get the list in reverse order?
print(x[::-1], x[::-1])
```

#### Sorting Lists

Python makes it very easy to sort lists.

The `sort` method on lists, sorts the list in-place.

```{.python .example}
names = ["alice", "dave", "charlie", "bob"]
names.sort() # sorts in-place
print(names)
```

The built-in function `sorted`, returns a new sorted list.

```{.python .example}
names = ["alice", "dave", "charlie", "bob"]

names2 = sorted(names)
print(names2)

# The name would remain unchanged
print(names)
```

Just like how we used the `key` argument for `min` and `max` we could use that with the `sorted` function or the `sort` method.

The following example, sorts the names by their length.

```{.python .example}
names = ["alice", "dave", "charlie", "bob"]
names2 = sorted(names, key=len)
print(names2)
```

We can pass optional argument `reverse=True` to sort it in the reverse order.

```{.python .example}
names = ["alice", "dave", "charlie", "bob"]
names2 = sorted(names, reverse=True)
print(names2)
```
