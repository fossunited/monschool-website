---
title: Why Version Control System
include_in_preview: false
---

Software development is a rapidly changing field and it is always difficult to maintain a single source of truth across teams. With complex code development, it is difficult to keep track of changes and to know what is the current state of the code. With the lack of proper software to control different versions of the code, it is difficult to collaborate across teams and developers and track the functional changes that are being made to the code. 

This is where Version Control System comes into play. Version Control Systems allows developer teams to efficiently track, manage and commit changes to their code without having to worry about overwriting the code written by other developers. It tracks every modification made to the source code in a special kind of database. It allows you to identify what changes were made in each version, tag those changes in a release, identify the developers who worked on a particular change and even fix those mistakes that have crept in the code, by reverting to a previous version.

## Why should we care?

Let's use a hypothetical scenario to understand the problem better — You are a software developer working on a project where you are the only person working on it. A single file contains all the source code and you are supposed to track all the new changes being made by saving different "versions" of it. As you make the changes to your code, you will save different "versions" of the file, every time you make some change, and in essence, it will create a lot of mess.

In a real-world scenario, the problem becomes even more complex — Multiple developers are collaborating to build projects together. The entire project would be divided into multiple files and directories and everyone will be making a lot of changes over time. In this scenario, you cannot save all the versions manually since it will be tedious and time-consuming. Furthermore, you will never be able to pick a certain file and identify who made the changes, the developer responsible for it, and how does it differ from the previous or the next version.

You need something to fix the conflicts that may arise when you overwrite someone else's code. You need a way to ensure that if your changes break something you can go back to a previous version. You need to ensure that all the changes being made (and their associated metadata) are being tracked and accounted for.

In a Version Control System, we acknowledge that there is only one project and hence only one version is present. Everything else, including past versions, are stored inside the Version Control System which can be pulled out anytime. Everyone on the team is free to work on anything at any time, given the fact that a Version Control System will merge all their changes to one version. Additionally, every developer would need to write what has changed in every change and it will help understand how the project has evolved between versions.

Using a Version Control System isn't just a skill — It's a necessity that will arise from time to time, not just when you are writing some code. Using it effectively can make you a better collaborator and this is what the course is about — helping you get better at it with the help of Git & GitHub. There are tools built to do this job for you, so why not use them?

## Types of Version Control Systems

There are two main types of version control systems: Centralized and Distributed Version Control Systems.

Centralized Version Control Systems is based on the idea that there is always a single "central" copy of your code on a server. Developers are supposed to "commit" or add their changes to the central copy. Distributed Version Control Systems, on the other hand, is based on the idea that every developer "clones" a copy of the code, which has all the metadata as the original and then commits their changes to the copy Distributed Version Control System is regarded as more modern, faster and lesser prone to errors. It is also inherently complex and requires some time to understand and wrap our heads around.

### Centralized Version Control Systems

Centralized Version Control System is based on a client-server model. The server serves as the main repository where all the versions of the code are presented. To get the code from the master main repository, the client needs to communicate with the server and get a local copy of the code. The client then makes changes to the code and commits those changes to the server. The server then merges those changes with the other changes that have been made by other clients and stores the merged changes in the main repository.

Though the whole concept looks straightforward in plan, it has multiple problems in execution. The first problem is that the central server represents a single point of failure. If the server goes down, all the version changes are lost along with all the metadata and the individual snapshots that developers have locally. Centralized Version Control Systems are also not suitable for large-scale projects because of multiple conflicts while merging the changes. Developers also need to communicate with the server every time they make a change, which is time-consuming and tedious.

<!-- TODO: Add a diagram depicting CVCS -->

### Distributed Version Control Systems

Distributed Version Control Systems on the other hand is based on the idea that every developer has a copy of the code and commits their changes to their copy. In a Distributed Version Control System, every developer can work on their own copy and it can contain the entire history or version of the code along with the metadata. This is a more modern and efficient way of version control. It empowers the developers to work locally and collaborate effectively after their changes are ready.

From a collaboration perspective, a Distributed Version Control System is more flexible and can be used for large-scale projects. It is also more efficient than a Centralized Version Control System because it doesn't require the server to be online all the time. It also doesn't require the developers to communicate with the server every time they make a change. If a particular server that was being used for collaboration dies, any of the client repositories can be copied back up to the server to restore it. Every clone is a full backup of all the data. 

<!-- TODO: Add a diagram depicting DVCS -->

## Benefits of Version Control System

Using a Version Control System has plenty of advantages. Some of them include:

- **Collaboration**: Using a Version Control System, you can easily collaborate with other developers without having to send your code over manually or asking someone else to integrate it. You can commit your changes, ask for reviews and work freely — all without worrying about conflicts. Collaboration using Version Control System happens to be one of the biggest drivers in the adoption of open source technology and the rise of open-source contributions since it allows folks from all over the world to contribute to the projects easily and effectively.

- **Backup**: With a Version Control System, you can backup your code every time a user copies your code. It allows them to create a backup of your code and then restore it if they ever need to. This is a great way to ensure that you don't lose your work if you accidentally delete your code or the server where it's hosted, goes down. In a software development team, every member will have a full-blown version of their code along with the entire history on their disk.

- **Tracking changes**: With a Version Control System, you can track every change made to your code. You don't have to worry about the associated metadata, which might include the developer who made the change, the version number, the date of the change, files changed etc. You can easily identify the changes made to your code and see the history of the code. In case of an event, where a developer responsible for a particular change has to be identified, you can easily use the metadata to identify the developer and the associated changes.

- **Restoring previous version**: One of the greatest advantages of using a Version Control System is that you can easily restore your code to a previous version. This is especially useful when you have tracked an anomaly in your code and you need to revert to a previous version of the code. It means that with a Version Control System, you can never mess up and this gives you added confidence while working on your project.

## Conclusion

The usage of the Version Control System is very essential in software development today. With the project being more and more complex, and development teams rising in size, it is becoming more and more important to have a version control system in place. This will help in managing the entire project and ensuring that efforts are not being duplicated and the code is not being overwritten.

Today Version Control System is becoming more and more crucial for project development where collaboration is paramount. It also gives enormous potential to you as a developer, to the point that it can be used even for solo or non-technical projects. In the next chapter, we will look at Git and what is its relevance in software development and to our overall course.
