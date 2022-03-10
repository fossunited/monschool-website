---
title: Introduction to Classes
include_in_preview: false
---

In this lesson we'll learn about classes and creating objects.

Object-oriented programming is a programming technique that organizes the code as classes and objects.

An object contains some data and some behavior, defined by the methods on that object.  Let's look at an example.

```{.python .example}
filename = "hello.py"
extension = filename.split(".")[1]
print(extension)
```

In the above example, the value of variable `filename` is a string, in other words, it is an object of built-in class `str`.

The `split` is a method defined in the `str` class and all the objects of that type can call it.

## The `class` statement

The class statement is used to define our own classes.

```{.python .example}
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 4)
print(p.x, p.y)
```

Calling `Point(3, 4)` creates a new instance of Point. Behind the scences, it does the following steps:

* creates an empty object of class `Point`
* initializes it by calling the `__init__` method
* returns the initialized object

## Attributes and Methods

If you look at the object `p`, it has two attributes `x` and `y`. They are accessed as `p.x` and `p.y`. It also has a method `__init__`, which is used to create a new instances of the class.

Let's add a new method `move` to the `Point` class.


```{.python .example}
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        """Moves the point by dx in the x-direction and
        dy in the y-direction.
        """
        self.x += dx
        self.y += dy

p = Point(3, 4)
print(p.x, p.y)

p.move(10, 20) # call the move method on Point p
print(p.x, p.y)
```

When we call a method on an object, the object is passed as the first argument. That is why we see the first argument in methods as `self`. It could called with any name, but it is called `self` by convention.



