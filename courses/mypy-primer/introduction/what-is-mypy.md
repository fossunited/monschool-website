---
title: What is mypy?
include_in_preview: false
---

Welcome to Mypy Primer! The course will teach you everything you need to know
about static type checking in Python, using a library called `mypy`.

By the end of this chapter, you are going to understand what static typing is,
how it works in Python, and why you should care about it.

## So what's static typing then?

You might know that Python is a _dynamically typed_ programming language. Or in
other words, Python's variables have dynamic types, not static types.

What that means is that variables in Python don’t have a specific data type
associated with them. Which means you can do things like this:

```{.mypy .example}
variable = "A string"
variable = 123
variable = ["spam", "eggs", 1000]
```

The variable started out as a string type in the first line. But then it was
re-assigned to an integer type and, finally, it was assigned a list in the third
line. Notice that the list doesn’t have fixed data types either, in our case it
contains both strings and integers.

In essence, Python defines the type of the data with the value itself, not with
the variable that is storing it. You can ask Python at runtime what the type of
a variable is, like so:

```{.mypy .example}
variable = "A string"
print(type(variable)) # Prints `<class 'str'>`
variable = 123
print(type(variable)) # Prints `<class 'int'>`
variable = ["spam", "eggs", 1000]
print(type(variable)) # Prints `<class 'list'>`
```

If you’ve previously worked with Java, C++, or any other statically typed
programming language, this behavior might seem a bit odd.

Let’s see the same piece of code in TypeScript, a similar but statically typed
language, just to see what happens. The code would look something like this:

```{.typescript .example}
let variable = "abc"
variable = "def"
variable = 42
variable = ["spam", "eggs", 1000]
```

And this code immediately errors out when TypeScript tries to compile it:

[TODO: add image #1]

This is because TypeScript believes that variable is of the string type, and it
won’t let you assign something to it that isn’t a string. So when we tried to
assign a number to it on line 3, it throws a compiler error.

[TODO: add image #2]

This is the fundamental difference between static and dynamic typing: in a
statically typed language, the type of variables is fixed, and defined even
before the program is run. On the other hand, in a dynamically typed language,
the type of a variable can change at any time.

## Why does it matter?

In statically typed languages, it is their compiler that does the type checking
for you. For a lot of compiled languages, having valid data types is necessary
for the compiler to be able to convert the program into valid, optimized machine
code. Knowing the proper types of variables is what lets the compiler know
various things, such as how much space to allocate for that variable when it
runs, for example.

But even putting that aside, there’s a really big benefit to having predefined
types for your variables: It essentially helps cross-verify your code against
various errors. Let’s look at an example.

Let’s say you’re writing software that will be used by teachers in a school. One
feature that the teachers want is to be able to search through all the students’
names in a class.

Since there are various sections in each class and each student belongs to one
section, you decide that a list of sections, each containing a list of students,
would be ideal to store your information. Like so:

```{.mypy .example}
sections = [
    ['Aron', 'Belle', 'Kyle'],
    ['Alice', 'Mike', 'Scott', 'Stacy']
]
```

There are seven students in total in this case: three in one section, and four
in the other. Now, you go ahead and implement the search function to search for
a student’s name in the class:

```{.mypy .example}
def search_student(sections, search_name):
    for section in sections:
      for student in section:
          if student == search_name:
              return "Student found!"

    return "No student found with this name."
```

You try to run this, and it works!

```{.mypy .example}
>>> search_student(sections, "Mike")
>>> 'Student found!'
>>> search_student(sections, "Steve")
>>> 'No student found with this name.'
```

A few days later, you try to run the same code somewhere else, and for some
reason it has stopped working correctly. You try to run the code with the same
options as before, and it still doesn’t run! What happened?

```{.mypy .example}
>>> search_student(sections, "Mike")
>>> 'No student found with this name.'
>>> search_student(sections, "Steve")
>>> 'No student found with this name.'
```

You look up the code implementation, and here’s what you find:

```{.mypy .example}
sections = {
    'Section A': ['Aron', 'Belle', 'Kyle'],
    'Section B': ['Alice', 'Mike', 'Scott', 'Stacy']
}
```

You remembered that you had updated sections to be a dictionary, because you
needed to add section names to the sections, for another feature.

But this is the weirdest part: **the code didn’t error out**. Instead of letting you
know that wherever you had written code that assumed sections to be a list is
now essentially invalid code, _it just silently kept working_.

If you’re unsure what happened and why it didn’t throw an error: the key thing
to notice is that dictionaries in Python are iterable, and when you try to
iterate over them, you get back the dictionary keys in the for-loop:

```{.mypy .example}
sections = {
    'Section A': ['Aron', 'Belle', 'Kyle'],
    'Section B': ['Alice', 'Mike', 'Scott', 'Stacy']
}
```

```{.mypy .example}
def search_student(sections, search_name):
    for section in sections: # section: 'Section A', ‘Section B’
        for student in section: # student: 'S', ‘e’, ...
            if student == search_name:
                return "Student found!"
    ...
```

So, section ended up being strings from the keys of the dictionary, and student
ended up being single characters. Basically, the code was doing nonsense work.
All without crashing, or giving any indication that something might have gone
wrong.

In comparison, if Python had a type checker which knew that sections expects a
list or a dictionary as the input, such a mistake would never occur. Even if you
were to mess up the type of data passed, the type checker would immediately let
you know.

Such type-related errors are some of the most common programming errors that
happen in all dynamically typed languages. Type checking lets you find and fix
them, saving your precious time and preventing bad crashes.

## Introducing mypy

`mypy` is a type checking library for Python.

Python has a really good ecosystem of type hinting and type checking tools that
allows you to get all the benefits of static type checking, with all the
flexibility and features of Python. It's an ideal solution for programming needs
in my experience.

I hope you're excited to learn about it, now that you understand everything it
can do for you. So let's get straight into it, by learning how type annotations
work in Python.
