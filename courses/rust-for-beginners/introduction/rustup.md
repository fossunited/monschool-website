---
title: First spin, Playground and Rustup
---

Test driving rust-lang with Playground and installing the rust compiler toolchain -rustc, cargo and more using Rustup.

We have learnt a bit about how rust-lang came to be and it's community, in this lesson, let's explore the language and take it for a spin. Log onto https://play.rust-lang.org to checkout the Playground, a web-app that emulates a rust compiler and lets you compile simple rust programs, enough for a beginner to learn the syntax of the language.

As you can see, we have a program that when we press "Run" will print "Hello, World!" to the adjoined output panel. Let's focus on the code for a minute.
```rust
fn main() {
    println!("Hello, world!");
}
```
If you are familiar with a langue such as c, cpp or python, this might be something you could easily figure out. `fn` is the keyword to define functions with, similar to `def` in python or `func` in golang, `main` is the function's name, defined such that it takes no arguments `()`, and the body of the function is just a statement that looks like a function to print the given string "Hello, World!" to screen. Well, that statement is infact a macro and that's where we have to start unpacking a lot, pun intended :smirk:

Now that I have thoroughly bored you with a write up, let's understand how we can tweak the playground to our liking from this [quick YouTube tutorial](https://www.youtube.com/watch?v=-lYeJeQ11OI&t=36s).

## Installing rust-lang with `rustup`

Writing rust in the browser is cool and all, but a whole lot of the libraries and facilities within the langauge do not run properly in such an environment, which is why we need to install the compiler and other tools that come with it on a system of our own. This can be easily done by logging onto https://rustup.rs and following the instructions there, else you could also follow this [handy tutorial](https://www.youtube.com/watch?v=2hY7Uib2UDM). If you are using Windows or another non-linux OS, you may have to set PATH or do some other tweaking and fixing, please look-up a tutorial specific to your OS of choice in that case.

## Compiling programs locally with `rustc`

If you have followed either of the above suggested steps, you will have installed the rust compiler called `rustc`, the rust package management utility `cargo` and a whole load of other tools that'll soon become very useful. To get started, let's print "Hello, World!" to screen by doing the following:
1. Create and open a file "hello.rs" and copy-paste the program from the playground example, save the file.
2. From within the same directory as the file, run the rust compiler with the file as input:
```bash
rustc hello.rs
```
3. Depending on the OS, you will endup having generated an executable, on linux it will be named "hello". Run it, this step might be different on other OSes:
```bash
./hello
```

### Building rust crates with `cargo`

We have experimented with writing, compiling and running rust-lang with help of the rust-compiler. Now there's a quicker and much more cleaner way to deal with bigger rust programs which may require more than one source file and even some dependencies outside of the standard library. That would be made possible by creating a rust crate, the term rustaceans use to refer to the source code that can be built into libraries and binaries with `cargo`. A walkthrough of the same is presented in the [video for installing rustup at 1:40](https://www.youtube.com/watch?v=2hY7Uib2UDM&t=100s). 

The differences with this approach are:
- Writing crates can be a great way to manage external dependencies
- Code is placed in `src/` and 
