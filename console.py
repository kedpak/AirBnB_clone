#!/usr/bin/python3
import cmd
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
