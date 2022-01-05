---
title: Adding Images
include_in_preview: false
---

# Images

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/yI-y8BJ-61c" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## How to add images
Images are very easy to include in the the document using `img` tag. `img` tag just needs to know where the image is.

```html
<img src="path of the image" />
```

image tag doesn't need a seaparate closing tag. You can use the `/` in the opening tag to close it. 

`src` atrribute here needs to be supplied with the path. It can relative or absolute. For example if the image is in the same folder as HTML then just the file name of the image should be enough.


```html
<img src="my_first_image.jpg" />
```


```html
<img src="https://upload.wikimedia.org/wikipedia/en/thumb/4/41/Flag_of_India.svg/320px-Flag_of_India.svg.png" />
```

## How to customize

You can resize the image by using the attributes like `width` and `height`. You can use various measurements like 

- `px` for pixes
- `%` for percentage etc

You dont have to give both `width` and `height`. You can give only one and the browser will adjust the other one.

You can give `alt` text for the image. It's used by the screen readers to readout.


## What more
- You can add image inside an HTML link so you can make image as clickable. How to do that? Remember tags can be nested.

- How to embed an .mp3 audio inside an html document? Try and explore `audio` tag.

