#!/usr/bin/python3
""" Defines HBNBCommand class."""
import cmd
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """ Represents the command interpreter for working with 'hbnb'
    project.
    """

    __classes = ["BaseModel", "User","State", "City", "Amenity",
                "Place", "Review"]
    prompt = "(hbnb) "
    
    def do_create(self, args):
        parsed_args = parseargs(args)
        if not parsed_args:
            print("** class name missing **")
            return
        if parsed_args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        else:
            b = eval(parsed_args[0])()
            b.save()
            print(b.id)

    def do_show(self, args):
        parsed_args = parseargs(args)

        if not parsed_args:
            print("** class name missing **")
            return
        if parsed_args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(parsed_args) < 2:
            print("** instance id missing **")
        else:
            s = models.storage
            b = s.all().get("{}.{}".format(parsed_args[0], parsed_args[1]))
            if b is None:
                print("** no instance found**")
            else:
                print(b.get("id"))

    def do_destroy(self, args):
        parsed_args = parseargs(args)

        if not parsed_args:
            print("** class name missing **")
            return
        if parsed_args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(parsed_args) < 2:
            print("** instance id missing **")
            return
        else:
            s = models.storage
            b = s.all().get("{}.{}".format(parsed_args[0], parsed_args[1]))
            if b is None:
                print("** no instance found **")
                return
            else:
                del s.all()["{}.{}".format(parsed_args[0], parsed_args[1])]
                s.save()

    def do_all(self, args):
        parsed_args = parseargs(args)
        if len(parsed_args):
            if parsed_args[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
            else:
                objs = instancelist(parsed_args)
                print(objs)
        else:
            objs = instancelist()
            print(objs)

    def do_quit(self, arg):
        return True

    def emptyline(self):
        pass

    def do_EOF(self, arg):
        print("")
        return True

    def help_all(self):
        print("Print a List of all instances or all [instance_name] instances\n\
                Usage:\n{}\n'all'\n'all BaseModel'\n".format("="*40))

    def help_destroy(self):
        print("Destroys an instance of class with the given id\n\
                Usage:\n{}\n'destroy [instanceid]'\n".format('='*40))

    def help_show(self):
        print("Shows an instance with a given id\n\
                Usage:\n{}\n'show BaseModel [instance_id]'\n".format('='*40))

    def help_create(self):
        print("create an object and save to JSON file\n\
              Usage:\n{}\n 'create BaseModel'\n".format('='*40))

    def help_quit(self):
        print("Quit command to exit the program\n")

    def help_EOF(self):
        print("Quit command when end of file is encountered.\n")

def parseargs(args):
    """ Parses arguments passed to command interpreter."""
    
    return args.split()

def instancelist(arg=None):
    """ Constructs instances and returns them as list."""

    if arg is None:
        instancedict = models.storage.all()
        objs = [eval(value["__class__"])(**value) for key, value in instancedict.items()]
        return [str(obj) for obj in objs]
    else:
        instancedict = models.storage.all()
        objs = [eval(value["__class__"])(**value) for key, value in instancedict.items()
                if value["__class__"] in arg]
        return [str[obj] for obj in objs]

if __name__ == "__main__":
    HBNBCommand().cmdloop()
