---
title: Dictionaries
include_in_preview: false
---

Dictionary is a data structure to store name-value pairs in Python. They are very versatile and provide fast access to access the elements.


```{.python .example}
d = {"x": 1, "y": 2, "z": 3}
print(d)
print(d["x"])
d["x"] = 11
print(d)
```

From Python 3.7 onwards, dictionaries maintain their insertion order, before that dictionaries were unordered.

## Using dictionaries

The dictionaries are typically used in two different ways.

1. as a record
2. as a database/lookup-table


```{.python .example}
# as a record
person = {
    "name": "Alice",
    "email": "alice@example.com",
    "phone": 1234
}
```

when using dictionary as a record, we know all the possible keys.

```{.python .example}
# as a lookup-table
phone_numbers = {
    "alice": 1234,
    "bob": 2345
}

name = "alice"
phone = phone_numbers[name]
print(name, phone)
```

when using dictionary as a lookup table, the keys are not known upfront.

## Common Operations on Dictionries

Elements of a dictionary can be accessed and modifiefd using the `[]` operator.

```{.python .example}
d = {"x": 1, "y": 2}
print(d["x"])

d["x"] = 11
print(d)
print(d["x"])
```

The `in` operator is used to check if an element is present in a dictionary.

```{.python .example}
d = {"x": 1, "y": 2}

print("x" in d)
print("z" in d)
print("z" not in d)
```

**`get`**

The `get` method is handy to access the value of a key in a dictionary when we are not sure if the key is present in the dictionary.

If the key is present in the dictioany, it gives the corresponding value, if not it returns the second argument.

```{.python .example}
phone_numbers = {
    "alice": 1234,
    "bob": 2345
}

n = phone_numbers.get("alice", "-")
print(n)

n = phone_numbers.get("dave", "-")
print(n)

print(phone_numbers)
```

**`setdefault`**

The `setdefault` method works like `get`, but also adds an entry when the key is missing.

```{.python .example}
phone_numbers = {
    "alice": 1234,
    "bob": 2345
}

n = phone_numbers.setdefault("alice", "-")
print(n)

n = phone_numbers.setdefault("dave", "-")
print(n)

print(phone_numbers)
```

**`update`**

The `update` method is used to add entries of one dictionary to another.

```{.python .example}
d1 = {"x": 1, "y": 2}
d2 = {"x": 11, "z": 33}

d1.update(d2)
print(d1)
```

## Iterating over dictionaries

Dictionaries supports three methods `keys`, `values` and `items` to access the keys, vaues and key-value pairs of the dictionary respectively.

```{.python .example}
d = {"x": 1, "y": 2, "z": 3}

print(d.keys())
print(d.values())
print(d.items())
```

### Iterating over the keys

```{.python .example}
d = {"x": 1, "y": 2, "z": 3}

for k in d.keys():
    print(k)
```

Iterating over a dictionary, goes over it's keys.

```{.python .example}
d = {"x": 1, "y": 2, "z": 3}

for k in d:
    print(k)
```

We can also access the value using the `[]` operator when iterating over the keys.

```{.python .example}
d = {"x": 1, "y": 2, "z": 3}

for k in d:
    print(k, d[k])
```

### Iterating over the values

```{.python .example}
d = {"x": 1, "y": 2, "z": 3}

for v in d.values():
    print(v)
```

Please note that when iterating over the values, we can not get the corresponding keys.

### Iterate over the key-value pairs

We can also iterate over the key-value pairs using the `items` method.

```{.python .example}
d = {"x": 1, "y": 2, "z": 3}

for k, v in d.items():
    print(k, v)
```

### Example: Marks of a student

Let's see how to store marks of a student in different subject be stored in a dictionary and use that to generate a report card.

```{.python .example}
marks = {
    "english": 89,
    "maths": 87,
    "science": 45
}

print(marks)
```

To generate a report, we need to print the subject and marks for each subject.

```{.python .example}
marks = {
    "english": 89,
    "maths": 87,
    "science": 45
}

for subject, score in marks.items():
    print(subject, score)
```

It would be nice to include the total marks at the end of the report.

```{.python .example}
marks = {
    "English": 89,
    "Maths": 87,
    "Science": 45
}

for subject, score in marks.items():
    print(subject, score)

total = sum(marks.values())
print("---")
print("Total", total)
```

### Example: Word Frequency

Write a program to compute the frequency of words in a file.

Suppose we have a file `words.txt` with the following contents:

```
zero
five
five four
five four three
five four three two
five four three two one
ten zero
```

If you notice, the word `zero` is occuring 2 times, `five` 5 times etc.

```{.python .example}
"""Program to compute frequency of words in the given file.

USAGE: python wordfreq.py words.txt
"""
import sys

def read_words(filename):
    """Reads and returns all words in the given filename as a list.
    """
    return open(filename).read().split()

def wordfreq(words):
    """Takes a list of words as argument and computes
    frquency of each unique word in those words as a dictionary.

        >>> wordfreq([])
        {}
        >>> wordfreq(['a', 'b', a'])
        {"a": 2, "b": 1}
    """
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq

def print_freq(freq):
    """Prints frequency of words in a nice readable format.
    """
    for w, count in freq.items():
        print(w, count)

def main():
    filename = sys.argv[1]
    words = read_words(filename)
    freq = wordfreq(words)
    print_freq(freq)

if __name__ == "__main__":
    main()
```


