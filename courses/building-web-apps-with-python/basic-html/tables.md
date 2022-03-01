---
title: Creating Tables
include_in_preview: false
---

# Tabular data
Tabular data or simple table are main part of any document. HTML gives you tags to represent a table.

## What are tables
- Table can have header, body and footer
- Table body can have rows
- Usually header and footer will have only one row
- Each rows can have cells

```{.html .example}
<table>
    <thead> </thead>
    <tbody> </tbody>
    <tfoot> </tfoot>
</table>
```

## How to add header
`thead` can have a row, denoted by `tr`. And the row inside thead can have cells `th`.

```{.html .example}
<table>
    <thead> 
        <tr>
            <th>Name</th>
            <th>Age</th>
        </tr>
    </thead>
    <tbody> </tbody>
    <tfoot> </tfoot>
</table>
```

## How to add value rows and cells
`tbody` can have many rows and cells  - here called `td`, along with the values.

```{.html .example}
<table>
    <thead> 
        <tr>
            <th>Name</th>
            <th>Savings</th>
        </tr>
    </thead>
    <tbody> 
        <tr>
            <td>Raj</td>
            <td>20</td>
        </tr>
        <tr>
            <td>Asif</td>
            <td>22</td>
        </tr>
        <tr>
            <td>Rebeka</td>
            <td>21</td>
        </tr>
    </tbody>
    <tfoot> </tfoot>
</table>
```


## How to add footers

You can ad footer just like header. Usually there will be only one row of it

```{.html .example}
<table>
    <thead> 
        <tr>
            <th>Name</th>
            <th>Savings</th>
        </tr>
    </thead>
    <tbody> 
        <tr>
            <td>Raj</td>
            <td>100</td>
        </tr>
        <tr>
            <td>Asif</td>
            <td>25</td>
        </tr>
        <tr>
            <td>Rebeka</td>
            <td>25</td>
        </tr>
    </tbody>
    <tfoot> 
      <td>Total</td>
      <td>150</td>
    </tfoot>
</table>
```

Here we have used the footer to do summary. But there is no such requirement. Its left to your creativity. You don't need to have them if its not required.

## What more

Sometime you might want to combine two rows or two cells. They can be achived using `colspan`or `rowspan`.  Search for them in Google and see how you can use them.