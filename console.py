#!/usr/bin/python3
"""Defines a class HBNBCommand, entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage

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

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        
        if not arg: #Checks if arg parameter is empty.
            print("** class name missing **") #if args is empty, then prints class name missing
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            file_storage = FileStorage() #creates an object that represents an instance of FileStorage class
            new_instance = BaseModel() #creating a new class object
            print(new_instance.id) #Prints id data of object to console.py
            file_storage.new(new_instance) #add the new instance to the storage system
            file_storage.save() #Use already defined Save method o this new object
            
    
    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        
        if not args: #Checks if arg parameter is empty.
            print("** class name missing **") #if args is empty, then prints class name missing
            return
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            #Again we use split() to split args string into list of words and store the result in args
            class_name = args[0] # Give first word in args to class_name variable
            instance_id = args[1] #Now we assign the second word in args
            file_storage = FileStorage()
            instance = storage.all().get(f"{class_name}.{instance_id}") #Uses storage to find class_name or instance_id and stores it in instance variable
            if instance:
                print(instance)
            else:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()