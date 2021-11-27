---
title: Adding Course Preview Image
include_in_preview: false
---

Every course on mon school has a preview image displaying in the course listing page and the course  page.

## Preparing the image

The Mon School platform requires the image to be of a specific size. A utility has been provided to make it easier to convert the image that you have into an image that is suitable for mon school.

```
$ python manage.py prepare-image source-image courses/my-course/preview-image.png
created courses/my-course/preview-image.png
```

## Specifying the Image in course.yml

Once you're prepared the image, you can specify the image in the `course.yml` file.

```
name: my-course
title: My course
...
preview_image: preview-image.png
...
```

The path to the image relative to the course directory is specified as field `preview_image`. It is recommended to name the image file `preview-image.png`.
