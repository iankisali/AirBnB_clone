#!/usr/bin/python3
"""Module entry point to command interpreter"""
import cmd
from models import storage
from models.base_model import BaseModel
import json
import re


class HBNBCommand(cmd.Cmd):
    """class for command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """handels EOF character"""
        print()
        return True

    def emptyline(self):
        """Doesn't do anything on enter"""
        pass

    def do_create(self, line):
        """creates instance"""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            my_file = storage.classes()[line]()
            my_file.save()
            print(my_file.id)

    def do_show(self, line):
        """print string representation of instance"""
        if line == "" or line is None:
            print("** class name is missing **")
        else:
            word = line.split(' ')
            if word[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(word) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(word[0], word[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes instance based on class name and id"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            word = line.split(' ')
            if word[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(word) < 2:
                print("** instance id is missing **")
            else:
                key = "{}.{}".format(word[0], word[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """print string representation of all instances"""
        if line != "":
            word = line.split(' ')
            if word[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                x = [str(obj) for key, obj in storage.all().items()
                     if type(obj).__name__ == word[0]]
                print(x)
        else:
            my_list = [str(obj) for key, obj in storage.all().items()]
            print(my_list)

    def do_count(self, line):
        """counts class instances"""
        word = line.split(' ')
        if not word[0]:
            print("** class name missing **")
        elif word[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            match = [k for k in storage.all() if k.startswith(
                 word[0] + '.')]
            print(len(match))

    def do_update(self, line):
        """update instance by adding or updating attribute"""
        if line == "" or line is None:
            print("** class name is missing **")
            return

        regex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(regex, line)
        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class does't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        value = value.replace('"', '')
                    attributes = storage.attributes()[classname]
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    elif cast:
                        try:
                            value = cast(value)
                        except ValueError:
                            pass
                    setattr(storage.all()[key], attribute, value)
                    storage.all()[key].save()

    def default(self, line):
        """catch command if no match"""
        self._precmd(line)

    def _precmd(sellf, line):
        """Intercept command to test for class.syntax()"""
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        matchUidArgs = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if matchUidArgs:
            uid = matchUidArgs.group(2)
            attrDict = matchUidArgs.group(2)
        else:
            uid = args
            attrDict = False

        attrValue = ""
        if method == "update" and attrDict:
            matchDict = re.search('^({.*})$', attr_or_dict)
            if matchDict:
                self.update_dict(classname, uid, matchDict.group(1))
                return ""
            matchAttrValue = re.search('^(?:"([^"]*)")?(?:, (.*))?$', attrDict)
            if matchAttrValue:
                attrValue = (matchAttrValue.group(1) or "")
                + " " + (matchAttrValue.group(2) or "")
        command = method + " " + classname + " " + uid + " " + attrValue
        self.onecmd(command)
        return command

    def update_dict(self, classname, uid, s_dict):



if __name__ == '__main__':
    HBNBCommand().cmdloop()
