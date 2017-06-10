#!/usr/bin/python3
'''command interpreter to manage data'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''the entry point of the command interpreter'''
    prompt = '(hbnb) '

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
