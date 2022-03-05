---
title: Reading mypy error messages
include_in_preview: false
---

By this point you've probably used mypy a fair bit, maybe even outside of the
course. And you've probably seen a bunch of these by now:

```console
mycode.py:2: error: No return value expected
mycode.py:5: error: Incompatible types in assignment (expression has type "str", variable has type "int")
mycode.py:7: error: Function is missing a return type annotation
```

And with the practice, you should already be able to tell exactly what each of
these errors mean, maybe even predict what the code looks like.

Here's the actual code:

```{.python .example .mypy-strict}
def foo() -> None:
    return 42

bar = 10
bar = 'baz'

def quux():
    return {'x'}
```

- The first error shows up when you try to return data from a function that is
  marked to not return anything (`-> None`).
- The second error should be an `int` variable being assigned a string.
- The third error is a function without a proper type signature.

As you get more and more familiar with mypy errors, you'll start realizing that
most of them boil down to just two things:

- Your code has a type mismatch, eg. mypy expected object of one type but found
  object of a different type.
- Mypy is unable to figure out the types in your code, and needs you to add more
  type information, eg. in a function defintion.

Let's see a couple more examples to explain this in detail:

```{.python .example .mypy-strict}
def print_spendings(purchases: list) -> None:
    total_spendings = 0
    for item, value in purchases:
        print(f"Bought {item} for {value} dollars")
        total_spendings += value

    print("Total spent:", total_spending)

purchases = [
  ("Eggs", 10),
  ("Cheese", 25),
  ("Bacon", 15),
]
print_spendings(purchases)
```

The second error is easy to understand and fix: We made a typo in the variable
name. The first one though, is telling us that mypy needs more information about
a function parameter, `purchases` in this case. By "type parameters" it means
the part inside the `[]` brackets.

We can see that it's a list of 2-tuples, but how would you write that as a type
hint? I could tell you, but you can also use `reveal_type` to figure it out
yourself:

```{.python .example .mypy-strict}
purchases = [
  ("Eggs", 10),
  ("Cheese", 25),
  ("Bacon", 15),
]
reveal_type(purchases)
```

So the type is supposed to be `list[tuple[str, int]]`. That's how `tuple` typing
works, by the way. Since tuples are essentially a way to represent a collection
of data points related to an entity. While other collections usually represent a
bunch of items, tuples usually represent a single item.

A good example is sqlite:

```python
>>> for row in cursor.execute('SELECT name, age, bio FROM users'):
...     print(row)
('Joe', 23, 'Hello!')
('Mike', 27, 'Web developer from California.')
>>>
```

For this reason, tuples take a type parameter for every index inside the tuple.
The type of the above tuples would be `tuple[str, int, str]`.

In case you want to make a tuple that contains data like a list, a tuple of many
strings for example, you can use the `...` syntax, like this:

`items: tuple[str, ...] = ("eggs", "cheese", "bacon")`

---

Anyway, you can fix the function signature like so:

`def print_spendings(purchases: list[tuple[str, int]]) -> None:`

Once you do that, mypy should report no errors.

Let's see another example:

```{.python .example .mypy-strict}
def unique_count(nums: list[int]) -> int:
    """counts the number of unique items in the list"""
    uniques = set()
    for num in nums:
        uniques.append(num)

    return uniques

counts = unique_count([1, 2, 1, 3, 1, 2, 4, 3, 1])
print(counts)
```

The first error says we need a better type annotation for `uniques`. Since we're
making an empty set, mypy doesn't know what it should contain. Add `: set[int]`
to fix that.

The second error says `set` doesn't have an `append` method -- and it's right.
Sets don't have `.append()`, they use `.add()` to add items. So let's fix that
method call as well.

The third error says we're returning a set, when we're supposed to return an
integer. The code was supposed to `return len(uniques)` instead.

With those fixed, the code should run and mypy should be happy.
