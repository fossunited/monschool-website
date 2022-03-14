---
title: Time Travelling With Git
include_in_preview: false
---

The primary responsibility of Git is to track changes and make sure that the changes are not being lost. It gives you a tighter control over your development workflow and helps you to keep your project clean and organized. However, a situation might arise where you need to travel back in time and see what was the state of your project at a particular point in time and make some changes to it. 

Git provides these time-traveling capabilities by allowing us to re-write the history of the files, under the pretext that some of these changes might be dangerous. Under this situation, its important for us to know and understand the concept of history re-writing commands for Git and how they work. We will also look into avoiding any pitfalls that might lead to a loss of data or context.

## Amending your last commit

The `git commit --amend` command allows us to amend the last commit that we made. This is useful when we want to make a change to the last commit and we want to keep the same message, without creating an entirely new snapshot. When we apply a `git commit --amend`, we don't just alter the last commit, we replace it completely. For Git, it would look like an entirely new commit with the same message, but a different hash. But where do we exactly get to apply this?

Let us take an example: We recently made a commit and pushed it to our remote repository where an automated workflow with test your code. However we realized that we forgot to stage and commit a file without which the tests would fail. We don't want to create a new commit, hence we can just amend the last commit. It is a part of everyday development workflow and gives you a handy way of dealing with this situation.

Let's take a live example. For our `monschool-calculator` repository, we have a file called `index.html`. Let us make a change to it. We will replace the text `MonSchool Calculator` by making it a H1 heading. You can do that by replacing the text with `<h1>MonSchool Calculator</h1>` in the file.

Perform a `git status` to see the changes that we have made:

```sh
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   index.html

no changes added to commit (use "git add" and/or "git commit -a")
```

Let's make a commit:

```sh
$ git add .
$ git commit -m "feat: change some text in the index.html"
[main c25b11b] feat: change some text in the index.html
 1 file changed, 1 insertion(+), 1 deletion(-)
```

However we forgot to add some new changes to the last commit. We want to have a small description about what the project does. Hence we add some background information by putting a `<p></p>` tag in the file. This is how it would look after our change:

```sh
  <p>
    This is a sample project for the purpose of the MonSchool Git & GitHub course.
  </p>
```

We want to push this change to the same commit. Fixing this error is simply a matter of staging the changes and committing them by adding a `--ammend` flag to the `git commit` command:

```sh
$ git add .
$ git commit --amend --no-edit

[main 168cf0f] feat: change some text in the index.html
 Date: Mon Mar 14 17:34:17 2022 +0530
 1 file changed, 4 insertions(+), 1 deletion(-)
```

The `--no-edit` flag tells Git to not make any changes to the Git commit message. If you would like to change the commit messag, you can use the command without the `--no-edit` flag and you can change the commit message before saving and closing the file.

## Rebasing your commits

Rebasing is the process of moving or combining multiple commits to a new base commit. Using Git rebase, you can change a set of commits and clean them up before you merge them into your default branch. This is specially useful when you want to delete commits, change your commit message to something else or just combine multiple commits into a single commit.

You would possibly not need rebase while working on your personal projects. However, if you are collaborating with others, you might need to rebase your commits to make sure that you are working on the same page. You can just use the `git rebase` command to rebase your commits. To use an interactive rebase, just add a `-i` flag to the command.

Let us check that out for the `monschool-calculator` repository:

```
$ git rebase -i

pick 168cf0f feat: change some text in the index.html

# Rebase ae4a133..168cf0f onto ae4a133 (1 command)
#
# Commands:
# p, pick <commit> = use commit
# r, reword <commit> = use commit, but edit the commit message
# e, edit <commit> = use commit, but stop for amending
# s, squash <commit> = use commit, but meld into previous commit
# f, fixup [-C | -c] <commit> = like "squash" but keep only the previous
#                    commit's log message, unless -C is used, in which case
#                    keep only this commit's message; -c is same as -C but
#                    opens the editor
# x, exec <command> = run command (the rest of the line) using shell
# b, break = stop here (continue rebase later with 'git rebase --continue')
# d, drop <commit> = remove commit
# l, label <label> = label current HEAD with a name
# t, reset <label> = reset HEAD to a label
# m, merge [-C <commit> | -c <commit>] <label> [# <oneline>]
# .       create a merge commit using the original merge commit's
# .       message (or the oneline, if no original merge commit was
# .       specified); use -c <commit> to reword the commit message
```

You can now see that our last commit is visible along with various options. You can reword a commit message, drop (or delete) it, squash the commit and more. Let us re-word our commit to something more meaingful. Use your editor to navigate to the `pick 168cf0f feat: change some text in the index.html` line and replace `pick` with `e` or `edit` to edit the commit message.

```sh
e 168cf0f feat: add a heading and a text to the index.html file

# Rebase ae4a133..168cf0f onto ae4a133 (1 command)
```

