#!/usr/bin/python3
import cmd
import sys
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

    prompt = "(hbnb) "
    classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    }

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

    def do_create(self, args):
        ''' creates a new instance of class BaseModel
        '''
        if len(args) == 0:
            print("** class name missing **")
            return
        arg_list = list(args.split())
        if arg_list[0] in self.classes:
            b_model = eval(arg_list[0])()
            b_model.save()
            print('{0}'.format(b_model.id))
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        ''' print string representation of instance based on
        class name and ID
        '''
        if len(args) == 0:
            print("** class name missing **")
            return

        all_obj = storage.all()
        arg_list = list(args.split())

        try:
            instance_id = "{0}.{1}".format(arg_list[0], arg_list[1])
            if arg_list[0] in self.classes:
                if len(arg_list) > 1:
                    if instance_id in all_obj.keys():
                        print(all_obj[instance_id])
                    else:
                        print("** no instance found **")
                        return
                else:
                    print("** instance id missing **")
                    return
            elif arg_list[0] not in self.classes:
                print("** class doesn't exist **")
        except:
            print("** instance id missing **")
            return

    def do_destroy(self, args):
        ''' deletes instance based on class name and id
        '''

        if len(args) == 0:
            print("** class name missing **")
            return
        all_obj = storage.all()
        arg_list = list(args.split())

        try:
            instance_id = arg_list[0] + '.' + arg_list[1]
            if arg_list[0] in self.classes:
                storage.reload()
                all_obj = storage.all()
                if instance_id in all_obj.keys():
                    del(all_obj[instance_id])
                    storage.save()
                else:
                    print("** no instance found **")
            elif arg_list[0] not in self.classes:
                print("** class doesn't exist **")
        except:
            print("** instance id missing **")
            return

    def do_all(self, args):
        ''' prints all string representation of instances created
        '''

        arg_list = list(args.split())
        results = []

        if len(args) == 0:
            storage.reload()
            all_obj = storage.all()
            for obj in all_obj:
                results += [str(all_obj[obj])]
                storage.save()
            print(results)
            return

        if arg_list[0] in self.classes:
            storage.reload()
            all_obj = storage.all()
            for obj in all_obj:
                results += [str(all_obj[obj])]
                storage.save()
            print(results)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        '''updates instance based on class name and id by
        adding attribute
        '''
        all_obj = storage.all()
        arg_list = list(args.split())

        if len(arg_list) == 0:
            print("** class name missing **")
            return
        elif len(arg_list) == 1 and arg_list[0] in self.classes:
            print("** instance id missing **")
            return
        elif len(arg_list) == 2 and arg_list[
                0] in self.classes and instance_id in all_obj.keys():
            print("** attribute name missing **")
            return
        elif len(arg_list) == 3:
            print("** value missing **")
            return
        if len(arg_list) > 4:
            arg_list = arg_list[:4]

        try:
            instance_id = "{0}.{1}".format(arg_list[0], arg_list[1])
            if arg_list[0] in self.classes:
                if instance_id not in all_obj.keys():
                    print("** no instance found **")
                    return
                    if instance_id in all_obj.keys():
                        storage.reload()
                        all_obj[instance_id].__dict__[
                            arg_list[2]] = arg_list[3].replace('\"', '')
                        storage.save()
                    else:
                        print("** class doesn't exist **")
        except:
            print ("** instance id missing **")
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
