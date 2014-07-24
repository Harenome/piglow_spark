#!/usr/bin/env python
"""PiGlow Spark module."""

from cmd import Cmd

from piglow_spark.piglow import PiGlow
from piglow_spark.error.piglow_error import PiGlowError

## Strings for terminal printing
NORMAL_TEXT = "\033[0m"
BOLD_TEXT = "\033[1m"
DIM_TEXT = "\033[2m"
UNDERLINED_TEXT = "\033[4m"
RED_TEXT = "\033[38;5;196m"
BLUE_TEXT = "\033[38;5;74m"
GREEN_TEXT = "\033[38;5;148m"
ORANGE_TEXT = "\033[38;5;214m"
YELLOW_TEXT = "\033[38;5;227m"

## A few decorators and utilities
def print_error(message):
    """Print an error message."""
    print(BOLD_TEXT + RED_TEXT + "Error" + NORMAL_TEXT + RED_TEXT + ": " \
        + message + NORMAL_TEXT)

def print_warning(message):
    """Print a warning message."""
    print(BOLD_TEXT + ORANGE_TEXT + "Warning" + NORMAL_TEXT + ORANGE_TEXT \
        + ": " + message + NORMAL_TEXT)

def foolproof(func):
    """Decorator to handle cases where an argument input is invalid."""
    def fooltest(self, args):
        """Test for fools."""
        try:
            return func(self, args)
        except ValueError:
            print_error("something is wrong with the supplied arguments.")
        except PiGlowError as error:
            print_error(error.message)

    return fooltest

def noargs(func):
    """Decorator for no argument commands."""
    def args_check(self, args):
        """Check args."""
        if args == "":
            return func(self, args)
        else:
            print_error("this command takes no argument.")

    return args_check

def print_func_help_aux(self, func):
    """Auxilary function for help printing."""
    fun = func(self)
    signature = BOLD_TEXT + fun.func_name + NORMAL_TEXT
    argcount = fun.func_code.co_argcount

    if fun.func_code.co_argcount > 0:
        argument_names = fun.func_code.co_varnames
        if argument_names[0] == "self":
            start = 1
        else:
            start = 0
        # 'co_varnames' include all variables of the code object.
        # We only need those that are arguments of the function.
        argument_names = argument_names[start:argcount]
        for arg in argument_names:
            signature = signature + " <" + UNDERLINED_TEXT + arg \
                + NORMAL_TEXT + ">"

    print("\n" + signature + "\n" + fun.func_doc)

def printhelp(func):
    """Decorator for help printing."""
    def print_func_help(self):
        """Print the help."""
        print_func_help_aux(self, func)
        print("")

    return print_func_help

def printhelpnotimpl(func):
    """Decorator for help printing."""
    def print_func_help(self):
        """Print the help."""
        print_func_help_aux(self, func)
        print_warning("this has not been implemented yet.\n")

    return print_func_help

def notimplemented(func):
    """Decorator for not implemented commands."""
    def nothing(self, args):
        """Nothing."""
        print_error("this functionnality has not been implemented yet.")

    return nothing


