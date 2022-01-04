---
title: Working with files and directories
include_in_preview: false
---

## Lesson Objectives

- [ ] Editing files
- [ ] Understand Linux Directory Structure
- [ ] Learning basic CLIs to navigate filesystem

### Refresher

We'll use some concepts here that was learned in the previous lesson. You can take a quick look at them to refresh them:

- `ssh user@ip` command to login from [Creating droplet lesson](./creating-droplet.md)

One of the most fundamental tasks that we should know while dealing with Linux is to navigate the filesystem. Common use cases include editing a config file for web servers, modifying app config, editing system files to setup cron etc, viewing logs and checking for errors etc.

To learn how to navigate your way around the filesystem, there are a few commands that you should know about. However, instead of learning these commands all at once, let's think about a real-world scenario where you will need to make use of these commands.

We had used `fortune` in our previous lesson where we learnt how to use `fortune` to print a random fortune cookie on the terminal. Our task for this lesson would be to print a new fortune cookie every time you log in to the server. To achieve that, we will need to edit a config file (present at the location `~/.bashrc/`) and make some changes.

Before we begin editing `~/.bashrc` (don't worry, we'll get on to what `~` actually means), we should first know where we are. Our first command in our toolset is `pwd`:

## Editing Files
### `pwd`: _Print Working Directory_

This command simply tells which _directory_ you are currently in the filesystem.

```
$ pwd
/home/ubuntu
```

As shown in the above output, we are inside `/home/ubuntu` directory. This directory is also called as `HOME` directory. Shell-like `bash` expand the character `~` to the full `/home/ubuntu` path, so you can also use `~` as an alias if you don't want to type the full path of the `HOME` directory.

Each user gets their own `HOME` directory and if you want to find the `HOME` directory for a particular user programmatically, you can also read the environment variable `$HOME` which also points to `/home/ubuntu`.

Now we know that we are inside `/home/ubuntu`, and we need to edit `~/.bashrc` file, how do we do that? We'll need to use a **text editor** to open this file and modify it.
To keep things simple and easier for beginners, we'll use `nano`. If you know `vim`/`emacs` already you can of course choose your poison, but for most people doing this course, `nano` is an excellent choice.

Let's open the file with the command:

```
$ nano ~/.bashrc
```

Now you can see the contents of `~/.bashrc`.

![img](./img/nano_bashrc.png)

We need to scroll to the bottom, so keep hitting `down` arrow key or `Pg Down` and scroll to the end of the file.

Next, enter this on a new line:

```
fortune
```

Now we need to save the file with the changes we made. Hit `Ctrl+X` and you'll be prompted for confirmation. Hit `Y` (_Yes_) to confirm that you want to save these changes.

You can see the contents of the file you just saved using `cat`:

```bash
cat ~/.bashrc
```

To see a new fortune cookie, simply log out and log in to the server again. You'll be greeted with a message like this:

```
$ ssh karan@143.110.178.40
karan@143.110.178.40's password: 
A is for Apple.
        -- Hester Pryne
```

## Linux Directory Structure

There are some important directories inside a Linux system that as a user you should be aware of:

- `/`: Root Directory. This is the top-level directory on your system. Every single file/directory is _nested_ inside this directory.
- `/bin`: Binaries. System-level programs (binaries/executables) are present inside `/bin`. User installed binaries are placed inside `/usr/bin`.
- `/etc`: Config files. System-level config files are placed here and can be edited if required.
- `/tmp`: Temporary directory. Files placed inside here are deleted when the system is rebooted.
- `/var`: Variable data files. Files that may change by a process during its operations are placed here. Commonly used for log files that go inside `/var/log`.

## Additional Commands

Let's talk a bit about some more commands that can be used to understand the filesystem better.

- `cd` (_change the working directory_): To move to a different directory (`/var/log` for example), you can use this:

```
$ cd /var/log
```

- `ls` (_list directory contents_): To display information about files in a directory.

Expanding on the above example, let's say we need to list the contents of `/var/log` directory:

```
$ ls /var/log
apt       btmp                   cloud-init.log  dmesg     droplet-agent.update.log  kern.log   lastlog  syslog                unattended-upgrades
auth.log  cloud-init-output.log  dist-upgrade    dpkg.log  journal                   landscape  private  ubuntu-advantage.log  wtmp
```

- `mkdir` (_make directories_): To create a directory.

Using `mkdir` we can create a new directory on our filesystem:

```
$ mkdir hello-world
```

- `mv` (move (rename) files): To move a file from a source directory to a destination directory. It can also be used to rename a file.

---

Let's use the above commands in our toolset to do the following exercise:

> Create an empty file inside `/tmp` and move it to our `$HOME` directory.

1. Since we need to create the file inside `/tmp`, let's `cd` to it:

```
$ cd /tmp
```

2. Next, let's create a dummy file with `nano`:

```
$ nano hello.txt
```

Enter some dummy content and save it. We can see the file is present inside `/tmp` using ls:

```
$ ls /tmp
```

3. Finally, let's move it to our `$HOME` directory

```
$ mv /tmp/hello.txt ~/
```

We can see the file is moved to the $HOME directory using `ls`:

```
$ ls ~/
```

Congrats! In this lesson, we learnt the basics of Linux filesystem and directories, but we have barely scratched the surface of the commands that will help you manage files/directories.

You are encouraged to read `man` pages of these commands. [Manual pages](https://man7.org/linux/man-pages/) help to understand what each command does and what are the additional options (_flags_) you can pass to achieve your desired results.

To read the man page of `ls`, for example, simply enter and a manual doc will open in your terminal:

```
man ls
```

There are some useful resources like https://tldr.sh/ and https://explainshell.com/ which can help you not feel overwhelmed with too many docs suddenly and find out the flag/information about each command quickly.
