---
title: HTML head and body
include_in_preview: false
---

# Basic  Structure

## HTML Document Basic Structure

Even though an HTML document works with just text and without any special tags. We do have  what we call a DOCTYPE. Which describes what kind of document this is. Since this an HTML document. We define that at the top. So that any software that handles this file knows that this is an actual HTML document

```{.html .example}
    <!DOCTYPE html>
```

- The we add `<html>` tag that encloses the whole document.
```{.html .example}
<!DOCTYPE html>
<html>
</html>
```

## Head and Body
- Now that we have defined the boundaries of our HTML document
- Lets divide that into 
    - head - Where we will add some metadata (data about this document) 
    - body - Where will add some content that we have
```{.html .example}
<!DOCTYPE html>
<html>
    <head>
    </head>
    <body>            
    </body>
</html>
```

## How to add title
- Let's give a title to the document
```{.html .example}
<!DOCTYPE html>
<html>
    <head>
        <title> My first HTML Document </title>
    </head>
    <body>            
    </body>
</html>
```
But the text is still jumbled. That is because we have not added any structure to the text

