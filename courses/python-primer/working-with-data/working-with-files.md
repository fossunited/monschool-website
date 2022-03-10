---
title: Working with Files
include_in_preview: false
---

It is very easy to read and write files in Python.

```{.python .example}
f = open("three.txt")
contents = f.read() # 'one\ntwo\nthree\n'
print(contents)
```

The built-in function `open` opens a file in read mode and returns a file object. We can call the `read` method on the file object to read all the contents of the file. We could simplify the above by combing the first two lines.

```{.python .example}
contents = open("three.txt").read() # 'one\ntwo\nthree\n'
print(contents)
```

The other common way to read a file is by reading lines.

```{.python .example}
lines = open("three.txt").readlines()
print(lines) # ['one\n', 'two\n', 'three\n']
```

We could also loop over the lines and print each line separately.

```{.python .example}
for line in open("three.txt").readlines():
    print(line)
```

Did you notice the exta empty lines after each line in the file? It is because there is a new-line character in each line and `print` is adding one more. We need stop one of these.

One approach is to ask the print to not add a new line.

```{.python .example}
for line in open("three.txt").readlines():
    print(line, end="") # ask print to not add a new line
```

And the another way is to remove the newline character from each line before printing.

```{.python .example}
for line in open("three.txt").readlines():
    print(line.strip("\n")) # remove the newline char from each line
```

When we want to iterate over the lines, we could just iterate over the file object without the need of `.readlines()`. This is possible because iterating over a file, goes over the lines any way.

```{.python .example}
for line in open("three.txt"):
    print(line, end="")
```

#### Example: word count

Unix has a word count program, wc.

We are going to use a file `numbers.txt` containing the following contents.

```
1 one
2 two
3 three
4 four
5 five
```

If we pass this file as an argument to the unix command `wc`, it would produce the following output.

```
$ wc numbers.txt
    5      10      34 numbers.txt
```

What does it take to implement this in Python?

<span id="livecode-options-wordcount"
    data-args="numbers.txt"
    data-source-file="wc.py"></span>


```{#wordcount .python .example .multi-file .show-args}
=== wc.py
"""Implements the wc command of unix.

Prints the line count, wordcount, char count and the filename.

USAGE:
    python wc.py filename
"""
import sys

def linecount(f):
    return len(open(f).readlines())

def wordcount(f):
    return len(open(f).read().split())

def charcount(f):
    return len(open(f).read())

def main():
    f = sys.argv[1]
    print(linecount(f), wordcount(f), charcount(f), f)

if __name__ == "__main__":
    main()
```

If we run this with numbers.txt as argument, we'll get this:

```
$ python wc.py numbers.txt
5 10 34 numbers.txt
```



**Problem:** Write a program `reverse_lines.py` that prints the lines in a file in the reverse order. The last line will be printed at the beginning etc.

```
$ python reverse-lines.py number.txt
5 five
4 four
3 three
2 two
1 one
```

**Problem:** Write a program reverse-words.py that prints words in each line in reverse order.

```
$ python reverse-words.py numbers.txt
one 1
two 2
three 3
four 4
five 5

$ python reverse-words.py words.txt
five
four five
three four five
two three four five
one two three four five
zero
```

#### Working with binary files

When we open a file in read mode, it tries to encode the bytes in the file using the spevcified encoding, which is `utf-8` in most cases. However, there will be cases where we need to deal with the bytes directly rather than converting to text. Reading binary files like images etc. is one such use case.

We can specify the mode as `rb` to open a file in read-binary mode. When a file is opened in binary mode, the `read` and the `readlines` functions returns bytes instead of string.

For example, reading the `numbers.txt` in read-binary mode gives the contents as bytes.

```{.python .example}
data = open("numbers.txt", 'rb').read() # gives bytes
print(data)
```

Compare that with reading it in read-text mode, which gives a string.

```{.python .example}
text = open("numbers.txt", 'r').read() # gives str
print(text)
```


## Writing Files

Files can be opened in write mode by specifying `"w"` or `"wt"` as mode. For writing binary files, it will be `"wb"`.

```{.python .example}
# write two lines into a.txt
f = open("a.txt", "w")
f.write("one\n")
f.write("two\n")
f.close()

# and read them back
contents = open("a.txt").read()
print(contents)
```

Whenever we open a file in a write mode, all the contents will be overwritten.

It is important to remember to close the file as the contents may not written to the disk until closed.

Sometimes we want to append something at the end of a file. In that case, we can open the file in append mode (`"a"`).


```{.python .example}
# write two lines to a.txt
f = open("a.txt", "w")
f.write("one\n")
f.write("two\n")
f.close()

# append two more lines to the same file
f = open("a.txt", "a")
f.write("three\n")
f.write("four\n")
f.close()

# and read them back
contents = open("a.txt").read()
print(contents)
```

### The `with` statement

The `with` statement is handy when writing to files as it takes care of closing the file automatically.


```{.python .example}
with open("a.txt", "w") as f:
    f.write("one\n")
    f.write("two\n")
# the file f gets closes automatically

# and read them back
contents = open("a.txt").read()
print(contents)
```

**Problem:** write a program `copyfile.py` to copy contents of one file to another. The program should accept a source file and a destination file as arguments and copy the source to the destination.

```
$ python copyfile.py a.txt b.txt
```

Note: Don't call this file `copy.py` as that interfere with a standard library module with the same name.