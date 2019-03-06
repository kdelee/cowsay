# cowsay
---

cowsay for GNU/Linux was initially written in perl by Tony Monroe (tony@nog.net), with suggestions from Shannon Appel (appel@CSUA.Berkeley.EDU) and contributions from Anthony Polito (aspolito@CSUA.Berkeley.EDU).


This project is a fork of the `cowsay-python` project by Vaasu Devan S:
- [https://pypi.org/project/cowsay/](https://pypi.org/project/cowsay/)
- [https://github.com/VaasuDevanS/cowsay-python](https://github.com/VaasuDevanS/cowsay-python)


The updates in this code is mainly to make the implementation more `pythonic`. It will work with Python3.6+


## Installation
```bash
# Clone the repository
git clone https://github.com/rashid-nhm/cowsay.git

# Copy the cowsay.py file to current directory
mv cowsay/cowsay.py ./

# Delete the directory
rm -r cowsay/
```

## Usage
```python
>>> import cowsay
>>> cowsay.say("Hello")
```

---
Note: Try not to do the following. It pollutes the namespace and is not recommended
```python
from cowsay import *  # DO NOT DO THIS
```
---

## Functions
To see all available characters:
```python
cowsay.character_names()
```

To print a text as a certain character:
```python
cowsay.<character>("Text I want to print")
```
A key difference is that the `cowsay.<character>()` function **returns** the string that needs to be printed
instead of printing the string itself. This was done so that the string can be stored in a variable. So if you
wanted to print cowsay messages later, send cowsay messages over a socket connection, or save logs in cowsay, 
you can do so.

The returned string is of type `CowString` which acts and behaves exactly the same as `str`. The only method that
is slightly different is the `__repr__` function.

The following characters can be used (no different than the original project):
- beavis
- cheese
- daemon
- cow
- dragon
- ghostbusters
- kitty
- meow
- milk  
- stegasaurus
- stimpy
- turtle 
- tux

If you wanted to print a message as `milk`, then you would have to do the following:
```
>>> print(cowsay.milk("Hello GitHub!"))
  _____________
 /             \
< Hello GitHub! >
  =============
                  \
                   \
                    \
                     \
                     
                    ____________ 
                    |__________|
                   /           /\
                  /           /  \
                 /___________/___/|
                 |          |     |
                 |  ==\ /== |     |
                 |   O   O  | \ \ |
                 |     <    |  \ \|
                /|          |   \ \
               / |  \_____/ |   / /
              / /|          |  / /|
             /||\|          | /||\/
                 -------------|   
                     | |    | | 
                    <__/    \__>
```

If you want to get a list of all functions:
```python
cowsay.character_functions()  # [<function cowsay.beavis>, <function cowsay.cheese>, ...]
```

You can also print from a random character:
```python
print(cowsay.random_character("Hello GitHub!"))
```
