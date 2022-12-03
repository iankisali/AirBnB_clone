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

## Models
The folder **[models](./models/)** contains ass classes used in the project.

File | Description | Attributes
---- | ----------- | ----------
[base_model.py](./models/base_model.py) | BaseModel class for all the other classes | `id`, `created_at`, `updated_at`
[user.py](./models/user.py) | User class for future user information | `email`, `password`, `first_name`, `last_name`
[amenity.py](./models/amenity.py) | Amenity class for future amenity information | `name`
[city.py](./models/city.py) | City class for future city location information | `state_id`, `name`
[state.py](./models/state.py) | State class for future location information | `name`
[place.py](./models/place.py) | Place class for future accomodation information | `city_id`, `user_id`, `name`, `description`, `number_rooms`, `number_bathrooms`, `max_guest`, `price_by_night`, `latitude`, `longitude`, `amenity_ids`
[review.py](./models/review.py) | Review class for future user/host review information | `place_id`, `user_id`, `text`

## File storage

The folder **[engine](./models/engine/)** in **[models](./models/)** folder manages the serialization and deserialization of all the data using JSON format.

A FileStorage class is defined in **[file_storage.py](./models/engine/file_storage.py)** with methods to follow this flow:
```<object> -> to_dict() -> <dictionary> -> JSON dump -> <json string> -> FILE -> <json string> -> JSON load -> <dictionary> -> <object>```

The **[__init__.py](./models/__init__.py)** file contains the instantiation of the FileStorage class called **storage**, followed by a call to the method reload() on that instance.
This allows the storage to be reloaded automatically at initialization, which recovers the serialized data.

## Tests

All the code is tested with the **unittest** module.
The test for the classes are in the **[test_models](./tests/test_models/)** folder.

## Authors

<details>
    <summary>Ian Kisali</summary>
    <ul>
    <li><a href="https://www.github.com/iankisali">Github</a></li>
    <li><a href="https://www.twitter.com/IanKisali_">Twitter</a></li>
    <li><a href="mailto:iankisali@gmail.com">E-mail</a></li>
    </ul>
</details>


<details>
    <summary>Eric Kabira</summary>
    <ul>
    <li><a href="https://github.com/Erico-droid">Github</a></li>
    </ul>
</details>
