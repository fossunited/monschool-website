---
title: The NamedTuple class
include_in_preview: false
---

`namedtuple`s are a lot like tuples, except every index of their fields has a
name, and they have some syntactic sugar which allow you to access its
properties like attributes on an object:

```{.python .example .mypy-strict}
from collections import namedtuple

Person = namedtuple('Person', ('name', 'age', 'bio'))
ishan = Person('Ishan', 31, 'Writer')

print(ishan)
print(ishan[1])
print(ishan.bio)
```

Since the underlying data structure is a tuple, and there's no real way to
provide any type information to namedtuples, by default this will have a type of
`Tuple[Any, Any, Any]`.

To combat this, Python has added a `NamedTuple` class which you can extend to
have the typed equivalent of the same. Their syntax allows adding types:

```{.python .example .mypy-strict}
from typing import NamedTuple

class Person(NamedTuple):
    name: str
    age: int
    bio: str

ishan = Person('Ishan', 31, 'Writer')

reveal_type(ishan)
reveal_type(ishan[1])
reveal_type(ishan.bio)

name, age, _ = ishan
reveal_type(age)
```

Underneath the syntax, it's still a tuple. But this allows mypy to know the
types of each element and their names as well.
