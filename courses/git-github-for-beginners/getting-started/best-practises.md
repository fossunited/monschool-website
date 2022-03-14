---
title: Best Practises
include_in_preview: false
---

Git has become ubiquitous in the software development world. Using Git, you can now track your changes, push them to a remote repository and also collaborate with your team. With every tool, there are some recommended best practices that you can follow. These best practices can improve collaboration, reduce the risk of errors and make your contributions more maintainable over time.

## Making simple & clean commits

While working on your project, you might encounter some feature or a bug that immediately needs to be worked upon. While working on that particular task, you might encounter another task that needs to be worked upon and even more. All of this would be snowballed into a single commit that would generate a large difference in the state of your project.

This is problematic. A person reviewing your changes won't be able to infer what each change signifies and what was their individual purpose. They also won't be able to track how the changes evolved over time and what was the impact of each change.

In times of emergency, you might need to revert back a specific change. This would be impossible if all the changes are stored in a single commit, since that would mean rolling back all the other changes as well. To make sure, you are able to do that, you need to use `git add` judiciously to stage only the files that you need to commit:

```sh
git add <file_1> <file_2> <file_3> ... <file_n>
```

After they are moved to the staging area, you can commit them and continue working on your project while making continuous commits. You can also mentally parse your changes easily using the `git log` command.

## Writing meaningful commit messages

One of the most important things you can do with Git is to write meaningful commit messages. This is the message that will be displayed when you push your changes to a remote repository. There are a lot of reasons why you should write meaningful commit messages:

- You want to easily parse the changes you have made to your project over time.
- You want to communicate the changes with other collaborators and help them understand the changes.
- You want to make sure that the changes you have made are not lost in the event of a conflict.

An insightful and descriptive commit message should be easy & concise while explaining the changes you made and the problem you are trying to solve. Writing your commit message in an imperative tone, like `Fix`, `Update`, `Add`, to help you understand the type of change being made.

We recommend the following type prefixes:

- `feat`: A new feature for the project.
- `fix`: A bug fix that addresses an old issue.
- `chore`: A change that doesn't modify the source code functionality.
- `docs`: Documentation changes for the project.
- `test`: Changes to the test suite for the project.
- `ci`: Changes to the CI configuration or the build scripts for the project.

You can additionally use more prefixes like `style`, `perf`, `revert` but they are out of scope for this chapter. We recommend following [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) as a convention to write commit messages.

Let us take a look at some good examples:

```sh
commit f1ea173d7a52ffbc6560e4e3938da40b41541df0 (HEAD -> master, origin/master, origin/HEAD)
Author: 02 <cocoeyes02@gmail.com>
Date:   Sun Mar 13 03:50:35 2022 +0900

    docs(about): add ramsey/conventional-commits in about page

commit 0ca3c59600dcb6d6b3471236f381b5f117194360
Author: lechbaczynskihtg <98815582+lechbaczynskihtg@users.noreply.github.com>
Date:   Mon Feb 28 11:53:01 2022 +0100

    fix(lang): capitalise Polish language

commit 791a0f2afcc9c6b5c7c72399ec98aee4aa8c4e48
Author: dali546 <35352237+dali546@users.noreply.github.com>
Date:   Thu Jan 20 12:49:02 2022 +0000

    fix: readd impertive wording FAQ
```

The above example is from [conventionalcommits.org](https://github.com/conventional-commits/conventionalcommits.org).

## Avoid committing auto-generated files

While working on a project, chances are high that some files would be auto-generated and re-generated. It can include those data that you wouldn't want to be made available to the public over a version control system. It is always recommended to do a sanity check in this case. To avoid committing those files to Git, you can add them to the `.gitignore` file.

The `.gitignore` file is a file that contains a list of files that you don't want to commit to Git. A standard `.gitignore` file looks like this:

```text
node_modules
build
npm-debug.log
.env
.DS_Store
```

The above content is a standard `.gitignore` file for a NodeJS project. You can add all the filenames for auto-generated files, specific configuration, environment variables, etc. that you don't want to commit to Git.

## Avoid altering Git history

After a commit has been made, pushed to a remote repository and merged to the default branch, it is recommended to avoid altering any published history. In previous sections, we have discussed how Git is a permanent record of your project's history. However, using `git rebase`, you can alter the history of your project. This operation is recommended when you are working on your local machine and on your branch.

It is not a good practise to alter the published Git history because you might loose valuable changes that you have made. These can include past commits which contains valuable information around how the project has evolved. In the next section, we will discuss how to use `git rebase` to alter the history of your project, and how to exercise caution when using it.

## Committing early and often

Git best works when it is used to commit often. Taking the best from the above two suggestions, around commit message guidelines and keeping commits small, you can always work on small chunks and keep committing often. It would allow the collaborators to see your work progress and you can build upon he work that you have done previously.

Git, as a version control system, is responsible for your changes only when they are committed. Committing early and often is a good way to make sure that you are always working on the latest version of your project and can easily mitigate conflicts that might arise.

You should only commit code when a logical change is ready. Splitting a task into multiple smaller tasks will help you make your commits manageable and you can easily see the progress of your work. You should also make sure that your changes are tested thoroughly before you commit them. It becomes even more important when it comes to pushing/sharing your code with others.
