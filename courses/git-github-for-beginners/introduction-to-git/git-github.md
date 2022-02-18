---
title: Git Github
include_in_preview: false
---

In the previous chapter, we learnt how Git provides fast and flexible version control for multiple collaborators. With Git, we can set up multiple parallel branches for development, develop our code independently, and merge the changes back to the main branch after a review. Collaborators working on their local copy can pull all the latest changes from the main branch, and push their changes back to their branches whenever they are ready. They can also compare the differences between the old and new files to see what has changed in a completely distributed structure.

However contrary to standard ways to share data, like using Google Drive or Dropbox, Git cannot automatically sync changes across multiple computers. All the updates made to local repositories need to be pushed to a remote repository and all the changes need to be pulled from the same repository as well. This brings in the need for hosting and running your Git server, where the collaborators can take an SSH session to the server and push and pull their changes. It becomes useful for all the collaborators to use this to push or pull updates. However, this process is time-consuming, error-prone and tedious. 

This is where GitHub comes in. GitHub is a web-based cloud hosting service for version control using Git. It is a free service that provides a simple interface for sharing code, collaborating with others, managing your projects and more. GitHub can permanently host a remote copy of the project, and it can be accessed from any computer with an Internet connection. All of the developers can push new changes to GitHub, and propose them for review, or pull new changes. This allows GitHub to act as an intermediary hub for collaboration, and to share code with others.

## Why use GitHub?

GitHub is the most popular code collaboration software, helping millions of software development teams across the world to collaborate and share. With GitHub, developers can build code, track and propose changes, track their progress and tasks, run software pipelines to release new versions, publish documentation, and more. GitHub is essentially beneficial for even non-developers, as it can be used to collaborate on documentation, design, strategy planning, and more. GitHub is also preferred for individual developers (it's free) as it allows them to freely build their projects, create a portfolio, and share their work with others.

There are several reasons why you should use GitHub. From a software development perspective, here are a few reasons:

- GitHub is free for individuals and organizations as long as their code is open source.
- GitHub boasts of the largest community of open source developers and projects. GitHub is usually the first choice for developers looking to open-source their projects and collaborate with others.
- GitHub provides a handy task-based workflow that makes it easy to track progress. Contributors can use GitHub to provide feedback, share bugs, request new features, and discuss project ideas.
- GitHub allows you to receive feedback and reviews from other developers on your changes. This is a great way to learn from each other's work and to improve your code.
- GitHub Actions is a powerful tool that allows you to automate tasks, set up software pipelines and releases. It can be used to run your tests, build your code, and deploy your code to production.

Apart from being a general Git-based provider, GitHub features many extended products and features making it a powerful tool to develop and collaborate on. If you are a student, you can use GitHub Student Developer Pack to avail yourself of tools and services (that are otherwise paid), completely free for a specific period. Today, GitHub is fueled by an ever-growing community of users and contributors, and this is what propels GitHub to be the most popular code collaboration software.

## GitHub terminology

To understand GitHub better, it is necessary to understand the terminology used in GitHub. Most of the terms used in the terminology would be better explained in the following chapters and sections. As a reader, don't fret out if you don't understand a term; We will uncover all the terms herewith practical demonstration and examples.

- **Repository**: A collection of files and folders that are used to store and share code. A repository can be created by a user or organization.

- **Issues**: A list of issues that are associated with a repository. These issues can be feature requests, bug reports, documentation updates, or any other issues that are associated with the repository. Issues are used for communication between the repository owner and the users or contributors.

- **Pull requests**: A request to merge changes from one branch into another. Pull requests are used by collaborators or general contributors to propose changes to different parts of the code and require review before they are merged.

- **Actions**: A set of configuration files that are used to automate tasks, set up software pipelines and releases. After creating an action, it can be configured automatically to run on every commit, every push, or every pull request and denote the status of the operation.

- **README**: A file that is used to describe the project and its purpose. It's usually the first file that is created in a repository and is used for general-purpose documentation.

- **LICENSE**: A file that is used to specify the license of the project. All open-source projects should have a license tagging their code to denote the terms of use and sharing of the code.

- **Releases**: A way to download the code & package associated with the project. Releases are used to share the packaged versions of the project with the users on every tag.

- **Fork**: A copy of a repository that is created by a user. A fork is a copy of the original repository that is created by a user and lives on the user's own GitHub account.

- **Packages**: A platform to host and manage the packages associated with the project. It can include libraries, modules, containers, and other software components that can be downloaded directly from GitHub.

- **Environments**: A deployment target for the project. An environment is a specific version of the project that is deployed to a specific location, like a staging or production environment.

You can further have a look at the [GitHub glossary](https://docs.github.com/en/get-started/quickstart/github-glossary) to get a better understanding of the terms used in GitHub.

<!-- Add a picture of a GitHub repository showing all of the above terms -->

## What is the difference between Git and GitHub?

While both of these terms are used interchangeably, both of them are entirely different. The term `Git` is used to refer to the version control system that is used to store and share code. The term `GitHub` is used to refer to the web-based cloud hosting service that is used to host and manage code. GitHub is designed as a Git repository hosting service, and share your projects outside of your local computer. GitHub also expands over the essential functionality of Git to provide a more robust and flexible task-management, collaboration, and continuous integration solution.

Though GitHub provides most of these services for free, GitHub also offers pro and enterprise plans for its users, who are interested in a tightly integrated and secure solution. It includes more private repositories (for internal teams), security features, and more. Git on the other hand is (and will always be) a free and open-source solution to version control your projects.

## Conclusion

In a standard workflow, you essentially fork a repository, create a copy of it on your local machine, create a branch and push your changes before making a pull request. You can then have the changes reviewed and merge them into the original repository. GitHub facilitates an easy solution to storing and collaborating on code, and it is the preferred way to share code with others.

GitHub also offers GitHub Desktop — A desktop application that is used to manage your GitHub account, repositories, and more. It is also offered as an alternative to using a command-line interface to manage your Git operations. Apart from all this, GitHub has heralded quality control among development teams. Now the changes don't need to be reviewed before the release and integrated once but can be continuously developed and integrated with each push. It also allows different teams to share their feedback on code changes, giving them extra flexibility and encouraging collaboration.

In the upcoming chapter, we will understand how you can collaborate with others using Git & GitHub. We will learn how you can set a repository up for a project, and how you can create a workflow to push and pull changes to and from GitHub using Git. Lastly, we will also cover how you can publish a simple package to GitHub and open-source the solution.
