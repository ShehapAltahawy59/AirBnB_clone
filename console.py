import cmd
from models.base_model import BaseModel
from models import storage
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    valid_classes = {"BaseModel":BaseModel(),}
    def do_quit (self,command):
        exit()
    def help_quit(self):
        """ Prints the help documentation for quit  """
        print("Quit command to exit the program\n")

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        print()
        exit()

    def help_EOF(self):
        """ Prints the help documentation for EOF """
        print("Exits the program without formatting\n")
    
    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_create(self,arg):
        if not arg:
            print("** class name missing **")
            return
        if arg not in HBNBCommand.valid_classes.keys():
            print("** class doesn't exist **")
            return
        new_obj=HBNBCommand.valid_classes[arg]
        new_obj.save()
        print(new_obj.id)
    
    def help_create(self):
        """ Prints the help documentation for EOF """
        print("create now model\n")

    def do_show(self,arg):
        commands=arg.split()
        if len(commands) == 0:
            print("** class name missing **")
            return
        if commands[0] not in HBNBCommand.valid_classes.keys() :
            print("** class doesn't exist **")
            return
        if len(commands) < 2:
            print("** instance id missing **")
            return
        objs = storage.all()
        for obj in objs.values():
            if commands[1] == obj.id:
                print(obj)
                return
        print("** no instance found **")
        return
        

    

        
            





if __name__ == '__main__':
    HBNBCommand().cmdloop()
