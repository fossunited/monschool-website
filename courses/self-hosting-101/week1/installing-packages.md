---
title: Installing Software Packages
include_in_preview: false
---

In Linux, different distributions have different ways of managing software packages. These packages consists of Audio/Video drivers, kernel, system softwares, and user level software like media/games/editors/browsers etc. To manage these packages, we use something called as _Package Managers_. They are small utilties which help in downloading software from _Repositories_ and regularly update them.

Since this course is targetted for Ubuntu which is a `Debian` flavour distribution, it comes with Advanced Packaging Tool (APT) package manager. With `apt` you can add/remove packages or update existing ones and even upgrade your entire Ubuntu server.

Some examples to showcase:

## Update software repositories

The APT package index is database of all packages under each repository present inside `/etc/apt/sources.list`. Whenever any package update happens in any repository, we must update the index first before `apt` can pull the new package updates.

```
sudo apt-get update
```

After running the above command, we can now run `apt-get upgrade` which will upgrade all the older packages in your system to their latest versions. It's a good practice to keep your servers updated as they contain security patches as well.

```
sudo apt-get upgrade
```

## Installing packages

Now that we learnt how to update our server, it's time to install a software package from the Ubuntu repository.

Let's install `jq`. `jq` is a CLI which is used to parse JSON. It's quite a handy utility as you can use it with combination with other utilities and parse/extract specific data from a JSON output.

```
sudo apt-get install jq
```

We can verify that it's installed with:

```
jq --help
```
