#!/usr/bin/python3
""" Console Module """
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import json

class HBNBCommand(cmd.Cmd):
    """cmd class
    """
    prompt = "(hbnb)"
    valid_classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }

    def do_quit(self, command):
        """command to end the program
        """
        return True

    def help_quit(self):
        """ Prints the help documentation for quit  """
        print("Quit command to exit the program\n")

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        return True

    def help_EOF(self):
        """ Prints the help documentation for EOF """
        print("Exits the program without formatting\n")

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_create(self, arg):
        """creates a class instance
        """
        if not arg:
            print("** class name missing **")
            return
        if arg not in HBNBCommand.valid_classes.keys():
            print("** class doesn't exist **")
            return
        new_obj = HBNBCommand.valid_classes[arg]()
        new_obj.save()
        print(new_obj.id)

    def help_create(self):
        """ Prints the help documentation for EOF """
        print("create now model\n")

    def do_show(self, arg):
        """prints string repr of an instance
        """
        commands = arg.split()

        if len(commands) == 0:
            print("** class name missing **")
            return
        if commands[0] not in HBNBCommand.valid_classes.keys():
            print("** class doesn't exist **")
            return
        if len(commands) < 2:
            print("** instance id missing **")
            return
        objs = storage.all()
        key = "{}.{}".format(commands[0], commands[1])
        if key not in objs.keys():
            print("** no instance found **")
            return
        print(objs[key])

    def help_show():
        """ Prints the help documentation for EOF """
        print("show model\n")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        """
        commands = arg.split()
        if len(commands) == 0:
            print("** class name missing **")
            return
        if commands[0] not in HBNBCommand.valid_classes.keys():
            print("** class doesn't exist **")
            return
        if len(commands) < 2:
            print("** instance id missing **")
            return
        objs = storage.all()
        key = "{}.{}".format(commands[0], commands[1])
        if key not in objs.keys():
            print("** no instance found **")
            return

        del (objs[key])
        storage.save()
        return

    def help_destroy(self):
        """ Prints the help documentation for EOF """
        print("remove model\n")

    def do_all(self, arg):
        'Prints all string representation of all instances based or not on the class name'
        if arg not in self.valid_classes and arg != "":
            print("** class doesn't exist **")
        else:
            for obj in storage.all().values():
                if arg == "" or arg == obj.__class__.__name__:
                    print(obj)

    def help_all(self):
        """ Prints the help documentation for EOF """
        print("print all model\n")

    def do_update(self, arg):
        """updates an instance
        """
        commands = arg.split()

        if len(commands) == 0:
            print("** class name missing **")
            return
        if commands[0] not in HBNBCommand.valid_classes.keys():
            print("** class doesn't exist **")
            return
        if len(commands) < 2:
            print("** instance id missing **")
            return
        else:

            key = "{}.{}".format(commands[0], commands[1])
            objs = storage.all()
            if key not in objs.keys():
                print("** no instance found **")
            elif len(commands) < 3:
                print("** attribute name missing **")
                return
            elif len(commands) < 4:
                print("** value missing **")
                return
            else:
                try:
                    obj = storage.all()[key]
                    attr_type = type(getattr(obj, commands[2]))
                    commands[3] = attr_type(commands[3])
                except AttributeError:
                    pass
                att_name = commands[2]
                att_value = commands[3].strip('""')
                setattr(obj, att_name, att_value)
                obj.save()
                return

    def default(self, line):
        args = line.split('.')
        if len(args) != 2:
            print("*** Unknown syntax: {}".format(line))
        else:
            if args[1].startswith("update(") and args[1][-1] == ")":
                arg = args[1][7:-1].replace(",", "").replace("\"", "").split(" ")
                if arg[1].startswith("{"):
                    arg = [x.replace("{","").replace("}","").replace(":","").strip("''")for x in arg ]
                    my_dict = {arg[i]: arg[i + 1] for i in range(1, len(arg), 2)}
                    for k, v in my_dict.items():
                        arg_temp = [args[0], arg[0], k, str(v)]
                        self.do_update(" ".join(arg_temp))
                else:
                    self.do_update(args[0] + " " + " ".join(arg))
            elif args[1].startswith("destroy(") and args[1][-1] == ")":
                arg = args[1][8:-1]
                self.do_destroy(args[0] + " " + arg)
            elif args[1].startswith("show(") and args[1][-1] == ")":
                arg = args[1][5:-1]
                self.do_show(args[0] + " " + arg)
            elif args[1] == "all()":
                self.do_all(args[0])
            elif args[1] == "count()":
                self.do_count(args[0])

    def do_count(self, arg):
        """print count of class instance"""

        if not arg:
            print("** class name missing **")
            return
        class_name = arg.split(" ")[0]
        if class_name not in HBNBCommand.valid_classes.keys():
            print("** class doesn't exist **")
            return
        count = 0
        obj = storage.all()
        for key, val in obj.items():
            if (key.split(".")[0]) == class_name:
                count += 1
        print(count)

    def help_count(self):
        """ Prints the help documentation for EOF """
        print("print the count of calss instance\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
