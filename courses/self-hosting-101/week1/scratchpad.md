---
title: Setting up a VPS
include_in_preview: false
---

TODO:
- [ ] Add objectives and add tasks (1/2/3) for setting up a server.
- [ ] Get a droplet
  - [ ] Feedback Form -> IP Address, Provider.
- [ ] `mon-school`
- [ ] Talk about apt before user

### Actionable Tasks

- [ ] Creating the droplet
- [ ] Installing `mon-school-agent`
- [ ] Editing files on server
  - [ ] cd ; ls; pwd; mkdir; nano
- [ ] Adding a non-root user
- [ ] Setting up SSH keys
  - [ ] Authorized Keys
- [ ] Installing a package
- [ ] Set a hostname
- [ ] Run a command in `tmux`. (Verify with `mon-school-debug`)

### Tests

- [ ] Ping the IP
- [ ] Verify `mon-school-agent` is running on port
- [ ] Read the file `/public/hello.txt`
- [ ] User list `ls /home`
- [ ] `~/.ssh/authorized_keys` <- Get the key name
  - [ ] `"users": [{"name": "anand", "authorized-keys": ["anand-bodhi"]}`
- [ ] `/apt/packages` <- dpkg/apt (Package name can come from config file)
- [ ] `hostnamectl`
- [ ] `pstree`

To get started with self hosting, you'll need a server to run the applications. There are multiple options to get a server:

- Cloud based providers like AWS, DigitalOcean etc.
- Raspeberry Pi
- NAS like Synology

Some of these options require you to have purchased hardware. However if you don't want to make the upfront commitment of a hardware purchase as well as the responsibility of a high uptime, cloud based providers are a fantastic choice for majority of the people. You can get started for as low as $5 on DigitalOcean, AWS provides a free tier for 1 year and you can check other providers for cheaper costs as well.

For this course we'll be using DigitialOcean but you're free to choose any provider you're most comfortable with. The commands/concepts demonstrated in this course are universal and not tied to any particular vendor, unless specified otherwise.

## SSH

Before you create a server, it's important to understand how to connect to it "securely". Since the server is "on cloud" (aka someone else is managing it for you), you need a secure way to access the machine. There are mainly 2 ways you can do it:

- Password based login. Some providers like DO provide access to the machine using their UI after you enter the "root password". However, if the password leaks, anyone in the world can access it.

- SSH based login: SSH is a way to let the server know it's you who is actually entering the machine. Imagine having a key and a lock. The server is locked down and you provide the key. The `ssh-agent` which is running inside the server then checks whether your key is valid or not (it maintains a list of authorized keys). If what you are providing is a valid key, the ssh-agent will accept the connection and let you in.

### Generating Keys
 
<Steps from GitHub article https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent>

### Add SSH Key to DO

<TODO: add screenshots>

## Creating a user

Once you're logged in the machine, there are a few things we need to edit to do to make it more secure.

The `user` which you are logged in as is called the `root` user. You can check the user details with `id`. A root user has a user id (UID) as `0`.

We need to create a separate non root user. A root user in Linux is the highest privilidge user and can do all kinds of tasks in it. Some examples:

- Run an application on a port < 1024
- Read/Write/Modify access any file
- Update packages globally
- User management

It's not a good idea to run any service as root unless really needed (that would be ~<1% of the case). So, we should create a non root user:

<TODO: Steps to do that>

## Package Management

In Linux, different distributions contain different ways of managing software packages. These packages consists of Audio/Video drivers, Kernel, system software and even user level software. This course is targetted for `debian` based distributions, which use `apt`.

`apt` is the package manager that comes installed with any `.deb` system. With `apt` you can add/remove packages or update existing ones.

<TODO; Show some apt-get commands>

```
apt-get update
apt-get upgrade
<!-- apt-get install vim -->
```

## Editing Files

TODO: Change to `nano`.

When we are SSH'ed in the server, we need a way to way to edit files. You'll sometimes need to edit the config files of the software you are deploying, modfiy the contents of a system file (like `~/.ssh/authorized_keys`) etc. In the above step we installed `vim`. `vim` is an extended version of `vi` a very popular and old software for editing files.

Some of the basics of `vim`:

<TODO: Add basic navigation of vim and commands like writing to buffer, inseting and saving>

## Getting Comfortable

If you've reached this far, give yourself a pat on the back. We've made it to the end of first week. It's now time for you to feel more comfortable in the server and we encourage you to try different experiments/commands on the system.

Some examples:

See your IP Address:

```
ip addr
```


Set the hostname of your machine

```
sudo hostnamectl set-hostname <your-name>
```

