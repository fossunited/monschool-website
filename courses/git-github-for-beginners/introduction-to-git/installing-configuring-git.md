---
title: Installing Configuring Git
include_in_preview: false
---

Before you start using Git, you need to have Git installed on your computer. Multiple Linux-based distributions come pre-installed with Git, but you can also install it yourself to make sure you are using the latest version available. On Windows and macOS, you need to install Git from scratch but it's typically easy.

## Installation

For this course, we will focus on using the Git command-line interface. We will not be covering GUI-based Git.

## Linux

If you are using Ubuntu, you can install Git with the following command:

```sh
apt-get install git
```

If you are using Fedora/RHEL/CentOS, you can install Git with the following command:

```sh
dnf install git
```

If you are using some other Linux-based distribution, look into the [Download for Linux and Unix](https://git-scm.com/download/linux) page for more information.

## macOS

You can install Git on macOS using Homebrew. If you have not used Homebrew before, you can install it with the following command:

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

After installing Homebrew, you can install Git with the following command:

```sh
brew install git
```

Optionally, you can also install Git using [XCode](https://developer.apple.com/xcode/) since Apple ships Git along with it.

## Windows

To use Git on Windows, you need to install it from [Download for Windows](https://git-scm.com/download/windows). You can choose the standalone version or the portable version.

If you are using Winget, you can install Git using:

```sh
winget install --id Git.Git -e --source winget
```

After installation, click on the downloaded installer file and select **yes** to install. The default components are automatically selected. You can additionally configure if you wish to use Git from Git BASH only or you wish to use Git from the command line and third-party tools (IDE, text editors). Furthermore, you can select the transport backend options, terminal emulator, line ending option and extra options.

-----

After installation, you can verify that Git is installed by running the following command:

```
git --version
```

On my macOS, I get the following output:

<!-- Add a screenshot showing a version message -->

## Configuration

Now Git has been installed on your machine and you are ready to explore it. Before you get started with using Git, it is preferred to configure the initial settings for user access. It is done using the `git config` command. This will serve as your Git credentials that will be a reference to your username and email address every time you make a commit. Using the `git config` command, you can save these variables at these places:

- `/etc/gitconfig`: The variables saved in this system file applies to every user on your system and all the repositories present on your local machine. You can use the `--system` flag with the `git config` command to apply this.
- `$HOME/.config/git/config`: The configuration variables saved to this file apply only to a single user, that is you. You can use the `--global` flag with the `git config` command to apply this.
- `config`: The configuration variables saved to this file apply only to the current repository. You can use the `--local` flag with the `git config` command to apply this.

Let us now register a username and an email address for our Git. To register a username, run the following command:

```sh
git config --global user.name "Your Name"
```

To register an email address, run the following command:

```sh
git config --global user.email "yourmail@mail.com"
```

You have now successfully registered a username and an email address for Git. Now that you have set an identity for yourself on Git, you can further customize your Git experience. For example, if the default text editor that you plan to use with Git is VS Code, you can set that using:

```sh
git config --global core.editor code
```

This will use the VSCode executable code. For windows users, you will need to specify the full path to the editor you want to use.

## Configuring SSH

SSH (Secure Shell) is a protocol that is used to connect and authenticate to remote machines. It is used to securely transfer files to and from remote machines and run commands while getting the output back and forth. With SSH keys, you can securely connect your local Git repository to a remote machine from where you can push or pull your updates. If you are using a Git-based provider, you won't have to provide your username or password at each visit.

While setting up SSH, you create a private and public key pair. The private key is saved to your local computer, generally in the `.ssh` directory. The public key is uploaded to the server to authenticate the request. You can generate a key using `ssh-keygen`:

```sh
ssh-keygen
```

After passing this command, you will be asked to set a filename and passphrase. Hit enter twice to pass the default option. Now run the following command to verify the keys that have been created by listing the directory:

```sh
ls ~/.ssh 
```

You will get a pair of key filenames as an output: `id_rsa` is the private key. `id_rsa.pub` is the public key. To avoid typing your password to push/pull changes to the remote repository, add it to the `ssh-agent`:

```sh
eval `ssh-agent` 
ssh-add ~/.ssh/id_rsa
```

You can now upload the public key to a Git-based provider of your choosing. In the later chapters, we will take a look at how you can do that with GitHub.

## Conclusion

In this chapter, we have covered the basics of how you can download and install Git on your computer. We have also covered how to configure Git to use your username and email address along with configuring SSH for pushing and pulling changes to the remote repository. In the next section, we will understand Git-based providers better and what is their exact purpose.
