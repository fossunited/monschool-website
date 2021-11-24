---
title: Handling dependencies in rust-lang
---

Rust has seen growing adoption, leading to more libraries written in the language, which ofcourse lead to the creation of an entire ecosystem of packages, aka crates, being released on a dedicated platform called [crates.io](https://crates.io). While developing a crate of your own, you may import/depend on another by including it in `Cargo.toml`. This chapter will clarify a few informative facts about including dependencies in your project.