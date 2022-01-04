---
title: Creating Users
include_in_preview: false
---

## Lesson Objectives

- [ ] Create a non-root user
- [ ] Understanding Access Levels and Controls
- [ ] Access droplet with non root user

### Refresher

We'll use some concepts here that was learned in the previous lesson. You can take a quick look at them to refresh them:

- `ssh user@ip` command to login from [Creating droplet lesson](./creating-droplet.md)


In the previous lesson, you would have observed that we logged in to the server using a `root` user. The `root` user is an _Adminstrator_ which is the most privileged user on the system. This means that it has the access to modify/remove any file across all directories, create/destroy processes, modify user accounts, install software packages etc.

It's generally a bad practice to run any process as a `root` user unless it's required. There are some tasks in Linux that can only be performed by a root user. However, besides that kind of task, we should not be running anything with a `root` user. In case the server gets compromised, then the attacker has full access to your system and the blast radius of the attack is widened. A good thumb of rule is to follow _Principle of Least Privilege_ to limit the blast radius in an attack. Creating a secondary, non-root user will help us achieve that.

Let's begin to do that, by _adding_ a new user to our system:

## Creating a User


To create a new user, we'll use the command `adduser`:

**NOTE**: Remember to substitute the word `karan` with your username in the following commands:

```
root@143.110.178.40's password: 
root@playground:~# adduser karan
Adding user `karan' ...
Adding new group `karan' (1000) ...
Adding new user `karan' (1000) with group `karan' ...
Creating home directory `/home/karan' ...
Copying files from `/etc/skel' ...
New password: 
Retype new password: 
passwd: password updated successfully
Changing the user information for karan
Enter the new value, or press ENTER for the default
    Full Name []: 
    Room Number []: 
    Work Phone []: 
    Home Phone []: 
    Other []: 
Is the information correct? [Y/n] Y
```

`adduser` opens an interactive prompt and asks for a few basic questions:

- `Password`: Type in a password that you will use to log in to this user.
- `Full Name`: You can enter your full name for the system to add more details.

Rest of the details you can leave empty as they are not required. Confirm the information with `Y` (_Yes_) and you're good to go!
### Granting privileges

At this moment, our `ubuntu` user doesn't have any privileged permissions. But to self-host applications, we'll need to perform tasks like installing packages, editing system files etc. We'll need to allow our `ubuntu` user to _become_ a privileged user to perform these tasks.

That's where `sudo` comes in the picture. Using `sudo` you can _become_ a root user and perform administrative tasks.

**NOTE**: Remember to substitute the word `karan` with your username in the following commands:

```
$ usermod -aG sudo karan
```

Perfect! We have added the user `karan` to a list of users who can use `sudo` (that list is called a `sudoers` file)

Let's switch to the user you created using `su`:

**NOTE**: Remember to substitute the word `karan` with your username in the following commands:

```
$ su karan
```

### Viewing user ID

Using the command `whoami` you can view the current user:

```
$ whoami
karan
```

This shows that we are currently logged in as `karan` user.

### Accessing droplet with non-root user

In the previous lesson, we used `ssh root@<ip>` to access our droplet. Since we have now created another user for ourselves, we'll use that to access the droplet from now:

```
$ ssh karan@143.110.178.40
karan@143.110.178.40's password: 
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

karan@playground:~$
```

Congrats! In this lesson, you have created a non-root user and learnt a bit about privilege escalation. In the next lesson, we'll learn how to install system packages and the concepts explained in this lesson like `sudo` will be used to perform some of the commands in that listen.
