#!/usr/bin/env python

from components.board import Board
from components.led import Led
from components.led import LedBrightnessError
from components.arm import Arm
from components.ring import Ring
from error.pyglowerror import PyGlowError

from cmd import Cmd


class PiGlow(Board):
    """Control the PiGlow board."""
    MIN_BRIGHTNESS = Led.MIN_BRIGHTNESS
    MAX_BRIGHTNESS = Led.MAX_BRIGHTNESS

    LED_NUMBER = Led.NUMBER
    LED_FIRST = Led.FIRST
    LED_AVAILABLE = Led.available()

    ARM_NUMBER = Arm.NUMBER
    ARM_FIRST = Arm.FIRST
    ARM_AVAILABLE = Arm.available()

    RING_NUMBER = Ring.NUMBER
    RING_FIRST = Ring.FIRST
    RING_AVAILABLE = Ring.available()


class PyGlowCmd(Cmd):
    """PyGlow interpreter."""
    def __init__(self, completekey='tab', stdin=None, stdout=None):
        self.__piglow = PiGlow()
        Cmd.__init__(self, completekey, stdin, stdout)
        self.prompt = "Pyglow: "

    ## A few decorators and utilities
    def foolproof(func):
        """Decorator to handle cases where an argument input is invalid."""
        def fooltest(self, args):
            try:
                return func(self, args)
            except ValueError:
                print("Error: something is wrong with the supplied arguments.")
            except PyGlowError as error:
                print(error.message)

        return fooltest

    def noargs(func):
        """Decorator for no argument commands."""
        def args_check(self, args):
            if args == "":
                return func(self, args)
            else:
                print("Error: this command takes no argument.")

        return args_check

    def printhelp(func):
        def print_func_help(self):
            f = func(self)
            signature = f.func_name
            argcount = f.func_code.co_argcount

            if f.func_code.co_argcount > 0:
                argument_names = f.func_code.co_varnames
                if argument_names[0] == "self":
                    start = 1
                else:
                    start = 0
                # 'co_varnames' include all variables of the code object.
                # We only need those that are arguments of the function.
                argument_names = argument_names[start:argcount]
                for arg in argument_names:
                    signature = signature + " <" + arg + ">"

            print("\n" + signature + "\n" + f.func_doc + "\n")

        return print_func_help

    def notimplemented(func):
        """Decorator for not implemented commands."""
        def nothing(self, args):
            print("This functionnality has not been implemented yet.")
            pass

        return nothing

    @staticmethod
    def two_args(func, args):
        """For commands that take two arguments, the first being and ID."""
        arguments = args.split()
        if len(arguments) != 2:
            print("Error this command takes two arguments.")
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
        print("Welcome to the PyGlow interpreter. Type 'help' if you don't know what to do.")
        Cmd.preloop(self)

    def postloop(self):
        Cmd.postloop(self)

    ## Commands
    @foolproof
    def do_all(self, args):
        brightness = int(args)
        self.__piglow.all(brightness)

    @printhelp
    def help_all(self):
        return self.__piglow.all

    @foolproof
    def do_led(self, args):
        PyGlowCmd.two_args(self.__piglow.led, args)

    @printhelp
    def help_led(self):
        return self.__piglow.led

    @foolproof
    def do_arm(self, args):
        PyGlowCmd.two_args(self.__piglow.arm, args)

    @printhelp
    def help_arm(self):
        return self.__piglow.arm

    @foolproof
    def do_ring(self, args):
        PyGlowCmd.two_args(self.__piglow.ring, args)

    @printhelp
    def help_ring(self):
        return self.__piglow.ring

    @foolproof
    def do_color(self, args):
        PyGlowCmd.two_args(self.__piglow.color, args)

    @printhelp
    def help_color(self):
        return self.__piglow.color

    @notimplemented
    def do_ledset(self, args):
        pass

    @printhelp
    def help_ledset(self):
        return self.__piglow.ledset

    @notimplemented
    def do_buffer(self, args):
        pass

    @printhelp
    def help_buffer(self):
        return self.__piglow.buffer

    @noargs
    @notimplemented
    def do_dump(self, args):
        pass

    @printhelp
    def help_dump(self):
        return self.__piglow.dump

    @noargs
    @notimplemented
    def do_restore(self, args):
        pass

    @printhelp
    def help_restore(self):
        return self.__piglow.restore

    @noargs
    def do_update(self, args):
        self.__piglow.update()

    @printhelp
    def help_update(self):
        return self.__piglow.update

    @noargs
    def do_off(self, args):
        self.__piglow.off()

    @printhelp
    def help_off(self):
        return self.__piglow.off

    @noargs
    def do_up_to_date(self, args):
        print(self.__piglow.up_to_date())

    @printhelp
    def help_up_to_date(self):
        return self.__piglow.up_to_date

    @noargs
    def do_exit(self, args):
        return True

    def help_exit(self):
        print("Exit the interpreter.")

if __name__ == '__main__':
    interpreter = PyGlowCmd()
    interpreter.cmdloop()
