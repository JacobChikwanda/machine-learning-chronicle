# Notes on NumPy

## Description

In this playlist, I am coding alongside John Elder. He is teaching me how to work with NumPy arrays in Python. By the end of this playlist, I should have a comprehensive understanding of these data structures.

## Getting Started

To get started, all we have to do is:

1. Ensure we have Python installed on our local machine. We can test this in the terminal by running:

    `python --version`

2. Install `numpy` in our Python virtual environment.

## Notes

Here, I share what I have learned while watching the videos and coding.

### Intro to NumPy - NumPy for Machine Learning 1

#### What is a NumPy array?

From this video, I learned that a NumPy array is simply a structure that stores information. John opened by explaining a list, which is a data structure in Python that helps us easily store data of all types.

```python
my_list = [
    {
        "name": "Jacob",
        "country": "Zambia"
    },
    {
        "name": "Mark",
        "country": "USA"
    }
]
```

The above structure helps us store a dictionary of information about people. It is suitable for small records. A question to help understand lists is the following:

#### Can a list handle billions of data?

I did a quick search on ChatGPT, and this is what I found:

> "In Python, a standard list can handle a large amount of data, but it may not be efficient or practical for billions of items due to memory constraints and performance issues."

From this, I've realized that while it's not impossible to work with lists and handle billions of records in Python, it’s often inefficient. I wouldn't want to create a program that makes users wait for days—after all, no one has time for that!

**What is the solution?** NumPy! It's one of the options among others.

#### NumPy Failed to Convert

I made an interesting discovery while learning:

1. **We can convert a list to a NumPy array.**

    It seems we can convert a Python list to a NumPy structure. However, if your list does not contain uniform elements, an error is thrown. So, you want to ensure your list has a consistent structure inside.

2. **NumPy converts types.**

    I conducted an experiment where I had a list containing two data types: strings and numbers. NumPy converted everything to strings.