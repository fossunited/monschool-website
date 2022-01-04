---
title: Setting up SSH Access
include_in_preview: false
---

## Lesson Objectives

- [ ] Understand how SSH Key Exchange Works
- [ ] Create your SSH Key
- [ ] Access droplet using SSH Key

### Refresher

We'll use some concepts here that was learned in the previous lesson. You can take a quick look at them to refresh them:

- `cd`, `ls`, `cd`, `nano` commands from [Filesystem lesson](./working-with-files-directories.md)
- `ssh user@ip` command to login from [Creating droplet lesson](./creating-droplet.md)

Since the time we'd set up our droplet, we have used a _root password_ to access our droplet. This method is not secure enough because if this password gets leaked then anyone having access to the password will be able to access your server.

Some automated malicious bots repeatedly try to authenticate with commonly known passwords and if your password is not secure enough, there are high chances of getting your server compromised.

A better approach is to use **SSH Keys**. SSH Keys is a pair of 2 keys - _Public_ and _Private_. Public keys can be shared with anyone, however, Private keys must be protected by you. Private Keys are the one that determines if it's actually _you_ who is logging in to the server.

## How a Key Exchange Happens

- You need to have an SSH key generated locally.
- On your server, you need to enter your **Public Key** in a file `~/.ssh/authorized_keys`. As the name suggests, SSH via Keys will only be allowed for the list of keys present in that file.
- When you SSH to the server, the server checks if the client's public key is present in the `~/.ssh/authorized_keys` list. If it's not present, it will reject the connection and the client won't be able to log in. If however, the key is present, it will encrypt a random string and send it to the client.
- The client will try to decrypt this string using the **Private Key**. It appends a unique ID to the decrypted messages, hashes the message and sends it back to the server. The server has the original decrypted message and the unique ID already, so it computes whether both hashes match exactly or not. If they match, that means the client was using the correct **Private Key** for the _Public Key_ present in the `~/.ssh/authorized_keys` and allowing the client to log in to the server.

Now that we understand how SSH Key Exchange works in theory, let's create a key for ourselves and SSH in our server using it.

### Step 1: Generate an SSH Key

*NOTE*: Run this on your local machine (not on the droplet).

```
$ ssh-keygen

karan@playground:~$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/karan/.ssh/id_rsa): 
Created directory '/home/karan/.ssh'.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/karan/.ssh/id_rsa
Your public key has been saved in /home/karan/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:/cub11pqZ4W2rQlsbXYCyYTbkSG7+zyC2nGYrZ1poYU karan@playground
The key's randomart image is:
+---[RSA 3072]----+
|          . .    |
|           + o   |
|          o +    |
|         . * o   |
|        S + =. . |
|         + +Eo+ .|
|        +.+.=+=++|
|       ..=oBo*+*=|
|      ..o.+.E=== |
+----[SHA256]-----+
karan@playground:~$ 
```

**NOTE**: If you already have an existing SSH Key you can keep using it. If you want to use a new SSH key, ensure that you save it to a different path so that your current key doesn't get overwritten.

It'll prompt you were to create the keys (the default location is `~/.ssh/id_rsa`). It'll also prompt you to enter a passphrase to access the key, enter a secure passphrase.

### Step 2: Add it to the agent

Your local machine is running an `ssh-agent`, which is the `client` that we referred to above. We need to add the key to this agent's session, so it knows that when a new SSH connection is created with the server, it can provide the _Public Key_ to it.

- First, ensure the agent is running:

```
$ eval "$(ssh-agent -s)"

Agent pid 171050
```

- Next, add the key

```
$ ssh-add ~/.ssh/id_rsa
Identity added: /home/karan/.ssh/karan_monschool (karan@monschool.net)
```

### Step 3: Add the Public Key to Server

Login to the server as a normal user:

```
$ ssh karan@ip  
```

Next, let's navigate inside the `~/.ssh` directory. To do that, we'll `cd` in it:


```
$ cd ~/.ssh/
```

Let's create a file `~/.authorized_keys` in this directory. This file has a list of all **Public Keys** that will be allowed to access this user. 

To edit this file, we'll use `nano`:

```
$ nano ~/.ssh/authorized_keys
```

Let's copy our **Public Key** that we created inside this.

To do that, open a new terminal session **on your local machine** and copy the contents of `~/.ssh/id_rsa.pub` file:

```
$ cat ~/.ssh/id_rsa.pub 
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC0dCvNUhvfS2UXTDEQN7krsBNry4uhUT2LTwIlSO+vSGDfYV7gSJPPwidSdwml8v6l+c7UzsespvqOZBcguznASPwDpJN4v2EMwdEFOQ3im/NOS/9uYnYvL4K+GPgY17bOQy0c5utsc5L9pqCVFlv/bmIhi19lQLQgShYI9NWkVdFgg1slFwFptc2+QP1YyheMQHwR3jukSMwwTeHYyfSDx/h62HCdKcbhkK3F1y5RNRt+nsnh7JwxGOYNW/vj5gCzZ2JLqtjyTfzoaCT6tojxrgDRKaq5fzlJse3aG9HiqSZoBSaV3BBlCrAUFh7Xs2cCbxRIUHi1WPIFpbX5xddyjl7/px85ljfSZl2ncIimMfeIAoIiXjNqBUD9p12PPgtIKETahFLcKFIyHhCJisPKxl4p8X0vCB9PpV5+MuZ2IX1bDfytJByL54Dvrbha1sNBWPsLVXiDZs8O/2rPgIuHcaRDnjiXTPhk3MXDP9d8DwXGDo5ytxziip11YmnJ+GE= karan@iris
```

Now, go back to the `nano` editor and paste this line. Hit `Ctrl X` to save. Verify that the file is saved correctly by seeing the contents of it:

```
$ cat ~/.ssh/authorized_keys
```

Perfect! Now let's try to log in to this server using the SSH key.

```
$ ssh karan@143.110.178.40
```

You'll observe that you are not prompted for a password anymore. This verifies that our SSH Key is working correctly!

### Additional Resources

There are some additional configurations that you can do to keep your server more secure, such as listening on a non-default port (other than `22` to restrict connection attempts by automated bots), allowing certain users to SSH etc. For a comprehensive article on the same, visit [this tutorial](https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys).


Congrats! In this lesson, you learnt how to make access to your droplet more secure!
