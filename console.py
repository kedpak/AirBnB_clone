#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
'''module: console
This module contains the entry point of command line iterpreter
Includes: help(builtin), EOF, quit, and custom prompt('hbnb')
'''


class HBNBCommand(cmd.Cmd):

    def __init__(self):
        '''constructor method
        '''
        cmd.Cmd.__init__(self)
        self.prompt = "(hbnb) "

    classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    }

    def do_create(self, args):
        """ creates a new instance of class BaseModel
        """
        if len(args) == 0:
            print("** class name missing **")
            return

        arg_list = list(args.split())
        if arg_list[0] in self.classes:
            b_model = eval(arg_list[0])()
            b_model.save()
            self.model_id = b_model.id
            print('{0}'.format(b_model.id))
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """ print string representation of instance based on
        class name and ID """

        if len(args) == 0:
            print("** class name missing **")
            return
        all_obj = storage.all()
        arg_list = list(args.split())

        if arg_list[0] in self.classes and arg_list[1]:
            if (arg_list[0] + "." + self.model_id) not in all_obj:
                print ("** no instance found **")
                return
            if arg_list[1] == self.model_id:
                print(all_obj[arg_list[0] + "." + self.model_id])
            else:
                print("** instance id missing **")
        elif arg_list[0] not in self.classes:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """ deletes instance based on class name and id
        """
        if len(args) == 0:
            print("** class name missing **")
            return
        all_obj = storage.all()
        arg_list = list(args.split())

        if arg_list[0] in self.classes and arg_list[1] == self.model_id:
            del(all_obj[arg_list[0] + "." + self.model_id])
        elif arg_list[0] not in self.classes:
            print("** class doesn't exist **")
        elif arg_list[0] in self.classes and arg_list[1] != self.model_id:
            print("** instance id missing **")

    def do_all(self, args):
        """ prints all string representation of instances created
        """
        all_obj = storage.all()
        arg_list = list(args.split())

        if len(args) == 0:
            for obj in all_obj:
                print(all_obj[obj])
            return

        if arg_list[0] in self.classes:
            for obj in all_obj:
                print(all_obj[obj])
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """updates instance based on class name and id by
        adding attribute"""

        all_obj = storage.all()
        arg_list = list(args.split())

        if len(arg_list) == 0:
            print("** class name missing **")
            return
        if len(arg_list) == 1:
            print("** instance id missing **")
            return
        if len(arg_list) == 2:
            print("** attribute name missing **")
            return
        if len(arg_list) == 3:
            print("** value missing **")
            return

        if arg_list[0] in self.classes:
            if arg_list[1] != self.model_id:
                print("** no instance found **")
                return
            else:
                all_obj[arg_list[0] + "." + self.model_id].__dict__[
                    arg_list[2]] = arg_list[3].replace('\"', '')
                storage.save()
        else:
            print("** class doesn't exist **")

    def emptyline(self):
        '''if empty line entered pass
        '''
        pass

    def do_EOF(self, line):
        '''EOF command to exit the program
        '''
        return (True)

    def do_quit(self, line):
        '''Quit command to exit the program
        '''
        return (True)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
