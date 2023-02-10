#!/usr/bin/python3
""" Defines HBNBCommand class."""
import cmd


class HBNBCommand(cmd.Cmd):
    """ Represents the command interpreter for working with 'hbnb'
    project.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):

        return True

    def emptyline(self):
        pass

    def do_EOF(self, arg):
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    def help_EOF(self):
        print("Quit command when end of file is encountered.\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
