---
title: Setup a site using git
include_in_preview: false
---

So far we've covered how to create our own site on the server and make it accessible. However in most real world cases, you'll want to _fetch_ the website from an external source and set it on your server. The most common usecases are personal websites/blogs etc where you store the content in a `git` repo and _build_ the website using a _Static Site Generator_.

Let's clone a sample website from Monschool repo and set it up as `red.<user>.monschool.net`.

```
git clone <> ~/red.<user>.monschool.net
```

We are now going to introduce the concept of `symlink`. A symlink is a _redirect_ for a file. For example, consider we have a file `~/test.txt`.

```
touch ~/test.txt
```

To make it available at a different place, say `~/new.txt`, we can _symlink_ `test.txt`. The advantage here over copying the file as `new.txt` is that the underlying file exists only in one place (`~/test.txt`) but a new copy of it also exists in ~/new.txt. So whenever we have to change the original file, we just need to do it in one place.

```
ln -s ~/test.txt ~/new.txt
```

Using `ln -s` we can create the symlink. We can verify the symlink exists using `ls -l`:

```
$ ls -l  new.txt
lrwxrwxrwx 1 karan karan 20 Dec 22 12:39 new.txt -> /home/karan/test.txt
```

Now that we understand how symlink works, you must be wondering why we introduced this in this chapter. Well, that is because whenever we pull our website using `git pull` and get the latest changes, we don't really want to copy our changes inside `/var/www` directory where we expect the site assets. (It is possible to change the root directory to where your site is, it's just a general good practice to keep it under `/var/www` so that if you have a lot of different sites on the system, you can all see it under one folder).

So, to achieve the above goal, we need to symlink `~/red.<user>.monschool.net to /var/www/`. Let's do that:

```
sudo ln -s ~/red.<user>.monschool.net to /var/www/
```

Now, using the knowledge from previous lesson where we created a `blue.conf`, let's create a `red.conf` as well:

TODO: Same config, paste here.

## Project: Setup a blog using Hugo

Now that you understand how sites are setup, cloned etc, it's time that you setup your own website using a static site generator. For this course, we will use `hugo`. Hugo is a popular static site generator written in Golang. It's a single binary program that can be downloaded and used to create websites using Markdown content. For this exercise, your task is to install Hugo, build a basic website and host it via NGINX.

You can refer to following links:

- https://gohugo.io/getting-started/installing/
- https://gohugo.io/getting-started/quick-start/
