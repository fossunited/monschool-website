---
title: Time Travelling With Git
include_in_preview: false
---

Git also provides you time travelling capabilities! Just joking, let's see how to use it.

Using Git you can checkout any previous snapshot into the working directory. It allows you to go back in the history of your project, understand what has changed and how it has changed. It is especially useful when you are working on a project, and want to trace a bug or a feature that you would like to see the implementation for.

To do that, we use the Git checkout operation. Checkout means that we are checking out a particular snapshot of the project. Checking out a past commit will result in a detached HEAD. A detached HEAD means that after checking out a particular commit, all the changes made to the project won't belong any more to the current branch. This is the reason why Git would suggest you to commit your changes before checking out a past commit, since your work might be lost.

To checkout to a previous commit, we need to retrieve the hash of a previous version of the project. To do that, we use the `git log` command.

```sh
Author: Harsh Mishra <erbeusgriffincasper@gmail.com>
Date:   Tue Mar 15 00:05:35 2022 +0530

    feat: add a text about the purpose of this project

commit c3bd105c8db2845c3202e953b1103d99cd8c7668
Author: HarshCasper <erbeusgriffincasper@gmail.com>
Date:   Mon Mar 14 17:34:17 2022 +0530

    feat: add a heading and a text to the index.html file

commit ae4a133ae0fb235a0714718b36cb7cba5ee7028d
Author: HarshCasper <erbeusgriffincasper@gmail.com>
Date:   Mon Mar 14 13:57:40 2022 +0530

    add a basic HTML template

commit 57d21bb234802d20511cc4863c04f7bffea0d46b
Author: Harsh Mishra <erbeusgriffincasper@gmail.com>
Date:   Tue Mar 8 13:01:05 2022 +0530
```

Every commit has a hash associated with it. The hash is a unique identifier for the commit. We can use the hash to checkout to a particular commit. For example, for the commit that has the message `feat: add a heading and a text to the index.html file`, the commit hash is `c3bd105c8db2845c3202e953b1103d99cd8c7668`.

To checkout the commit `c3bd105c8db2845c3202e953b1103d99cd8c7668`, we can use the following command:

```sh
git checkout c3bd105c8db2845c3202e953b1103d99cd8c7668
```

You will receive an output similar to this:

```sh
Note: switching to 'c3bd105c8db2845c3202e953b1103d99cd8c7668'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at c3bd105 feat: add a heading and a text to the index.html file
```

You can now quickly inspect an old version of your project. However be cautious of the fact that since there is no branch reference to the current `HEAD`, you are in the detached `HEAD` state. To get back to the latest commit and the current `HEAD`, you need to use the `git checkout` command:

```sh
git switch -
```
