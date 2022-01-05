---
title: Introduction to HTML Document
include_in_preview: false
---

# HTML Document

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/0oyaXavKtrE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## What's HTML Document
- A web document is a text file usually with .html or .htm extension
- It usually contains HTML, Hyper Text Markup Language. It's a simple language, that is used to do
    - Attach meaning to the content in the text
        - Are these paragraphs
        - Is this a table
        - Is this a list
    - Strucutre the text
        - Is this header
        - Is this style
    - Format them
        - make the text strong or bold
        - break the line
    - Linking between the documente etc
        - Add link to another document
    - Adding or embeding media
        - Add an image
        - Embed a youtube iframe
- All this is usually achived by using HTML tags
- An HTML tag will usually contain 
    - An opening tag
    - Closing tag
    - Content
    - Attributes and values
For example:
    `<p style="color: #8ebf42;"> This is my first paragraph </p>`
Here the
    - `<p .....>` Is opening tag - says when the paragraph starts
    - `</p>` Is called closing tag - says when the paragraph ends
    - `style` is attribute
    - `"color: #8ebf42;"` is the value of the attribute

Some tags may not require an end tag. As they may not have any enclsoing content. Like  like break tag
    - `<br/>` - breaks the line

Also tags can be nested. It means you can use tags inside another tag content. For example bold tags inside paragraph tags. This gives immense power to format the document.


Now that we know this. Let's create a simple HTML document. Let's call `my_first.html`

## Simple HTML Document
- So open Gedit or any text editor. 
- Create a file called "my_first.html" and save it to your computer. Remember where you saved it
- You can add any text you want and save it.
- In this example we will take three paragraphs from the book Pride and Prejudice

```text
Pride and Prejudice, by Jane Austen.

From Chapter 3

Not all that Mrs. Bennet, however, with the assistance of her five daughters, could ask on the subject, was sufficient to draw from her husband any satisfactory description of Mr. Bingley. They attacked him in various ways; with barefaced questions, ingenious suppositions, and distant surmises; but he eluded the skill of them all; and they were at last obliged to accept the second-hand intelligence of their neighbour, Lady Lucas. Her report was highly favourable. Sir William had been delighted with him. He was quite young, wonderfully handsome, extremely agreeable, and, to crown the whole, he meant to be at the next assembly with a large party. Nothing could be more delightful! To be fond of dancing was a certain step towards falling in love; and very lively hopes of Mr. Bingley’s heart were entertained.

“If I can but see one of my daughters happily settled at Netherfield,” said Mrs. Bennet to her husband, “and all the others equally well married, I shall have nothing to wish for.”

In a few days Mr. Bingley returned Mr. Bennet’s visit, and sat about ten minutes with him in his library. He had entertained hopes of being admitted to a sight of the young ladies, of whose beauty he had heard much; but he saw only the father. The ladies were somewhat more fortunate, for they had the advantage of ascertaining from an upper window, that he wore a blue coat and rode a black horse.

An invitation to dinner was soon afterwards dispatched; and already had Mrs. Bennet planned the courses that were to do credit to her housekeeping, when an answer arrived which deferred it all. Mr. Bingley was obliged to be in town the following day, and consequently unable to accept the honour of their invitation, etc. Mrs. Bennet was quite disconcerted. She could not imagine what business he could have in town so soon after his arrival in Hertfordshire; and she began to fear that he might be always flying about from one place to another, and never settled at Netherfield as he ought to be. Lady Lucas quieted her fears a little by starting the idea of his being gone to London only to get a large party for the ball; and a report soon followed that Mr. Bingley was to bring twelve ladies and seven gentlemen with him to the assembly. The girls grieved over such a number of ladies; but were comforted the day before the ball by hearing, that instead of twelve, he had brought only six with him from London, his five sisters and a cousin. And when the party entered the assembly room it consisted of only five altogether; Mr. Bingley, his two sisters, the husband of the eldest, and another young man.


Got from Project Gutenberg - https://www.gutenberg.org/files/1342/1342-h/1342-h.htm#link2HCH0003

--


```

## How to view it
- Now open this file `my_first.html` in a browser. 
- You can see the text but the format is all over the place

## Next
- That is because we have not added any stricutre or meaning to the text
- Once we add some tags to define the structure, it should look better
- We will do that next