Once done, you will see the following:

```sh
Stopped at 168cf0f...  feat: add a heading and a text to the index.html file
You can amend the commit now, with

  git commit --amend 

Once you are satisfied with your changes, run

  git rebase --continue
```

Push `git commit --amend` on your terminal and change the top-most line there to the new commit message:

```sh
feat: change some text in the index.html

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
```

Finally run `git rebase --continue` to see the following output:

```sh
git rebase --continue
Successfully rebased and updated refs/heads/main.
```

On doing a `git log`, you will see the following:

```sh
commit b1f8768a36aacc1f7cfffb6aac1d4c5d36f6fcb9 (HEAD -> main)
Author: HarshCasper <erbeusgriffincasper@gmail.com>
Date:   Mon Mar 14 17:34:17 2022 +0530

    feat: add a heading and a text to the index.html file
```

Now you can use `git rebase -i` to replay the commits using specific commands you have specified.

You can additionally squash your commits as well. This is useful when you want to combine multiple commits into a single commit.

Let's take an example. Change the title of our `index.html` file from `Calculator` to `MonSchool Calculator`. Make a commit and see the following log:

```sh
commit 65d294881403d121674c7a5b5eeb68c29c77cb8c (HEAD -> main)
Author: HarshCasper <erbeusgriffincasper@gmail.com>
Date:   Mon Mar 14 18:00:05 2022 +0530

    feat: changed the html title

commit b1f8768a36aacc1f7cfffb6aac1d4c5d36f6fcb9
Author: HarshCasper <erbeusgriffincasper@gmail.com>
Date:   Mon Mar 14 17:34:17 2022 +0530

    feat: add a heading and a text to the index.html file
```

We now want to squash these two commits together. Let's see how the interactive rebase can help.

We have two commits here. Keep in mind that we must always squash a commit into another commit. Push the following command on your terminal:

```sh
git rebase -i HEAD~2
```

You will see the following output:

```sh
pick b1f8768 feat: add a heading and a text to the index.html file
pick 65d2948 feat: changed the html title

# Rebase ae4a133..65d2948 onto ae4a133 (2 commands)
```

Replace the `pick` command with `s` or `squash` to squash the commits. In our case, we will edit the `pick` command to `s` or `squash` for `pick 65d2948 feat: changed the html title`. Save the file and close it, and you will be greeted with the following output:

```sh
# This is a combination of 2 commits.
# This is the 1st commit message:

feat: add a heading and a text to the index.html file

# This is the commit message #2:

feat: changed the html title
```

You can comment out the second commit message `feat: changed the html title` by adding a `#` at the beginning of the line. This will ensure that Git ignores this as a commit message. Save and close the file and you will see the following output:

```sh
[detached HEAD c3bd105] feat: add a heading and a text to the index.html file
 Date: Mon Mar 14 17:34:17 2022 +0530
 1 file changed, 5 insertions(+), 2 deletions(-)
Successfully rebased and updated refs/heads/main.
```

On performing a `git log`, you will see the following:

```sh
commit c3bd105c8db2845c3202e953b1103d99cd8c7668 (HEAD -> main)
Author: HarshCasper <erbeusgriffincasper@gmail.com>
Date:   Mon Mar 14 17:34:17 2022 +0530

    feat: add a heading and a text to the index.html file

commit ae4a133ae0fb235a0714718b36cb7cba5ee7028d (origin/main, origin/HEAD)
Author: HarshCasper <erbeusgriffincasper@gmail.com>
Date:   Mon Mar 14 13:57:40 2022 +0530

    add a basic HTML template
```

Our commit has now been squashed and is no longer visible! If you sense that something is going wrong, you can use `git rebase --abort` to skip the rebase operation immediately.

## Refloging

Git keeps tracks of updates to the branches using a mechanism called as `reflog`. It can allow you to go back to the changesets that were made before a specific commit and are no longer available. The reflog contains all of the information about the branches, their respective states and more.

To do a reflog, you can use the following command:

```sh
git reflog
```

In our case you will see the following output:

```sh
c3bd105 (HEAD -> main) HEAD@{0}: rebase (finish): returning to refs/heads/main
c3bd105 (HEAD -> main) HEAD@{1}: rebase (squash): feat: add a heading and a text to the index.html file
b1f8768 HEAD@{2}: rebase (start): checkout HEAD~2
65d2948 HEAD@{3}: commit: feat: changed the html title
b1f8768 HEAD@{4}: rebase (continue) (finish): returning to refs/heads/main
b1f8768 HEAD@{5}: commit (amend): feat: add a heading and a text to the index.html file
```

You can also check the reflog for a specific time period using:

```sh
git reflog --relative-date
```

Git reflog provides a safety net in case something goes wrong. Rebase operation is tricky and we will further explore it in upcoming chapters.
