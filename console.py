#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
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

    def do_create(self, args):
        """ creates a new instance of class BaseModel
        """
        if len(args) == 0:
            print("** class name missing **")
            return

        arg_list = list(args.split())
        if arg_list[0] == "BaseModel":
            b_model = BaseModel()
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

        if all_obj["BaseModel." + self.model_id] is None:
            print("** no instance found **")
        if arg_list[0] == "BaseModel" and arg_list[1] == self.model_id:
            print(all_obj["BaseModel." + self.model_id])
        elif arg_list[0] != "BaseModel":
            print("** class doesn't exist **")
        elif arg_list[1] != self.model_id:
            print("** instance id missing **")

    
    def do_destroy(self, args):
        """ deletes instance based on class name and id
        """
        if len(args) ==0:
            print("** class name missing **")
            return
        all_obj = storage.all()
        arg_list = list(args.split())

        if arg_list[0] == "BaseModel" and arg_list[1] == self.model_id:
            del(self.b_model)
        elif arg_list[0] != "BaseModel":
            print("** class doesn't exist **")
        elif arg_list[1] != self.model_id:
            print("** instance id missing **")

    
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
