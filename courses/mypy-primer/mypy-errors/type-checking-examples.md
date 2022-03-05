---
title: Simple type checking examples
include_in_preview: false
---

The most that you'll be doing with mypy is tweaking your code, fixing potential
bugs, and changing your type annotations, to make mypy confident that your code
is good. Let's look at a couple more code examples and see what mypy says about
them.

## Colors?

Let's write something to find a user's favorite color:

```{.python .example .mypy-strict}
user_data = {
  'name': 'Mike Tyson',
  'color': 'red',
  'city': 'New York',
}

def get_favorite_color() -> str:
    favorite_color = user_data.get('color')
    return favorite_color

print("Tyson's favorite color is:", get_favorite_color())
```

The code runs fine, but mypy isn't happy yet. Why is that? The message is a bit
cryptic:

```console
mycode.py:9: error: Incompatible return value type (got "Optional[str]", expected "str")
```

Here's what mypy is saying: `user_data.get(...)` returns an `Optional[str]`, but
the function is supposed to return a `str`. What it's trying to say is: `.get()`
can possibly return `None`. (We'll explore `Optional` in detail later.)

Though `data` is defined with a `color` property in it, the code _could_ have
changed the dictionary's contents, and removed the `color` property from inside
it. Figuring out what value is and isn't inside a dictionary isn't possible
without actually running the code, so mypy doesn't assume anything.

Essentially, `mypy` is concerned that `user_data.get(...)` could return `None`,
which goes against your annotation of `-> str`.

To fix it, we can do multiple things, but for now, let's just assure mypy that
we're always going to have `color` in the dictionary.

For that, let's add a runtime assertion:

```{.python .example .mypy-strict}
user_data = {
  'name': 'Mike Tyson',
  'color': 'red',
  'city': 'New York',
}

def get_favorite_color() -> str:
    favorite_color = user_data.get('color')
    assert favorite_color is not None
    return favorite_color

print("Tyson's favorite color is:", get_favorite_color())
```

If `favorite_color` is ever `None`, Python will crash at runtime. So, mypy can
guarantee that the color is a `str`. Mypy is convinced, and your types are
perfectly valid.

> There is another similar way to solve this, by not using `.get()`. I'll leave
> that for you to figure out.

## An exercise

Try adding types to this code, and figure out if this code has any bugs:

```{.python .example .mypy-strict}
def average(a, b, c):
    return (a + b + c) / 3

english, science, math = 75, 87, 90
avg_score = average(english, science, math)

def print_scorecard(score):
    print(f"Average score is: {score}")

if avg_score.is_integer():
    print_scorecard(int(avg_score))
else:
    print_scorecard(avg_score)
```
