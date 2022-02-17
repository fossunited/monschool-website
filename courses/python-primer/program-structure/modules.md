---
title: Modules
include_in_preview: false
---

Python comes with many built-in modules.

A module is imported using the `import` statement.

The following example imports the time module and prints the current time using the `asctime` function defined in that module.

```{.python .example}
import time
print(time.asctime())
```

## The `os` module

The `os` module provides functions related to files and processes.

The following example prints the current working directory.

```{.python .example}
import os
print(os.getcwd())
```

The `listdir` funtion lists all the files in a given directory.

```{.python .example}
import os

print(os.listdir("."))
```
