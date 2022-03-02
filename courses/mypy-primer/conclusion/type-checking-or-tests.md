---
title: Type checking, or writing tests? Why not both!
include_in_preview: false
---

People like to argue that:

- If I've been writing python for so long without types, why should I care now?
  or, I don't need types because I write tests.
- Conversely, people can think they don't need tests because mypy catches all of
  their bugs for them.

Why types:
It's very easy to write tests that forget to check all type errors

```{.python .example}
def process(self, items):
    for item in items:
        print("Processing", item.value.id)
```

You can very easily forget to write a test where `value` is `None`. Type
annotations eliminate a whole class of bugs: type errors.

Why tests?
Because tests are important for checking your logic. Logical errors can't be
possibly tested through type checking.

They work in unison: Type checking ensure that most completely invalid inputs
are removed, such as passing a string instead of int. Tests prevent more fine
grained bugs, that can come from logical errors and the like.

