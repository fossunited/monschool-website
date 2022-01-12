---
title: Course Outline
include_in_preview: false
---

So now that you have a basic idea of what self hosting means and the broad list of things that you can self host, it's a good time to go through the course outline. The course as mentions in it's title is _101 Level_ (Basic Level) and we'll gradually pace the course from learning basics of a Linux system, to hosting a webserver, deploying a Python based full stack application and finally learning a bit about debugging and monitoring these systems.

## Outline

## Course Outline

# Mon School Self Hosting 101

## Course Outcomes

At the end of this course, you should be able to:

- Setup a personal server using major cloud providers.
- Be confident in running off the shelves apps like NGINX/Redis/PostgreSQL.
- Learn how to deploy and run Python applications.
- Managing `Day 2` tasks like debugging using metrics and logs.

## Week 1

**Objective**: Setup and configure a VPS.

- Provision a droplet
- Configure the droplet with users, SSH keys
- Learn about package management
- Learn about Files and Directories
- Basics of `tmux`

## Week 2

**Objective**: Deploy a static website with NGINX

- Install a webserver `nginx`.
- Configure NGINX to serve a hello world website.
- Configure NGINX to deploy your personal blog.

## Week 3

**Objective**: Deploy a Python application

- Setup a database using `PostgreSQL`
- Setup and configure the Python application.
- Configure `gunicorn`/`uwsgi` to make it accessible via a webserver.
- Configure NGINX to setup a reverse proxy

## Week 4

**Objective**: Setting up system services

- Learn about `systemd`, `supervisorctl` to setup background services.
- Learn about `cron` to setup periodic jobs.

## Week 5

**Objective**: Logs, Debugging and Fixing

- Find critical information using system logs.
- Basic Linux utilities to find about disk usage, resource usage, network I/O.

## Week 6

**Objective**: Recap + Further Reads

- Reflect upon the course so far/things learnt etc
- Automate certain tasks

**Optional**: Based on the interest in the course we can add a week on *Hosting apps using Docker/Containers*
