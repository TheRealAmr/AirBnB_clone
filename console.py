#!/usr/bin/python3
"""Console Class."""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNB Command."""

    prompt = '(hbnb) '

    def do_hello(self, args):
        """Print a greeting."""
        print("Hello!")

    def emptyline(self):
        """DO nothing."""
        pass

    def do_quit(self, args):
        """Quit the command-line interpreter."""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF."""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
