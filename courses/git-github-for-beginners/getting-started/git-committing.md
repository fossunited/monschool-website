---
title: Git Committing
include_in_preview: false
---

The primary purpose of Git is to version your code. Git allows you to track changes to your code and to keep track of the changes in a repository. Now that we have cloned a repository and will be making changes, we need a credible way through which changes can be tracked and added. It brings us to the topic of having Git save our current state of the repository and make sure that new changes are tracked continuously.

In Git terminology, we call this a **commit**. A commit is a snapshot of the repository at a particular point in time which is then entered into the repository's history. To make a commit, we need to:

1. Move the changed files to a **staging area** from where we can make a commit.
2. Finalize a commit by adding a human-readable message.

The staging area is necessary because it signifies the Git that we would like the changed files to be tracked. But why it is necessary? Staging area allows you to include and exclude specific files from being tracked. 

Let us take an example. You are working on publishing your recent pictures on your social media profile. You have a bunch of pictures that you want to publish on your social media pages. But you don't want to publish specific pictures because of one or the other reason. For now, you wish to only publish those pictures that are perfect to go on your social media profile. So, you can move only those pictures which you wish to publish to the social media post and publish it. Later, you can fine-tune the rest of pictures and publish them on your social media profile as and when you want.

In a similar way, using Git, you can stage the specific files that you wish to be committed by Git. Rest of the files that are not staged, will not be tracked by Git and you can commit them later. Thus, you won't run into a risk of committing a change that you are still working on.

## Staging changes using Git

Before you start, let's make a change to the repository. In the previous chapter, we have cloned the `monschool-repository`. In your case, the repository has been created under your profile and hence you would be working on your own personal repository.

Go ahead and make a new file in the repository. Let's call it `main.py`. We will add a simple function to this file to add two arithmetical numbers.

```
def sum(a, b):
    """Sum of two numbers"""

    return a + b

if __name__ == "__main__":
    print(sum(2, 3))
```

Save the file. Let's check the status of the repository by using `git status`.

```sh
$ git status

On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	main.py

nothing added to commit but untracked files present (use "git add" to track)
```

We see a message stating `nothing added to commit` which means that the file is not tracked by Git. We can use `git add` to track the file. This would make the file ready for commit.

```sh
git add main.py
```

You will see that the terminal did not show any output which means that the command has successfully executed. Let's do another status check:

```sh
$ git status

On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   main.py
```

The file `main.py` would be highlighted in green which means that it is ready for commit.

## Committing changes using Git

After staging our files using Git, we can commit the changes using `git commit`. This would make the changes that we have staged a permanent part of the repository. To commit your changes, you can push the following command to the terminal:

```sh
git commit -m "Name of your Commit Message"
```

The `-m` flag is interesting here. It provides a human-readable message which is used to describe the changes that you are committing. This message will be displayed to other collaborators and even your own future-self who will be able to see the changes that you have made and would like to infer the context of the changes.

Let's see what happens after we make a commit with the `main.py` file:

```
$ git commit -m "add a Python file to add two numbers"

[main 815e01f] add a Python file to add two numbers
1 file changed, 8 insertions(+)
create mode 100644 main.py
```

It means that we have successfully made a commit and the changes that we have made are now permanent. The first line of the output is the commit message while the second line displays the number of insertions and deletions that have happened.

Let's check the status of the repository:

```sh
git status

On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
```

Interestingly, the status of the repository is now clean. This means that there are no changes that are staged for commit. It means that we are up-to-date and there are no uncommitted changes. If you edit the `main.py` file again, you will see a message stating that there are changes that are not staged for commit.

You can use `git log` to generate a log about all the commits inside the repository. Let us check our logs and see what effect our commit has on the repository:

```sh
$ git log

commit 815e01f0aa805398cda470c6e8dfd416641ec256 (HEAD -> main)
Author: HarshCasper <erbeusgriffincasper@gmail.com>
Date:   Tue Mar 8 14:03:59 2022 +0530

    add a Python file to add two numbers
```

The output will display the commit message and the commit hash. The commit hash is a unique identifier for the commit. You can also see the author, the date and the time of the commit. In the above example we only see one commit, but git will generate a continuous log of it. You can exit out of it by pressing the `q` key to return to the terminal.
