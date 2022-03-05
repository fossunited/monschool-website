---
title: Typing *args and **kwargs
include_in_preview: false
---

`*args` and `**kwargs` is a feature of python that lets you pass any number of
arguments and keyword arguments to a function (that's what the name `args` and
`kwargs` stands for, but these names are just convention, you can name the
variables anything).

All the extra arguments passed to `*args` get turned into a tuple, and kewyord
arguments turn into a dictionay, with the keys being the string keywords:

```{.python .example .mypy-strict}
def i_can_take_any_values(first_arg, *args, **kwargs):
    print('got extra args:', args)
    print('got kwargs:', kwargs)

i_can_take_any_values(1, 16, 'Hello', x=False, answer=42)
```

Since the `*args` will always be of type `Tuple[X]`, and `**kwargs` will always
be of type `Dict[str, X]`, we only need to provide one type `X` to be able to
define their type. Here's a practical example, that takes keywords of marks in a
subject, and creates a `Scorecard`:

```{.python .example .mypy-strict}
class Scorecard:
    def __init__(
        self,
        english: int | None,
        maths: int | None,
        physics: int | None
    ) -> None:
        self.english = english
        self.maths = maths
        self.physics = physics

def build_scorecard(**marks: int) -> Scorecard:
    card = Scorecard(
        english=marks.get('english'),
        maths=marks.get('maths'),
        physics=marks.get('physics'),
    )
    return card

marks = {'english': 55, 'physics': 84}
scorecard = build_scorecard(**marks)
print(scorecard.physics)
print(scorecard.maths)
```

To verify, you can use `reveal_type`:

```{.python .example .mypy-strict}
def build_scorecard(**marks: int) -> None:
    reveal_type(marks)
```

`marks` is indeed `dict[str, int]`.
