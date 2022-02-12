---
title: Installing Software Packages
include_in_preview: false
---

In this lesson we'll learn about the package management system of Ubuntu. We'll learn how to keep packages updated and install new packages from the package manager.

### Refresher

We'll use some concepts here that was learned in the previous lesson. You can take a quick look at them to refresh them:

- `ssh user@ip` command to login from [Creating droplet lesson](./creating-droplet.md)

---

In Linux, different distributions have different ways of managing software packages. These packages consist of Audio/Video drivers, Linux Kernel, System-level packages, and user-level software like media/games/editors/browsers etc. To manage these packages, we use something called _Package Managers_. They are small utilities that help in downloading software from _Repositories_ and regularly update them.

In this course, we are using a Ubuntu-based droplet, which comes with an Advanced Packaging Tool (APT) package manager. With `apt` you can add/remove packages or update existing ones and even upgrade across Ubuntu versions.

Our task for this lesson is to install a tool called `fortune`. `fortune` is a very old, popular and entertaining utility. The tool does exactly what the name says - it prints random fortune cookies to the terminal.

## Step 1: Update software repositories

Before we install any package, we must ensure that our package repository is up-to-date. The APT package index is a database of all packages under each repository.

When a package gets updated, we need to update our local index before we can install the latest package versions. To do that, run the following command:

```bash
$ sudo apt-get update
```

After running the above command our package list got updated. However, our software packages haven't been _upgraded_, only the details of new versions present in the package index have been _updated_. We need to run `apt-get upgrade` which will upgrade all the older packages in our system to their latest versions as present in the package index.

## Step 2: Installing packages

Now that we learnt how to keep our package repositories updated, it's time for us to install the package `fortune-mod` from the Ubuntu repository.

**NOTE**: The name of the package is `fortune-mod` in the APT repository, however the actual name of the command is `fortune`.

```bash
$ sudo apt-get install fortune-mod
```

We can verify that it's installed by running the command `fortune`:

```bash
$ fortune
Is this happening?
```

**NOTE**: Since `fortune` prints a random message every time you run, it's completely normal for you to see an output different than above.

Congrats! You learnt how to update packages and even install one yourself. Here's an exercise for you:

---

## Task

Install the famous utility `cowsay` and print this message "I like learning new things". The output would look something similar to:

```
$ cowsay I like learning new things
 ____________________________
< I like learning new things >
 ----------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```
