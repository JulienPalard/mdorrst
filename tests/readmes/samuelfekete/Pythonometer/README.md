# Pythonometer 
*A tool for measuring and improving Python skills*


## What is Pythonometer?
Pythonometer is tool for measuring how good someone is at Python. 

The goal of this project is to have a comprehensive set of code questions
covering all areas of Python, so that a Pythonometer score will
accurately represent how good someone is at python, and that anyone practicing for the
sake of getting a good score will actually become very good at coding in Python.

## Usage
It's really easy to install and use:
```
pip install pythonometer
pythonometer
```


## Status
This project is currently at prototype stage, with just a small number of questions.


## Contributing 
Contributions are very welcome, as it would take a lot of work to fulfill the ambitious
goal of covering as much of Python as possible. 

It's very easy to contribute questions, just create a class that inherits from Question.
A question must have three methods: one to get the question text, one to check if an
answer is correct, and one that returns a valid answer. All questions are automatically tested
by supplying the question with its own answer.


### Guidelines for adding questions.
The goal of this project is to test Python skills and not puzzle-solving skills.
The idea is that a user practising would benefit from repeating the same questions,
by building muscle-memory for generic Python tasks, and improve coding speeds
by reducing the need to look things up.

- Questions should be simple and clearly defined. 
- Each question should focus on one very specific piece of knowledge, and require the
minimum amount of code that is needed to demonstrate that bit of knowledge.
- All expected answers should be in pure code (no questions expecting answers in English).
This ensures the complete objectivity of the automated score (the code can still be judged
subjectively from the answer log), and it also serves to make it useful for a user who
is repeating questions to practice.
- Each question should have a title. This is a short sentence summarizing the question.
It should appear on its own line at the beginning of the question text. It should also be
the docstring for the question class.
- The docstring should also link to the page in the Python docs that document the question.

The questions are organised like the Python documentation, with each module corresponding to a 
page in the docs. This will make it possible to check how much of the Python language is being tested.
