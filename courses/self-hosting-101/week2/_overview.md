---
title: Overview
include_in_preview: false
---

## Actionable Tasks

- [ ] Install NGINX
- [ ] Editing default `index.html`
- [ ] Setting up a sitename (vhost) `blue.user.monschool.net`
- [ ] `red.user.monschool.net` from a `.git` repo.
  - [ ] symlink
  - [ ] nginx config
- [ ] Configure SSL for `red.user.monschool.net`
- [ ] Project: Setup Hugo
  - [ ] https://gohugo.io/getting-started/installing/

## Tests

- [ ] curl `<public-ip>:80` from outside
- [ ] verify the content of response body
- [ ] Verify the site is running
  - [ ] check if symlink is proper
- [ ] Check file permission not belonging to root user

## What is NGINX

NGINX is a popular web server which is used to serve static assets, web applications and also act as a load balancer. Imagine you have created a small website for yourself but you want the world to see it. How do you do that? You need to _serve_ these assets via a webserver. All these popular tools like Netlify etc also use their own versions of a web server.

## Installing

```
sudo apt-get install nginx
sudo systemctl enable --now nginx
```

### Verify it's running

```
curl localhost:80
```

## Setup a static website

Let's create a mini HTML file to showcase how to configure NGINX to serve an HTML file.

### Creating the file

TODO: Use nano and give links for `vim`.

We'll use the knowledge of `vim` from previous lesson and create an `index.html` file on the server.

```
`/var/www/html/`
mkdir ~/website && cd ~/website
vim index.html
```

<TODO: Add basic index.html structure>

## Configure NGINX

<TODO: Take some sample from nginxconfig.io>

### Verify it's accessible from outside world

If you're interested in making this website available to the world, you'll need to explicitly allow access to it.
Since the website is running on port 80, we need to configure a firewall rule which allows all IPs to connect to it.

<TODO: Firewall steps>

### Configure SSL

<TODO: Certbot steps>

