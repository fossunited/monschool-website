---
title: Designing with Classes
include_in_preview: false
---

A well designed software is flexible to accomodate the changing requirements. In this lesson, we'll how to design software using classes to bring that flexibility.

## Multiple Implementations

One of the way to make software flexible is to allow multiple implementations of an interface.

Let's examine the following example.

```{.python .example}
def wordcount(filename):
    contents = open(filename).read()
    return len(contents.split())

print(wordcount("three.txt"))
```

This implementation counts the number of words given a filename. We may not be able to use the same function if we have a URL instead of a file.

We could make the function more flexible by making it take a file object instead of a filename.

```{.python .example}
def wordcount(fileobj):
    contents = fileobj.read()
    return len(contents.split())

print(wordcount(open("three.txt")))
```

It is almost the same code, except it takes a file as argument instead of the filename.

Now that the function takes a file object as argument, we can pass any file-like objects as arguments. If you look at the code of `wordcount`, it is calling the `read` method on the fileobject. So any object that supports `read` method can fit in here.

It turns out that the HTTP response is a file-like object and we can use that to count the number of words at a given URL.

```{.python .example}
def wordcount(fileobj):
    contents = fileobj.read()
    return len(contents.split())

# print the number of words in the contents of file
print(wordcount(open("three.txt")))

# print the number of words in the contents of a URL
from urllib.request import urlopen
response = urlopen("https://anandology.com/tmp/hello.txt")
print(wordcount(response))
```

The response object returned by the `urlopen` function is a file-like object and it supports `read` and `readlines` methods.

We could also write our own class that supports the `read` method and objects of that class will work with the `wordcount` function.

```{.python .example}
def wordcount(fileobj):
    contents = fileobj.read()
    return len(contents.split())

class FakeFile:
    def read(self):
        return "a b c"

f = FakeFile()
print(wordcount(f))
```

## Class Inheritance

In the above section, we've seen how to we can use different implementations with the same function, as long they all of them implement the required methods. While this works well for small cases, it becomes very fragile when attempting with classes having multiple methods.

Class Inheritance provides a systematic way to handle multiple implementations while allow resuing some of the code between them.

Before we get into the disucssion of how to model classes using inheritance, let's understand how it works.

```{.python .example}
class Calculator:
    def add(self, a, b):
        return a+b

    def mul(self, a, b):
        return a*b

class ScientificCalculator(Calculator):
    def exp(self, a, b):
        return a**b

    def square(self, a):
        return super().mul(a, a)

calc = ScientificCalculator()
print("2 + 3 = ", calc.add(2, 3))
print("2 * 3 = ", calc.mul(2, 3))
print("2 ** 3 = ", calc.exp(2, 3))
print("square(3) = ", calc.square(3))
```

In the above example, `ScientificCalculator` is


### Example: Charts and Dashboard

Let's take an example of rendering charts and dashboard. There will be multiple charts like barchart, piechart etc. and a dashboard can have multiple charts in it. We'll use classes to model this and make the implementation flexible enough to support other types of charts in the future.

In our implementation, charts and dashboards are rendered to html. The html of dashboard contains the rendered html of each chart along with some more details of the dashboard.

This is implemented as two files, `chart.py` containing the implementation of charts and dashboard and a `main.py` that creates a bunch of charts and creates a dashboard using them.

Please note that in this example, all the charts render only dummy HTML.

```{.python .example .multi-file}
=== main.py
from chart import BarChart, LabelledBarChart, PieChart, Dashboard

data = [1, 2, 3]
charts = [
    BarChart(data),
    LabelledBarChart(data, "Awesome Chart"),
    PieChart(data),
]
dashboard = Dashboard("My Dashboard", charts)
print(dashboard.render())

=== chart.py
"""Python library to create charts and dashboards.
"""

class Chart:
    def render(self):
        """Renders the chart as HTML.
        """
        pass

class BarChart(Chart):
    def __init__(self, data):
        self.data = data

    def render(self):
        return '  <div class="barchart">...</div>\n'

class LabelledBarChart(BarChart):
    def __init__(self, data, label):
        super().__init__(data)
        self.label = label

    def render(self):
        header = f"  <h2>{self.label}</h2>\n"
        return header + super().render()

class PieChart(Chart):
    def __init__(self, data):
        self.data = data

    def render(self):
        return '  <div class="piechart">...</div>\n'

class Dashboard:
    def __init__(self, title, charts):
        self.title = title
        self.charts = charts

    def render(self):
        html = ""
        html += f"<h1>{self.title}</h1>\n"
        html += '<div class="dashboard-charts">\n'
        for c in self.charts:
            html += c.render()
        html += '</div>\n'
        return html
```

While the chart library is designed with just 3 charts and a dashboard, it is flexible to accomodate new kinds of charts. In the following example, we'll create an additional type of chart called Table and add it to the dashboard.

```{.python .example .multi-file}
=== main.py
from chart import Chart, BarChart, LabelledBarChart, PieChart, Dashboard

class Table(Chart):
    def __init__(self, data):
        self.data = data

    def render(self):
        return '  <div class="table">...</div>\n'

data = [1, 2, 3]
charts = [
    BarChart(data),
    LabelledBarChart(data, "Awesome Chart"),
    PieChart(data),
    Table(data)
]
dashboard = Dashboard("My Dashboard", charts)
print(dashboard.render())

=== chart.py
"""Python library to create charts and dashboards.
"""

class Chart:
    def render(self):
        """Renders the chart as HTML.
        """
        pass

class BarChart(Chart):
    def __init__(self, data):
        self.data = data

    def render(self):
        return '  <div class="barchart">...</div>\n'

class LabelledBarChart(BarChart):
    def __init__(self, data, label):
        super().__init__(data)
        self.label = label

    def render(self):
        header = f"  <h2>{self.label}</h2>\n"
        return header + super().render()

class PieChart(Chart):
    def __init__(self, data):
        self.data = data

    def render(self):
        return '  <div class="piechart">...</div>\n'

class Dashboard:
    def __init__(self, title, charts):
        self.title = title
        self.charts = charts

    def render(self):
        html = ""
        html += f"<h1>{self.title}</h1>\n"
        html += '<div class="dashboard-charts">\n'
        for c in self.charts:
            html += c.render()
        html += '</div>\n'
        return html
```

As you can see the new table chart that we've created was seemlessly added to the dashboard.

Object oriented programming is an interesting way to create extensive software. This lesson provided a glimpse of how to design software with classes.