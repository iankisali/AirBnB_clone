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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
