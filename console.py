#!/usr/bin/python3
"""Console Class."""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models import storage as data
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNB Command."""

    prompt = '(hbnb) '

    def __init__(self):
        """Init."""
        super().__init__()
        self.classN = ["BaseModel", "User", "Place",
                       "State", "City", "Amenity", "Review"]

    def do_hello(self, args):
        """Print a greeting."""
        print("Hello!")

    def emptyline(self):
        """DO nothing."""
        pass

    def do_quit(self, args):
        """Quit the command-line interpreter."""
        return True

    do_exit = do_quit
    do_q = do_quit

    def do_EOF(self, arg):
        """Exit the program on EOF."""
        return True

    # COMMANDS
    def do_create(self, cln):
        """Init new instance of a class."""
        if len(cln) and cln in self.classN:
            x = eval(cln)
            x = x()
            print(x.id)
            x.save()
            return
        elif not len(cln):
            print("** class name missing **")
            return
        elif cln not in self.classN:
            print("** class doesn't exist **")
            return

    def do_show(self, cln):
        """Print string representation of an instance."""
        if len(cln) and cln.split(" ")[0] in self.classN:
            try:
                cln.split(" ")[1]
            except Exception as e:
                print("** instance id missing **")
                return
            idd = cln.split(" ")[0] + '.' + cln.split(" ")[1]
            x = data.all()
            if idd not in x:
                print("** no instance found **")
                return
            print(x[idd])
            return
        elif not len(cln):
            print("** class name missing **")
            return
        elif cln.split(" ")[0] not in self.classN:
            print("** class doesn't exist **")
            return

    def do_destroy(self, cln):
        """Delete instance based on class name and id."""
        if len(cln) and cln.split(" ")[0] in self.classN:
            try:
                cln.split(" ")[1]
            except Exception as e:
                print("** instance id missing **")
                return
            idd = cln.split(" ")[0] + '.' + cln.split(" ")[1]
            x = data.all()
            if idd not in x:
                print("** no instance found **")
                return
            del x[idd]
            data.save()
            return
        elif not len(cln):
            print("** class name missing **")
            return
        elif cln.split(" ")[0] not in self.classN:
            print("** class doesn't exist **")
            return

    def do_all(self, cln):
        """Print all string representation of all.

        instances based on class name or not.
        """
        if len(cln):
            if cln not in self.classN:
                print("** class doesn't exist **")
                return
            d = data.all()
            print([d[x].__str__() for x in d
                   if cln in x])
            return
        else:
            d = data.all()
            print([d[x].__str__() for x in d])

    def do_update(self, args):
        """Update an instance based on the class name and id."""
        arg_list = args.split(" ")
        if not len(args):
            print("** class name missing **")
        elif arg_list[0] not in self.classN:
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        elif len(arg_list) < 3:
            print("** attribute name missing **")
        elif len(arg_list) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(arg_list[0], arg_list[1])
            d = data.all()
            val = arg_list[3]
            try:
                val = eval(arg_list[3])
            except Exception as e:
                pass
            if key in d:
                obj = d[key]
                setattr(obj, arg_list[2], val)
                obj.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
