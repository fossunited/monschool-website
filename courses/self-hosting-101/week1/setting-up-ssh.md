---
title: Setting up SSH Access
include_in_preview: false
---

So far we've been logging to our servers using a `root` password. The problem with that is, if this password gets leaked then anyone having access to the password will
be able to access your server. There are some automated malicious bots that repeatedly try to authenticate with common known passwords and if your password is not secure enough, there are high chances of getting your server compromised.

A better approach is to use **Keys** for logging in. SSH Keys are is a pair of 2 keys - Public and Private. Public keys can be shared with anyone, however Private keys must be protected by you. Private Keys are the one that determine if it's actually _you_ who is logging in the server.

## How a Key Exchange Happens

- You need to have a SSH key generated locally.
- On your server, you need to enter your **Public Key** in a file `~/.ssh/authorized_keys`. As the name suggests, SSH via Keys will only be allowed for the list of keys present in that file.
- When you SSH to the server, the server checks if the client's public key is present in the `~/.ssh/authorized_keys` list. If it's not present, it will reject the connection and client won't be able to login. If however the key is present, it will encrypt a random string and send it to the client.
- The client will try to decrypt this string using the **Private Key**. It appends a unique ID to the decrypted messages, hashes the message and sends it back to the server. The server has the original decrypted message and the unique ID already, so it computes whether both hashes match exactly or not. If they match, that means the client was using the correct **Private Key** for the _Public Key_ present in the `~/.ssh/authorized_keys` and allow the client to login to the server.

Now that we understand how SSH Key Exchange works in theory, let's create a key for ourselves and SSH in our server using it.

### Step 1: Generate a SSH Key

TODO: ssh-keygent no args
TODO: Warn about prev keys

```
ssh-keygen -t ed25519 -C "your_email@example.com"
```

It'll prompt you where to create the keys (the default location is `~/.ssh/id_ed25519`). It'll also prompt you to enter a passphrase to access the key, enter a secure passphrase.

### Step 2: Add it to the agent

Your local machine is running an `ssh` agent, which is the `client` that we referred above. We need to add the key to this agent's session, so it knows that when a new SSH connection is created with the server, it can provide the _Public Key_ to it.

- First ensure the agent is running:

```
eval "$(ssh-agent -s)"

Agent pid 171050
```

- Next, add the key

```
ssh-add ~/.ssh/id_ed25519
Identity added: /home/karan/.ssh/karan_monschool (karan@monschool.net)
```

### Step 3: Add the Public Key to Server

Login to the server using our password.

```
ssh root@<PUBLIC IP>  
root@<PUBLIC IP>'s password: 
```

Switch to `ubuntu` user, as we want to restrict our SSH only to the `ubuntu` user:

```
su - ubuntu
ubuntu@playground:~$ 
```

Next, let's navigate inside the `~/.ssh` directory. To do that, we'll `cd` in it:

```
cd ~/.ssh/
```

Now, before we edit the file, it's a good practice to explore all the files present in the directory. You can use `ls` to _List all files_ in the directory.

```
$ ~/.ssh$ ls
authorized_keys
```

As you can see, we already have `authorized_keys` inside the `~/.ssh` directory. Let's create a backup of this file before we edit. In case something goes wrong, we can replace our file with the backup. To do that, we need to use `cp`. `cp` is used to copy files.

Basic syntax of `cp` looks like:

```
cp source dest
```

Let's take a backup of `authorized_keys` as `authorized_keys.bak`:

```
cp authorized_keys authorized_keys.bak
```

To ensure that the file is copied, we can `ls` the directory and we should see both the files:

```
$ ls
authorized_keys  authorized_keys.bak
```

Perfect! Now, let's edit the `authorized_keys` file using `nano` that we learnt in our earlier lesson:

```
nano authorized_keys
```

As you can see, the file is currently empty. Let's copy our **Public Key** that we created inside this.

To do that, open a new terminal session on your local machine and copy the contents of `~/.ssh/id_ed25519.pub` (or if you chose a custom path for the public key, use that) file:

```
$ cat ~/.ssh/karan_monschool.pub 
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIF1mu97d97beaTuY6/DEYEfwG9ETv+71e49RmPzEoDVO karan@monschool.net
```

Now, go back to the `nano` editor and pase this line. Hit `Ctrl X` to save. Verify that the file is saved correctly by seeing the contents of it:

```
$ cat ~/.ssh/authorized_keys
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIF1mu97d97beaTuY6/DEYEfwG9ETv+71e49RmPzEoDVO karan@monschool.net
```

Perfect! Now let's actually try to login to this server using the SSH key.

```
$ ssh ubuntu@<ip>
```

You are now logged in to the server without being asked for a password!

There are some additional configurations that you can do to keep your server more secure, such as listening on a non default port (other than `22` to restrict connection attempts by automated bots), allow certain users to SSH etc. For a comprehensive article on the same, visit [this tutorial](https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys).
