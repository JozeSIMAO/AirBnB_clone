#!/usr/bin/python3
"""Defines a class HBNBCommand, entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
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
            instance = file_storage.all().get(f"{class_name}.{instance_id}") #Uses storage to find class_name or instance_id and stores it in instance variable
            if instance:
                print(instance)
            else:
                print("** no instance found **")
    
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
         print("**class name missing *Z*")
        return

    
        args = arg.split() #Splits the argument into a list of words
        class_name = args[0]
        
        if len(args) < 2: # This checks if the argument contains a class name and an instance id
            print("** instance id missing **")
        else:
            instance_id = args[1]
            instances = storage.all()
            key = f"{class_name}.{instance_id}"

        # Check if the instance exists and delete it if found
        if key in instances:
            del instances[key] #If Key is found, Delete
            storage.save() #Save progress
        else:
            print("** no instance found **") #If the class name and id does not exist

def do_all(self, arg):
    """Prints all string representations of instances"""
    args = arg.split() #Splits the argument into a list of words

  
    if not arg:  # This checks if the argument is empty, and if so, print all instances
        print([str(instance) for instance in storage.all().values()]) #We use str() to turn the ibject instance into a printable string
    elif args:
        class_name = args[0]

      
        if class_name in storage.all():  # This check if the class name exists in the storage

           
            print([str(instance) for instance in storage.all().values() if instance.__class__.__name__ == class_name]) # Now we are filterering instances by class name and print them
        else: #If class name and ID does not exist
            print("** class doesn't exist **")

def do_update(self, arg):
    """Updates an instance's attribute"""
    if not arg: #If instance is not in arg
        print("** class name missing **")
    else:
        args = arg.split() #Splits the argument into a list of words
        class_name = args[0] #Give first word in args variable name class_name

    
        if len(args) < 2:    #This checks if the argument contains a class name and an instance id. Use Len() to filter condition
            print("** instance id missing **")
        elif f"{class_name}.{instance_id}" not in storage.all():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            instance_id = args[1]
            attr_name = args[2]
            attr_value = args[3]

            
            instance = storage.all().get(f"{class_name}.{instance_id}")#We can now get the instance from storage

            if instance:#Finally, we can set the attribute value and save the instance
                
                setattr(instance, attr_name, attr_value)
                instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()