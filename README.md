# Air BnB Clone - The Console
![alt text](https://github.com/kedpak/AirBnB_clone/blob/master/hbnb_screenshot.png)
## Synopsis
The AirBnB clone project is a multi-threaded project that covers the fundamental areas of higher level programming. The end goal of the entire project is to deploy on our own server, a simple clone of the AirBnB website. For this first segment, the team will create a console/command line interpreter that takes in input, and stores objects into a JSON file. 

![alt text](https://github.com/kedpak/AirBnB_clone/blob/master/console.png)

## Description
 A command line interpreter/console, is the interface where a user inputs commands to perform specific tasks. This command interpreter manages objects that is utilized for the AirBnB website. In the context of this project, it will be used for the following:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database, etc.
* Do operations on objects (count, compute stats, etc.)
* Update attributes of an object
* Destroy an Object

### Key Concepts
#### CMD Module
The CMD module provides support for line-oriented command intepreters. Cmd is a class that provides a framework for a command line interface. It is often utilized with testing, administrative tasks, and debugging. 

#### Packages
Packages organize a Python module by utilizing "dotted module names". A Python file is called a module. When a module is inside of a folder, the folder is called a package. Packages are crucial for orgainzing files in a large project. The following example shows a submodule called 'rap' being imported from a package called 'music' using dotted notation.

`import music.rap`

#### UUID Module
The UUID module implements objects and functions that are immutable. The functions provide a unique ID. 

#### Datetime Module
The Datetime module implements classes that handle anything dealing with dates and times. There are two primary date and time objects that are utilized: "naive" and "aware"
* aware: aware objects possess sufficient knowledge and to be able to pinpoint where it stands relative to other aware objects. Fore example, specific time zones, and day light savings. 
* naive: naive objects do not possess enough knowledge to know where it stands relatively. 

#### Unittest Module
The Unittest Module allows for testing

#### args/kwargs
The *args and *kwargs allows for a variable number of arguments to be passed through a function. 

* *args: Certain functions do not know how many arguments will be passed into the function, therefore args is important for flexible passing of a certain number of arguments. 

* **kwargs: kwargs allows a keyworded variable to be passed into the function argument. 

## Excution Process
Interactive mode

```sh
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$`

Non-interactive mode

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## How to Start and Usage


## Authors
* Kevin Pak
* Christian Agha
* Chris Turner
