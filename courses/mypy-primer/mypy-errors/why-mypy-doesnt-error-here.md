---
title: Why doesn't mypy show an error here?
include_in_preview: false
---

Now that we have picked up the basics, let's use mypy for some serious work, and
see how it can help us along the way.

Here's the code example that we'll be working with:

```{.mypy .example}
import json
from itertools import cycle

items_json = """
{
    "items": [
        "item 1", "item 2", "item 3", "item 4", "item 5",
        "item 6", "item 7", "item 8", "item 9", "item 10"
    ]
}
"""

def get_worker_count(): return 4

def run_processes() -> None:
    worker_count = get_worker_count()
    print("Running with " + worker_count + " workers")

    workers = range(worker_count)

    items = json.loads(items_json)
    for item, worker in zip(items, cycle(workers)):
        print(f"Processing {item} with worker {worker}")


if __name__ == "__main__":
    run_processes()
```

The code seems alright if you take a look at it. The list of `items` and workers
get zipped together to get one of them at a time, and `cycle(workers)` from
`itertools` ensures that when workers run out, they restart from the first one.

But if you try to run the code, it crashes immediately. There must be a bug. But
then, why doesn't `mypy` catch it? It says it found no issues. The first thing
in such cases would be to remember to run it in strict mode. Enabling that, it
tells us that we didn't add types to `get_worker_count`. So let's do that:

```python
# Update the code with this annotation
def get_worker_count() -> int: return 4
```

Now run `mypy` on it again, and we get:

```console
mycode.py:18: error: Unsupported operand types for + ("str" and "int")
Found 1 error in 1 file (checked 1 source file)
```

So it does catch the issue: we can't add `worker_count` (an integer) to strings.
Let's fix that. Make the following change on line 18:

```python
    # Replace `worker_count` with `str(worker_count)`
    print("Running with " + str(worker_count) + " workers")
```

And now mypy should say it found no issues.

But, if you try to run the code, you get the following output:

```console
Running with 4 workers
Processing items with worker 0
```

We were expecting 10 items to show up, but we only got one? Clearly we have some
other bug going on. And yet mypy is perfectly happy with the code. Why is that?

Before that, let's try to debug the code. Here's what the code should look like:

```{.mypy .example}
import json
from itertools import cycle

items_json = """
{
    "items": [
        "item 1", "item 2", "item 3", "item 4", "item 5",
        "item 6", "item 7", "item 8", "item 9", "item 10"
    ]
}
"""

def get_worker_count() -> int: return 4

def run_processes() -> None:
    worker_count = get_worker_count()
    print("Running with " + str(worker_count) + " workers")

    workers = range(worker_count)

    items = json.loads(items_json)
    for item, worker in zip(items, cycle(workers)):
        print(f"Running {item} with worker {worker}")


if __name__ == "__main__":
    run_processes()
```

Since the items don't seem right, let's try to print it out:

```python
    items = json.loads(items_json)
    # Add this line
    print("Items:", items)
    for item, worker in zip(items, cycle(workers)):
        ...
```

The output:

```console
Running with 4 workers
Items: {'items': ['item 1', 'item 2', 'item 3', 'item 4', 'item 5', 'item 6', 'item 7', 'item 8', 'item 9', 'item 10']}
Running items with worker 0
```

Well turns out, we had a _dictionary_ in `items`, not a list of the actual items
that we wanted.And since both lists and dictionaries can be iterated upon, the
code ran either way.

Unfortunately, logical errors cannot be caught with a type checker. You'll have
to ensure such cases yourself.

There are however, a few things we can do. Let's fix the code and add some
assertions for good measure:

```{.mypy .example}
import json
from itertools import cycle
from time import sleep

items_json = """
{
    "items": [
        "item 1", "item 2", "item 3", "item 4", "item 5",
        "item 6", "item 7", "item 8", "item 9", "item 10"
    ]
}
"""

def get_worker_count() -> int: return 4

def run_processes() -> None:
    worker_count = get_worker_count()
    print("Running with " + str(worker_count) + " workers")

    workers = range(worker_count)

    # Updated code:
    data = json.loads(items_json)
    items = data['items']
    # Add assertion to ensure that it is defintely a list
    assert isinstance(items, list)

    for item, worker in zip(items, cycle(workers)):
        print(f"Running {item} with worker {worker}")


if __name__ == "__main__":
    run_processes()
```

Now the code runs as we wanted. Mypy did help us find some errors, but things
like logical errors have to be fixed yourself, as usual.
