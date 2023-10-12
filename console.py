#!/usr/bin/python3
"""Defines a class HBNBCommand, entry point of the command interpreter"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Represents the the HBNBCommand class"""
    prompt = '(hbnb) '
    
    def do_quit(self, arg):
        """Exits the program if (quit) is input"""
        return True
    
    def do_EOF(self, arg):
        """Exits the program if (EOF) is input"""
        return True
    
    def emptyline(self):
        """Does nothing"""
        pass
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()