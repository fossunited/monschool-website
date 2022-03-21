---
title: Merging
include_in_preview: false
---

As we discussed in the previous section, one of the most powerful feature in Git is to create branches for parallel development. We can capitalize upon Git's distributed nature to create a new branch, propose new changes and delete them later. However, the proposed changes should make their way to the default `main` branch. This is where we arrive at the concept of Git merging.

Git merging allows you to integrate your changes from one branch to another. It is the safest way to make sure that the commits you made on your branch find their way to the `main` branch. It also makes sure that in case your branch is deleted, your work is not lost.

## Git Merge

The `git merge` command will merge any changes that were made to the codebase on another branch to your current branch. 

The syntax is:

```sh
git merge <branch-name>
```

The `<branch-name>` is the name of the branch that you want to merge with your current branch.

Let's take our previous example. We had a branch named `monschool-calculator-html`. We made some changes to our `index.html` file and we want to merge those changes to the `main` branch. To do that, we need to first switch to the `main` branch:

```sh
$ git checkout main

Switched to branch 'main'
Your branch is up to date with 'origin/main'
```

You can now enter the following command to merge the changes:

```sh
git merge monschool-calculator-html

Updating f3209e7..664c2eb
Fast-forward
 index.html | 38 ++++++++++++++++++++++++++++++++++++++
 1 file changed, 38 insertions(+)
```

Let's do a `git log` to see what we have done:

```
commit 664c2eb1ed65a190644835aff2d79277f36a00c7 (HEAD -> main, monschool-calculator-html)
Author: HarshCasper <erbeusgriffincasper@gmail.com>
Date:   Mon Mar 21 11:42:46 2022 +0530

    add HTML for the calculator page

commit f3209e7b30e30998bb576118f1384082185838f3 (origin/main, origin/HEAD)
Author: Harsh Mishra <erbeusgriffincasper@gmail.com>
Date:   Tue Mar 15 00:05:35 2022 +0530

    feat: add a text about the purpose of this project
```

As you can see, the commit that we made on the `monschool-calculator-html` branch is now merged to the `main` branch.

## Merge Failures

There are specific cases when merging will fail. Let us take a few examples.

Suppose you have un-committed changes on your branch. Let's say you have made a change to `index.html` and you want to merge the commits from another branch to your `main` branch. In this situation, Git will ask you to commit your changes before merging.

In this situation, you can create a new branch and commit those changes:

```
git checkout -b <new-branch-name>
git add .
git commit -m "<commit-message>"
```

Or you can stash them! Git stash saves the uncommitted changes locally. It can then allow you to make any sort of changes, switch different branches, merge other branches and more. Once you are satisfied, you can bring those changes back when you need them. A stash does not save the changes files in the index and it is not committed.

To stash your changes, you can use the following command:

```sh
git stash
```

To get your changes back, you can use the following command:

```sh
git stash pop
```

We have explored how we can deal with uncomitted changes! But what if we are dealing with a conflict. Let's take an example.

You are working on a feature branch and you have made some changes to the `index.html` file. Now, you want to merge those changes to the `main` branch. However, your friend has made some changes to the `index.html` file and you pulled their changes from the remote repository.

Now, you have a conflict. Both of you have made changes to the same file portions and they are conflicting. This is because Git does not know how to merge the changes together and which commits should be applied to the file. This is a popular case of a merge conflict. In the next section, we will further explore what merge conflicts are and how to resolve them.
