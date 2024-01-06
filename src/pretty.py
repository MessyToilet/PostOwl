import shutil                       
from colorama import Fore, Style
import os

VERSION = 1.0

LOGGED_IN_SMTP = ""
LOGGED_IN_POP3 = ""
LOGGED_IN_IMAP = ""
LOGGED_IN_WITH = ', '.join(['NOT LOGGED IN' if s == '' else s for s in [LOGGED_IN_SMTP, LOGGED_IN_POP3, LOGGED_IN_IMAP]])


def printLogo(color:str = 'white'):
    supportedColors = ["BLACK", 
                       "RED", 
                       "GREEN", 
                       "YELLOW", 
                       "BLUE", 
                       "MAGENTA", 
                       "CYAN", 
                       "WHITE", 
                       "RESET", 
                       "LIGHTBLACK_EX", 
                       "LIGHTRED_EX", 
                       "LIGHTGREEN_EX", 
                       "LIGHTYELLOW_EX", 
                       "LIGHTBLUE_EX", 
                       "LIGHTMAGENTA_EX", 
                       "LIGHTCYAN_EX", 
                       "LIGHTWHITE_EX"]

    if color.upper() not in supportedColors:
        print(f"ERROR: unsupported color given, supported colors:\n{supportedColors}")
    else:
        text_color = getattr(Fore, color.upper())
 
    logo = f"""{text_color}
                 _______  _     _  ___       _______  _______  _______  _______                
                |xxxxxxx||x|   |x||xxx|     |xxxxxxx||xxxxxxx||xxxxxxx||xxxxxxx|                
                |xxxxxxx||x| _ |x||xxx|     |xxxxxxx||xxxxxxx||xxxxxxx||xxxxxxx|                
   .___,        |xx| |xx||x||x||x||xxx|     |xxx|_|x||xx| |xx||x|_____   |xxx|          .___,   
___('v')___     |xx|_|xx||xxxxxxx||xxx|___  |xxxxxxx||xx|_|xx||xxxxxxx|  |xxx|       ___('v')___
`"-\._./-"'     |xxxxxxx||xxxxxxx||xxxxxxx| |xxx|    |xxxxxxx| _____|x|  |xxx|       `"-\._./-"'
    ^ ^         |xxxxxxx||xx| |xx||xxxxxxx| |xxx|    |xxxxxxx||xxxxxxx|  |xxx|           ^ ^    
{Style.RESET_ALL}{text_color}\033[1m
By: MessyToilet    Github: https://github.com/MessyToilet/PostOwl
{Style.RESET_ALL}
""" 

    terminal_size = shutil.get_terminal_size()
    lines = logo.split('\n')
    max_length = max(len(line) for line in lines)
    centered_lines = [(line.center(terminal_size.columns, ' ') if len(line.strip()) > 0 else ' ' * terminal_size.columns) for line in lines]
    
    os.system("cls")
    print(f"{text_color}\033[1mVersion {text_color}{VERSION}   {text_color}Logged in with: {text_color}{LOGGED_IN_WITH}\033[0m")
    print('\n'.join(centered_lines))
