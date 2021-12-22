---
title: Creating Users
include_in_preview: false
---

So far, you would have observed that we are logged into our server using a `root` user. The `root` user is like an Admin user which is the most privilidged user on your system. That means it has access to modify/remove any of the file across all directories, terminate a process, spawn new processes, create new user accounts, install software packages etc.

It's a bad practice to run any process as a `root` user or to even login as a `root` user. If the server gets compromised, then the attacker has access to do any kind of task on your system. However, if we create another user which has restricted permissions, isolated filesystem access it'll help us to limit the damage in case of a compromised system.

Our task for this lesson is to create a non root user called `ubuntu`.

## Creating a User

## TODO: Explain adduser prompts.

In order to create a new user, we'll use `adduser $USERNAME`:

```
root@playground:~# adduser ubuntu
Adding user `ubuntu' ...
Adding new group `ubuntu' (1000) ...
Adding new user `ubuntu' (1000) with group `ubuntu' ...
Creating home directory `/home/ubuntu' ...
Copying files from `/etc/skel' ...
New password: 
Retype new password: 
passwd: password updated successfully
Changing the user information for ubuntu
Enter the new value, or press ENTER for the default
	Full Name []: Ubuntu
	Room Number []: 
	Work Phone []: 
	Home Phone []: 
	Other []: 
Is the information correct? [Y/n] Y
root@playground:~#
```

We can find the list of all users on the system using `less /etc/passwd`. There should be an entry for the user you just created. You can ignore all other users in this list as they are system users.

### Granting privileges

At this moment, our `ubuntu` user doesn't have any privileged permissions. But we do need some of these permissions in order to do tasks like installing packages, for example. Now, we can either do that by logging as a `root` user or by using `su` (_substitute users_). Logging as `root` user everytime you need to perform administrative tasks is a bit of hassle. And `su` doesn't give complete admin privileges.

That's where `sudo` comes in the picture. Using `sudo` you can _become_ an admin user and perform administrative tasks. Now you must be wondering how is this safe as we have bypassed the `root` user login completely.

TODO: Remove `/etc/sudoers` part.

For any user to do `sudo`, the user must be present in the `sudoers` list which is present inside `/etc/sudoers`. Let's create an entry for `ubuntu` user:

```
root@playground:~# usermod -aG sudo ubuntu
```

Let's switch to `ubuntu` user using `su`:

```
su ubuntu
```

### Viewing user ID

TODO: Talk about `whoami`

Each user on Linux get's its own user ID. To find the ID of the current user:

```
ubuntu@playground:~$ id -u
1000
```

`root` user however is a special user and it's ID is always `0` on all systems.

```
ubuntu@playground:~$ sudo su
root@playground:/home/ubuntu# id -u
0
```

Congrats! You created a non root user and used that to login to the server.
