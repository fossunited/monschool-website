---
title: Using tmux
include_in_preview: false
---

`tmux` is a terminal multiplexer, which allows you to create and persist "shell sessions" on the server. This is helpful if you have to run a long running command and don't want the process to be killed if your SSH connection is abrupted for any reason. This is also helpful if you have more than 1 person logging in to your server and you together need to work on the same session.

`tmux` allows you to _attach_ multiple shells to a same terminal session. That means, you can open a `tmux` window, split into 4 parts (_panes_) and run different commands on each of them. The actual session is just one, but `tmux` creates 4 on top of it. 

Let's create a new session with:

```
tmux
```

You'll be logged into to your current user account. `tmux` is controlled using what is called as **Modifier Key** (Mod). The default hotkey for that is `Ctrl+b`. This combination will be referred as `mod` in the below commands:

### Panes

- `mod %`: To split a window vertically.
- `mod "`: To split a window horizontally.
- `mod [`: To add a scrollbar to current pane.

You can move around the panes with `mod + Right/Left/Up/Down` arrow keys.

![img](./img/tmux.png)

### Windows

- `mod c`: Create a new window.
- `mod p`: Switch to previous window index.
- `mod n`: Switch to next window index.

### Attaching/Deattaching

- `mod d`: To deattach from the current `tmux` window.
- `tmux ls`: To list all the `tmux` active sessions.
- `tmux a -t 0`: To attach to a particular `tmux` session (`0` index in this case).

## Resources

You can explore some handy cheatsheets like https://tmuxcheatsheet.com/ and https://devhints.io/tmux for more commands.
