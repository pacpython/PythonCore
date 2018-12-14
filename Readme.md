# Welcome to Python World
#### What is Python?
* Python is a popular programming language. It was created in 1991 by Guido van Rossum.

#### It is used for:
1. web development (server-side),
2. software development,
3. mathematics,
4. system scripting.

### Download Python
https://www.python.org/downloads/

### Download VS Code
https://code.visualstudio.com/download

### Python extension for Visual Studio Code
https://marketplace.visualstudio.com/items?itemName=ms-python.python

### Check Python Version
```python
$ python --version
```

### PowerShell
```bash
[Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\Python27","User")
```


## First Python Program
```python
mgs = "Hello World!"
print(mgs)
```

### Run Program
```bash
python HelloWorld.py
```

## The Python Command Line
```bash
$ python
>> print("Hello, World!")
>> exit()
```

* Python uses indentation to indicate a block of code. Python will give you an error if you skip the indentation:

#### Right
```python
if 5 > 2:
  print("Five is greater than two!")
```

#### Wrong
```python
if 5 > 2:
print("Five is greater than two!")
```

#### Code Comment
```python
#This is a comment.
print("Hello, World!")
```

#### Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
* A variable name must start with a letter or the underscore character
* A variable name cannot start with a number
* A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
* Variable names are case-sensitive (age, Age and AGE are three different variables)

#### Python Operators
* Arithmetic operators
* Assignment operators
* Comparison operators
* Logical operators
* Identity operators
* Membership operators
* Bitwise operators

#### Python Collections (Arrays)
There are four collection data types in the Python programming language:
* List is a collection which is ordered and changeable. Allows duplicate members.
* Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
* Set is a collection which is unordered and unindexed. No duplicate members.
* Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.



### Format Document 
(⇧ ⌥ F) 


### Debugging
A debug toolbar appears along the top with the following commands from left to right: continue (F5), step over (F10), step into (F11), step out (⇧F11), restart (⇧⌘F5), and stop (⇧F5).
* https://code.visualstudio.com/docs/python/python-tutorial




### Next steps
* [Linting](https://code.visualstudio.com/docs/python/editing) - Enable, configure, and apply a variety of Python linters.
* [Debugging](https://code.visualstudio.com/docs/python/debugging) - Learn to debug Python both locally and remotely.
* [Unit testing](https://code.visualstudio.com/docs/python/unit-testing) - Configure unit test environments and discover, run, and debug tests.
* [Settings reference](https://code.visualstudio.com/docs/python/settings-reference) - Explore the full range of Python-related settings in VS Code.

