---
title: Pulling Changes
include_in_preview: false
---

As we discussed in the previous section, a collaborator can push their work to your repository. It means that we need a workflow to pull their work every now and then to ensure that your local repository is always updated. To do that, we use a command called `git pull`.

The Git pull operations, prompts Git to connect to GitHub, which acts as a remote repository, and ensure that all the changes are integrated into your local repository without any conflicts.

The `git pull` command is also a combination of two other Git commands: `git fetch`, which fetches all the new commits from the remote repository, and `git merge`, which merges the fetched commits into your local repository. Through the Git pull operation:

- Your local working branch is updated and all new commits from the remote repository are available locally.
- Your remote tracking branch is updated as well and you can continue working on any of them.

The syntax of the `git pull` command:

```sh
git pull <remote-name> <branch-name>
```

The `remote-name` acts as the name of the remote repository. The `branch-name` acts as the name of the branch that you want to pull from the remote repository.

Let's check out an example. We recently made a commit, directly through GitHub interface. Consider that this change has been made by your fellow collaborator. You need to pull those changes to ensure that your local repository is up to date. To do that, you can simply run the following command:

```sh
$ git pull origin main

remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 802 bytes | 267.00 KiB/s, done.
From github.com:HarshCasper/monschool-calculator
 * branch            main       -> FETCH_HEAD
   c3bd105..f3209e7  main       -> origin/main
Updating c3bd105..f3209e7
Fast-forward
 index.html | 4 +++-
 1 file changed, 3 insertions(+), 1 deletion(-)
```

If you do a `git log` command, you will see that the commit has been pulled from the remote repository:

```sh
commit f3209e7b30e30998bb576118f1384082185838f3 (HEAD -> main, origin/main, origin/HEAD)
Author: Harsh Mishra <erbeusgriffincasper@gmail.com>
Date:   Tue Mar 15 00:05:35 2022 +0530

    feat: add a text about the purpose of this project

commit c3bd105c8db2845c3202e953b1103d99cd8c7668
Author: HarshCasper <erbeusgriffincasper@gmail.com>
Date:   Mon Mar 14 17:34:17 2022 +0530

    feat: add a heading and a text to the index.html file
```

Using a combination of `git pull` and `git push`, you can ensure that you are pushing in small chunks of your work every now and then, and also that you are pulling in commits pushed by your collaborator. This is a very important feature of Git. With Git pull, we have covered all four network interactions in Git:

- `git clone`
- `git push`
- `git fetch`
- `git pull`

The Git fetch operation ensures that all the remote branches are updated. However no changes are actually reflected on the local repository. Only the Git merge operation, can merge all the pulled changes and ensure that the local repository is up to date.

Do note that if you have uncommitted changes, you will get a warning message. In case two commits are conflicting, a merge conflict would arise which we would need to fix. However, the goldern rule is that you should always commit your changes before pulling new commits to a remote repository.
