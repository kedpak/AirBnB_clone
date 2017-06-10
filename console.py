#!/usr/bin/python3
'''command interpreter to manage data'''
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    '''the entry point of the command interpreter'''
    prompt = '(hbnb) '

    def do_create(self, args):
        '''Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id'''
        classes = {
            "BaseModel": BaseModel
        }

        args_list = list(args.split())
        if len(args_list) == 0:
            print("** class name missing **")
            return

        if args_list[0] in classes.keys():
            obj = classes[args_list[0]]()
            obj.save()
            print("{}".format(obj.id))
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        '''rints the string representation of an instance
        based on the class name and id'''

        args_list = list(args.split())
        if len(args_list) == 0:
            print("** class name missing **")
            print("** instance id missing **")
            return
        if len(args_list) == 1:
            print("** instance id missing **")
            return

        all_objs = storage.all()
        obj_class = args_list[0]
        obj_id = args_list[1]
        if obj_id in all_objs:
            if all_objs[obj_id].__class__.__name__ == obj_class:
                print(all_objs[obj_id])
            else:
                print("** class doesn't exist **")
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        '''Deletes an instance based on the class name
        and id and saves the change into the JSON file'''

        args_list = list(args.split())
        if len(args_list) == 0:
            print("** class name missing **")
            print("** instance id missing **")
            return
        if len(args_list) == 1:
            print("** instance id missing **")
            return

        all_objs = storage.all()
        obj_class = args_list[0]
        obj_id = args_list[1]
        if obj_id in all_objs:
            if all_objs[obj_id].__class__.__name__ == obj_class:
                del(all_objs[obj_id])
                storage.save()
            else:
                print("** class doesn't exist **")
        else:
            print("** no instance found **")

    def do_all(self, args):
        '''Prints all string representation of all instances
        based or not on the class name.
        Usage: $ all BaseModel or $ all'''

        args_list = list(args.split())
        if len(args_list) == 0:
            all_objs = storage.all()
            for obj in all_objs:
                print(all_objs[obj])
            return

        if len(args_list) == 1:
            obj_class = args_list[0]
            all_objs = storage.all()
            found_class = 0
            for obj_id in all_objs:
                if all_objs[obj_id].__class__.__name__ == obj_class:
                    found_class = 1
            if found_class == 1:
                for obj_id in all_objs:
                    if all_objs[obj_id].__class__.__name__ == obj_class:
                        print(all_objs[obj_id])
            else:
                print("** class doesn't exist **")

        else:
            print("Usage: $ all __class__.__name__ or $ all")

    def do_update(self, args):
        ''' Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the JSON file)
        Usage: update <class name> <id> <attribute name> <attribute value>'''

        args_list = list(args.split())
        if len(args_list) == 0:
            print("** class name missing **")
            print("** instance id missing **")
            print("** attribute name missing **")
            print("** value missing **")
            return
        if len(args_list) == 1:
            print("** instance id missing **")
            print("** attribute name missing **")
            print("** value missing **")
            return
        if len(args_list) == 2:
            print("** attribute name missing **")
            print("** value missing **")
            return
        if len(args_list) == 3:
            print("** value missing **")
            return

        all_objs = storage.all()
        obj_class = args_list[0]
        obj_id = args_list[1]
        attr = args_list[2]
        attr_value = args_list[3]
        found_class = 0
        found_id = 0

        for obj in all_objs:
            if all_objs[obj].__class__.__name__ == obj_class:
                found_class = 1
                if all_objs[obj].id == obj_id:
                    found_id = 1
        if found_class == 0:
            print("** class doesn't exist **")
            return
        if found_id == 0:
            print("** no instance found **")
            return

        all_objs[obj_id].__dict__[attr] = attr_value
        storage.save()

    def do_quit(self, arg):
        '''exits the program'''
        return True

    def do_EOF(self, arg):
        '''exits the program'''
        return True

    def emptyline(self):
        '''reprompts on empty line input'''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
