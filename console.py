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

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        if not arg: #Checks if arg parameter is empty.
            print("** class name missing **") #if args is empty, then prints class name missing
            return
        try:
            class_name = arg.split()[0] #We are splitting arg string into a list of words (using split())
            new_instance = BaseModel() #creating a new class object
            new_instance.save() #Use already defined Save method o this new object
            print(new_instance.id) #Prints id data of object to console.py
        except NameError: #if there is a Name Error, it will print class doesnt exist
            print("** class doesn't exist **")
    
    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg: #Checks if arg parameter is empty.
            print("** class name missing **") #if args is empty, then prints class name missing
            return
        try:
            args = arg.split() #Again we use split() to split args string into list of words and store the result in args
            class_name = args[0] # Give first word in args to class_name variable
            if len(args) < 2: #Checking if the length of args word is less than 2, if so object ID is missing
                print("** instance id missing **")
                return
            instance_id = args[1] #Now we assign the second word in args
            instance = storage.all().get(f"{class_name}.{instance_id}") #Uses storage to find class_name or instance_id and stores it in instance variable
            if instance:
                print(instance)
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()