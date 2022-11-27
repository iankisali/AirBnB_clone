# AirBnB_clone - The Console

![hbnb logo](./img/hbnb_logo.png)

## Description

This is a team project that is part of ALX Full-stack Software Engineering Program. It is the first step towards building our first full web application - AirBnB clone. In this repo we are creating the Console which is a Storage Engine i.e a Command Interpreter that can manipulate data without visual interface, like a Shell.

Below is a pictorial reprsentation of steps taken to build the AirBnB clone:

![Flow Chart](./img/flowchart.png)

This repository contains the Storage Engine as shown above.

## Usage

The console works both in interactive mode and non-interactive mode, much like a Unix shell.
It prints a prompt **(hbnb)** and waits for the user for input.

### Interactive Mode

In Intercative mode the shell works as follows:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) help all
Prints all string representation of all instances.

(hbnb) help create
Creates an instance.

(hbnb) help update
Updates an instance by adding or updating attribute.

(hbnb) quit
$
```

### Non-interactive Mode
In Non-Intercative mode the shell works as follows:

```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)

$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
(hbnb) 
$
```

## Commands

Command | Example
------- | -------
Run the console | ```./console.py```
Quit the console | ```(hbnb) quit```
Display the help for a command | ```(hbnb) help <command>```
Create an object (prints its id)| ```(hbnb) create <class>```
Show an object | ```(hbnb) show <class> <id>``` or ```(hbnb) <class>.show(<id>)```
Destroy an object | ```(hbnb) destroy <class> <id>``` or ```(hbnb) <class>.destroy(<id>)```
Show all objects, or all instances of a class | ```(hbnb) all``` or ```(hbnb) all <class>```
Update an attribute of an object | ```(hbnb) update <class> <id> <attribute name> "<attribute value>"``` or ```(hbnb) <class>.update(<id>, <attribute name>, "<attribute value>")```
