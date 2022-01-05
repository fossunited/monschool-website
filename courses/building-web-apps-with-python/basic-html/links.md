---
title: Adding Links
include_in_preview: false
---


<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/f_1XSC8OHug" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Anchor tag

The biggest feature of web is links. You can link various documents on the web using the an 'anchor tag'


```html
<a href="https://en.wikipedia.org/wiki/India"> Wikipedia India Page</a>
```

Here
- https://en.wikipedia.org/wiki/India -> is the link
- Wikipedia India Page is the text

- You can link to all kinds of documents, it doesn't have to be an HTML document.
- Links can also be relative url


## How to add download links

```html
<a href="https://www.gutenberg.org/ebooks/4908.epub"> Five of Maxwell's Papers by James Clerk Maxwell </a>

```
Here as you can see it's linked to an epub and not an HTML document. In this case. the browser may not know how to handle the file. It will prompt you to download.

You can also add `download` attribute to force the browser to download.

```html
<a href="my_first.html" download>Download this</a>
```

## How to customize links

- The content of the anchor tag doesn't have to be text. It can contain other tags
- For example you can make the text strong or add images etc

```html
<a href="my_first.html" download><strong>Download this</strong></a>
```

Sometimes you don't want the linked page to open in the same window. You want to open in a different window. Then you can use `target` attibute.

```html
<a href="my_first.html" target="_blank"><strong>My first</strong></a>
```
It can be 

- _blank  Open in a new window or tab
- _self   Open in the same frame
- _parent Open in the parent frame
- _top    Open in the full window
- or you can use frame name.

