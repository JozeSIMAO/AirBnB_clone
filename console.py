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
            file_storage = FileStorage()
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
            print("**class name missing **")
            return
        
        args = arg.split()
        class_name = args[0]
        file_storage = FileStorage()
        
        if len(args) < 2:
            print("** instance id missing **")
        else:
            instance_id = args[1]
            instances = file_storage.all()
            key = f"{class_name}.{instance_id}"
        
        if key in instances:
            del instances[key]
            file_storage.save()
        else:
            print("** no instance found **")
    
    def do_all(self, arg):
        """Prints all string representations of instances"""
        file_storage = FileStorage()
        file_storage.classes = {
            "BaseModel": BaseModel,
        }
        file_storage.reload() #Loads data from file storage
        instances = file_storage.all()
        args = arg.split() #Splits the argument into a list of words

        if not arg:  # This checks if the argument is empty, and if so, print all instances
            print([str(instance) for instance in file_storage.all().values()]) #We use str() to turn the ibject instance into a printable string
        elif args:
            class_name = args[0]
            if class_name in file_storage.classes: #If class name and ID does exist
                object_list = [str(instance) for instance in instances.values() if instance.__class__.__name__ == class_name]
                if object_list:
                    print(object_list)
                else:
                    print("[]")
            else:
                print("** class doesn't exist **")
            
      
def do_update(self, arg):
    """Updates an instance's attribute"""
    file_storage = FileStorage()
    
    if not arg:  # If instance is not in arg
        print("** class name missing **")
    else:
        args = arg.split()  # Splits the argument into a list of words
        if len(args) < 2:  # This checks if the argument contains a class name and an instance id.
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            if f"{class_name}.{instance_id}" not in file_storage.all():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                attr_name = args[2]
                attr_value = args[3]
                instance = file_storage.all().get(f"{class_name}.{instance_id}")

                if instance:
                    # Check if the attribute exists in the instance and cast the value to the attribute type
                    if hasattr(instance, attr_name):
                        attr_type = type(getattr(instance, attr_name))
                        if attr_type == str:
                            setattr(instance, attr_name, str(attr_value))
                        elif attr_type == int:
                            setattr(instance, attr_name, int(attr_value))
                        elif attr_type == float:
                            setattr(instance, attr_name, float(attr_value))
                        else:
                            print("** Invalid attribute type. Only string, integer, and float attributes can be updated. **")
                            return
                        instance.save()
                    else:
                        print("** Invalid attribute name. Attribute doesn't exist for this model. **")
                else:
                    print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()