class PiGlowCmd(Cmd):
    """PiGlow interpreter."""
    def __init__(self, completekey='tab', stdin=None, stdout=None):
        self.__piglow = PiGlow()
        self.__saved_state = self.__piglow.dump()
        Cmd.__init__(self, completekey, stdin, stdout)
        self.prompt = BOLD_TEXT + "PiGlow Spark" + DIM_TEXT + " >>>" \
            + NORMAL_TEXT + " "

    @staticmethod
    def two_args(func, args):
        """For commands that take two arguments, the first being and ID."""
        arguments = args.split()
        if len(arguments) != 2:
            print_error("this command takes two arguments.")
        else:
            # Dirty workaround (can't use isistance !):
            try:
                int(arguments[0])
            except ValueError:
                # If arguments[0] is not a string representing an int.
                return func(arguments[0], int(arguments[1]))
            # If arguments[0] is a string representing an int.
            return func(int(arguments[0]), int(arguments[1]))

    ## Redefinition of some inherited methods
    def emptyline(self):
        # The default behaviour is to repeat the last used command !
        pass

    def preloop(self):
        print("Welcome to the PiGlow Spark interpreter.\n" \
            + "Type '" + GREEN_TEXT + "help" + NORMAL_TEXT \
            + "' if you don't know what to do.")
        Cmd.preloop(self)

    def postloop(self):
        Cmd.postloop(self)

    ## Commands
    def do_list(self, args):
        """Command to list IDs."""
        def print_ids(ids):
            for i in ids:
                print(i)
        def print_leds():
            print("\nLEDs:\n-----")
            print_ids(self.__piglow.LED_AVAILABLE)
        def print_rings():
            print("\nRings:\n------")
            print_ids(self.__piglow.RING_AVAILABLE)
        def print_arms():
            print("\nArms:\n-----")
            print_ids(self.__piglow.ARM_AVAILABLE)

        if args == "":
            print_leds()
            print_rings()
            print_arms()
            print("")
        else:
            arguments = args.split()
            if len(arguments) != 1:
                print_error("This command takes 0 or 1 argument.")
            elif args == "leds":
                print_leds()
                print("")
            elif args == "rings":
                print_rings()
                print("")
            elif args == "arms":
                print_arms()
                print("")
            else:
                print_error("Invalid argument.")

    def help_list(self):
        """Print the help for the list command."""
        print("\n" + BOLD_TEXT + "list" + NORMAL_TEXT + " [" \
            + UNDERLINED_TEXT + "leds" + NORMAL_TEXT + " | " \
            + UNDERLINED_TEXT + "rings" + NORMAL_TEXT + " | " \
            + UNDERLINED_TEXT + "arms" + NORMAL_TEXT + "]")
        print("Print the available IDs.\n")

    @foolproof
    def do_all(self, args):
        """Do all."""
        brightness = int(args)
        self.__piglow.all(brightness)

    @printhelp
    def help_all(self):
        """Print the help for all."""
        return self.__piglow.all

    @foolproof
    def do_led(self, args):
        """Command to light a LED."""
        PiGlowCmd.two_args(self.__piglow.led, args)

    @printhelp
    def help_led(self):
        """Print the help for the led command."""
        return self.__piglow.led

    @foolproof
    def do_arm(self, args):
        """Command to light an Arm."""
        PiGlowCmd.two_args(self.__piglow.arm, args)

    @printhelp
    def help_arm(self):
        """Print the help for the arm command."""
        return self.__piglow.arm

    @foolproof
    def do_ring(self, args):
        """Command to light a Ring."""
        PiGlowCmd.two_args(self.__piglow.ring, args)

    @printhelp
    def help_ring(self):
        """Print the help for the ring command."""
        return self.__piglow.ring

    @foolproof
    def do_color(self, args):
        """Command to light a Color."""
        PiGlowCmd.two_args(self.__piglow.color, args)

    @printhelp
    def help_color(self):
        """Print the help for the color command."""
        return self.__piglow.color

    @notimplemented
    def do_ledset(self, args):
        """Command to light a set of LEDs."""
        pass

    @printhelpnotimpl
    def help_ledset(self):
        """Print the help for the ledset command."""
        return self.__piglow.led_set

    @notimplemented
    def do_buffer(self, args):
        """Command to buffer brightnesses."""
        pass

    @printhelpnotimpl
    def help_buffer(self):
        """Print the help for the buffer command."""
        return self.__piglow.buffer

    @noargs
    def do_dump(self, args):
        """Command to dump the current state."""
        self.__saved_state = self.__piglow.dump()

    @printhelp
    def help_dump(self):
        """Print the help for the dump command."""
        return self.__piglow.dump

    @noargs
    def do_restore(self, args):
        """Command to restore a state."""
        self.__piglow.restore(self.__saved_state)

    @printhelp
    def help_restore(self):
        """Print the help for the restore command."""
        return self.__piglow.restore

    @noargs
    def do_update(self, args):
        """Command to update the board."""
        self.__piglow.update()

    @printhelp
    def help_update(self):
        """Print the help for the update command."""
        return self.__piglow.update

    @noargs
    def do_off(self, args):
        """Command to switch off all LEDs."""
        self.__piglow.off()

    @printhelp
    def help_off(self):
        """Print the help for the off command."""
        return self.__piglow.off

    @noargs
    def do_up_to_date(self, args):
        """Command to check whether the board is up to date."""
        print(self.__piglow.up_to_date())

    @printhelp
    def help_up_to_date(self):
        """Print the help for the up_to_date command."""
        return self.__piglow.up_to_date

    @noargs
    def do_exit(self, args):
        """Command to exit."""
        return True

    def help_exit(self):
        """Print the help for the exit command."""
        print("Exit the interpreter.")

