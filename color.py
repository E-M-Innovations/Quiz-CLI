from termcolor import cprint
import sys

def eprint(string): 
    """
    Prints error-related text in bold red to stderr 

    Args: 
        string (str): The text to print to stderr
    """
    cprint(string, "red", attrs=["bold"], file=sys.stderr)

def nprint(string): 
    """
    Prints neutral text in yellow 

    Args: 
        string (str): The text to print to stdout 
    """

    cprint(string, "light_blue")

def hprint(string): 
    """
    Prints header text in bold light blue 
    Args: 
        string (str): The text to print to stdout 
    """
    cprint(string, "light_blue", attrs=["bold"])

def sprint(string): 
    """
    Prints successful text in green 

    Args: 
        string (str): Th text to print to stdout 
    """
    cprint(string, "green", attrs=["bold"])