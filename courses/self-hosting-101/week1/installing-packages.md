---
title: Installing Software Packages
include_in_preview: false
---

In Linux, different distributions have different ways of managing software packages. These packages consists of Audio/Video drivers, kernel, system softwares, and user level software like media/games/editors/browsers etc. To manage these packages, we use something called as _Package Managers_. They are small utilties which help in downloading software from _Repositories_ and regularly update them.

Since this course is targetted for Ubuntu which is a `Debian` flavour distribution, it comes with Advanced Packaging Tool (APT) package manager. With `apt` you can add/remove packages or update existing ones and even upgrade your entire Ubuntu server.

Our task for this lesson is to install a tool called `fortune`. `fortune` is a very old, popular and entertaining utility. The tool does exactly what the name says - it prints random fortune cookies to the terminal.

## Step 1: Update software repositories

TODO: Reword directory path.

Before we install any package, we must ensure that our package respository is up-to date. The APT package index is database of all packages under each repository present inside `/etc/apt/sources.list`. When a package gets updated, we need to update our local index before we can install the latest package versions. To do that, run the following command:

```
sudo apt-get update
```

After running the above command our package list got update. Now, we can run `apt-get upgrade` which will upgrade all the older packages in your system to their latest versions. It's a good practice to keep your servers updated as they contain security patches as well.

```
sudo apt-get upgrade
```

## Step 2: Installing packages

Now that we learnt how to keep our package repositories updated and also install latest updates, it's time for us to install a `fortune` from the Ubuntu repository.

```
sudo apt-get install fortune-mod
```

We can verify that it's installed by running:

```bash
❯ fortune
Is this really happening?
```

# TODO: Mention `fortune` can print random string.

Congrats! You learnt how to update packages and even install one yourself. Here's an exercise for you:

Install the famous utility `cowsay` and print this message "I like learning new things". The output would look something similar to:

```bash
❯ cowsay I like learning new things
 ____________________________
< I like learning new things >
 ----------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```
