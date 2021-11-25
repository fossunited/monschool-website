---
title: Adding Examples
include_in_preview: false
---

Most courses on Mon School are very interactive and include many live examples. The platform supports adding live examples in many programming languages.

To add an example, use the following format and replace the `<lang>` with the name of the programming language.

    ```{.<lang> .example}
    code comes here
    ```

The following sections show how to add examples in various programming languages.

## Python

The following in the syntax for adding a Python example.

    ```{.python .example}
    print("hello, world!")
    ```

And the it be rendered as the following:

```{.python .example}
print("hello, world!")
```

## Rust

The following in the syntax for adding a Rust example.

    ```{.rust .example}
    fn main() {
        println!("Hello World!");
    }
    ```

And the it be rendered as the following:

```{.rust .example}
fn main() {
    println!("Hello World!");
}
```

## Go

The following in the syntax for adding a Go example.

    ```{.golang .example}
    package main

    import "fmt"

    func main() {
        fmt.Println("hello world")
    }
    ```

And the it be rendered as the following:

```{.golang .example}
package main

import "fmt"

func main() {
    fmt.Println("hello world")
}
```

## Supporting a new programming language

If the programming language that you are using for your course is not supported for live examples, please create an issue in [fossunited/falcon](https://github.com/fossunited/falcon/issues) repository and mention the course issue in `monschool_website` repo. It would be something like `fossunited/monschool#29`.


