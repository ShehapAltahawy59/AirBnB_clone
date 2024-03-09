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
        """prints string representation of objects
        """
        my_dict = storage.all()
        my_list = []
        if len(arg) == 0:
            for values in my_dict.values():
                my_list.append(str(values))
            print(my_list)
        else:
            if arg not in HBNBCommand.valid_classes:
                print("** class doesn't exist **")
            else:
                for value in my_dict.values():
                    if value.to_dict()["__class__"] == arg:
                        my_list.append(str(value))
                print(my_list)

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
            objs = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
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
                    attr_type = type(getattr(obj, commands[2]))
                    commands[3] = attr_type(commands[3])
                except AttributeError:
                    pass
                att_name = commands[2]
                att_value = eval(commands[3])
                obj = objs[key]
                setattr(obj, att_name, att_value)
                obj.save()
                return

    def default(self, arg):
        """change the default behavior of cmd """

        args = arg.split(".")
        if len(args) != 2:
            print("*** Unknown syntax: {}".format(arg))
        else:
            class_name = args[0]
            command_name = args[1].split("(")[0]
            command_args = args[1].split("(")[1].split(")")[0].split("''")[0]
            values = command_args.split(",")
            _values = [value.strip('""') for value in values]
            cleaned_value_string = ' '.join(_values)

            if len(_values) == 2:
                if _values[1].startswith("{") and _values[1].endswith("}"):
                    attribute_value_pairs = _values[1][1:-1].split(",")
                    dictt = {}
                    for pair in attribute_value_pairs:
                        attr, val = pair.split(":")
                        dictt[attr.strip('""')] = val.strip('""')
                        x, y = dictt.items()[0]
                    string = "{} {} {}".format(_values[0], x, y)
                    cleaned_value_string = ' '.join(string)

            command_dict = {
                "all": self.do_all,
                "count": self.do_count,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "update": self.do_update
            }
            if command_name in command_dict.keys():
                command = command_dict[command_name]

                if command_name == "show" or command_name == "destroy":
                    string = "{}{}{}".format((class_name), " ", command_args.strip('""'))
                    return command(string)

                elif command_name == "update":
                    string = "{} {}".format((class_name), cleaned_value_string)
                    return command(string)
                else:
                    return command("{}{}".format(class_name, ""))
            else:
                print("*** Unknown syntax: {}".format(arg))


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
