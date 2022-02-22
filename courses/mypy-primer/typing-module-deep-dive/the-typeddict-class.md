---
title: The TypedDict class
include_in_preview: false
---

When getting data from an API for example, it's fairly common to have data in a
dictionary, like so:

```python
user = {
    'name': 'Mike',
    'age': 21,
}
```

The thing with such data is that it's usually well structured with string keys,
but the values are of various different types. Often you can define a schema for
the data type, i.e. you know that the dictionary will have a string `"name"`,
and an integer `"age"`. But with normal dictionaries, it doesn't work that way:

```{.python .example}
user = {
    'name': 'Mike',
    'age': 21,
}
reveal_type(user['name'])
reveal_type(user['age'])
```

Just like the case with `['Mike', 21]`, mypy defaults to assuming you're just
making a `dict[str, object]`. And usually, that would be the right assumption.
But not in this specific case.

Maybe you can try to define a schema by making a dictionary with the types? If
you try to do that you'll get weird errors, about `Type[int]` and `Type[str]`:

```{.python .example}
user = {
    'name': str,
    'age': int
}
d['name'] = 'Mike'
d['age'] = 31
```

Mypy knows about this usecase, and it has a feature that allows making such dict
types. The solution is to use `TypedDict` to define a `User` type first, and to
tell mypy that we want the `user` dictionary to adhere to that shape:

```{.python .example}
from typing import TypedDict

User = TypedDict('User', {
  'name': str,
  'age': int
})

user: User = {
    'name': 'Mike',
    'age': 21,
}

reveal_type(user['name'])
reveal_type(user['age'])
```

Another option is to use the same syntax as `NamedTuple`. But unlike NamedTuple,
you don't need to instantiate the `User` class, a regular dictionary also works.

```{.python .example}
from typing import TypedDict

class User(TypedDict):
    name: str
    age: int

user: User = {
    'name': 'Mike',
    'age': 21,
}

reveal_type(user['name'])
reveal_type(user['age'])
```

You can even define deeply nested data in this way:

```{.python .example}
from typing import TypedDict

class UserDetails(TypedDict):
    name: str
    age: int

class User(TypedDict):
    userid: int
    username: str
    details: UserDetails

def get_user() -> User:
    return {
        "username": "miketyson",
        "userid": 123456,
        "details": {
            "name": "Mike Tyson",
            "age": 21,
        },
    }
```

We can use TypedDicts inside TypedDicts to make this work.
