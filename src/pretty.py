import shutil                       
from colorama import Fore, Style
import os

VERSION = 1.0

LOGGED_IN_SMTP = ""
LOGGED_IN_POP3 = ""
LOGGED_IN_IMAP = ""
LOGGED_IN_WITH = ', '.join(['NOT LOGGED IN' if s == '' else s for s in [LOGGED_IN_SMTP, LOGGED_IN_POP3, LOGGED_IN_IMAP]])

def printLogo(color: str):
    text_color = getattr(Fore, color.upper())
 
    logo = f"""{text_color}
                 _______  _     _  ___       _______  _______  _______  _______                
                |xxxxxxx||x|   |x||xxx|     |xxxxxxx||xxxxxxx||xxxxxxx||xxxxxxx|                
                |xxxxxxx||x| _ |x||xxx|     |xxxxxxx||xxxxxxx||xxxxxxx||xxxxxxx|                
   .___,        |xx| |xx||x||x||x||xxx|     |xxx|_|x||xx| |xx||x|_____   |xxx|          .___,   
___('v')___     |xx|_|xx||xxxxxxx||xxx|___  |xxxxxxx||xx|_|xx||xxxxxxx|  |xxx|       ___('v')___
`"-\._./-"'     |xxxxxxx||xxxxxxx||xxxxxxx| |xxx|    |xxxxxxx| _____|x|  |xxx|       `"-\._./-"'
    ^ ^         |xxxxxxx||xx| |xx||xxxxxxx| |xxx|    |xxxxxxx||xxxxxxx|  |xxx|           ^ ^    
{Style.RESET_ALL}{text_color}{Style.RESET_ALL}""" 

    os.system("cls")
    print(f"{text_color}{makeBold('Version')} {text_color}{VERSION}   {text_color}{makeBold('Github:')} {text_color}https://github.com/MessyToilet/PostOwl")
    printCentered(logo)

def printOptions(color: str):
    text_color = getattr(Fore, color.upper())
    text_color_padding = makePadding(text_color)

    NONE_STRNG = ""
    SMTP_HEADER, POP3_HEADER, IMAP_HEADER = "~ SMTP OPTIONS ~", "~ POP3 OPTIONS ~", "~ IMAP OPTIONS ~"
    SMTP_CONFIG, POP3_CONFIG, IMAP_CONFIG = " [1.0]  SMTP Config                  ", " [2.0]  POP3 Config                  ", " [3.0]  IMAP Config"
    SMTP_MAILUS, POP3_MAILUS, IMAP_MAILUS = " [1.1]  Mail user            (target)", " [2.1]  Mail user            (target)", " [3.1]  Mail user            (target)"
    SMTP_MAILLI, POP3_MAILLI, IMAP_MAILLI = " [1.2]  Mail users             (list)", " [2.2]  Mail users             (list)", " [3.2]  Mail users             (list)"
    SMTP_RANDUS, POP3_RANDUS, IMAP_RANDUS = " [1.3]  Mail random            (list)", " [2.3]  Mail random            (list)", " [3.3]  Mail random            (list)"
    SMTP_RANDLI, POP3_RANDLI, IMAP_RANDLI = " [1.4]  Mail randoms           (list)", " [2.4]  Mail randoms           (list)", " [3.4]  Mail randoms           (list)"
    SMTP_RANDDO, POP3_RANDDO, IMAP_RANDDO = " [1.5]  Mail random          (domain)", " [2.5]  Mail random          (domain)", " [3.5]  Mail random          (domain)"
    SMTP_RANDDL, POP3_RANDDL, IMAP_RANDDL = " [1.6]  Mail randoms         (domain)", " [2.6]  Mail randoms         (domain)", " [3.6]  Mail randoms         (domain)"
    SMTP_BOMBUS, POP3_BOMBUS, IMAP_BOMBUS = " [1.7]  Mail bomb user       (target)", " [2.7]  Mail bomb user       (target)", " [3.7]  Mail bomb user       (target)"
    SMTP_BOMBLI, POP3_BOMBLI, IMAP_BOMBLI = " [1.8]  Mail bomb users        (list)", " [2.8]  Mail bomb users        (list)", " [3.8]  Mail bomb users        (list)"
    SMTP_BOMBRA, POP3_BOMBRA, IMAP_BOMBRA = " [1.9]  Mail bomb random       (list)", " [2.9]  Mail bomb random       (list)", " [3.9]  Mail bomb random       (list)"
    SMTP_BORAUS, POP3_BORAUS, IMAP_BORAUS = " [.10]  Mail bomb randoms      (list)", " [.10]  Mail bomb randoms      (list)", " [.10]  Mail bomb randoms      (list)"
    SMTP_BORADO, POP3_BORADO, IMAP_BORADO = " [.10]  Mail bomb random     (domain)", " [.10]  Mail bomb random     (domain)", " [.10]  Mail bomb random     (domain)"
    SMTP_BORADS, POP3_BORADS, IMAP_BORADS = " [.10]  Mail bomb randoms    (domain)", " [.10]  Mail bomb randoms    (domain)", " [.10]  Mail bomb randoms    (domain)"

    interface = f"""{text_color_padding}{text_color}╔{NONE_STRNG:═^38}╗ ╔{NONE_STRNG:═^38}╗ ╔{NONE_STRNG:═^38}╗
║{SMTP_HEADER:^38}║ ║{POP3_HEADER:^38}║ ║{IMAP_HEADER:^38}║
╠{NONE_STRNG:═^38}╣ ╠{NONE_STRNG:═^38}╣ ╠{NONE_STRNG:═^38}╣
║{NONE_STRNG: ^38}║ ║{NONE_STRNG: ^38}║ ║{NONE_STRNG: ^38}║
║{SMTP_CONFIG:<38}║ ║{POP3_CONFIG:<38}║ ║{IMAP_CONFIG:<38}║
║{SMTP_MAILUS:<38}║ ║{POP3_MAILUS:<38}║ ║{IMAP_MAILUS:<38}║
║{SMTP_MAILLI:<38}║ ║{POP3_MAILLI:<38}║ ║{IMAP_MAILLI:<38}║
║{SMTP_RANDUS:<38}║ ║{POP3_RANDUS:<38}║ ║{IMAP_RANDUS:<38}║
║{SMTP_RANDLI:<38}║ ║{POP3_RANDLI:<38}║ ║{IMAP_RANDLI:<38}║
║{SMTP_RANDDO:<38}║ ║{POP3_RANDDO:<38}║ ║{IMAP_RANDDO:<38}║
║{SMTP_RANDDL:<38}║ ║{POP3_RANDDL:<38}║ ║{IMAP_RANDDL:<38}║
║{SMTP_BOMBUS:<38}║ ║{POP3_BOMBUS:<38}║ ║{IMAP_BOMBUS:<38}║
║{SMTP_BOMBLI:<38}║ ║{POP3_BOMBLI:<38}║ ║{IMAP_BOMBLI:<38}║
║{SMTP_BOMBRA:<38}║ ║{POP3_BOMBRA:<38}║ ║{IMAP_BOMBRA:<38}║
║{SMTP_BORAUS:<38}║ ║{POP3_BORAUS:<38}║ ║{IMAP_BORAUS:<38}║
║{SMTP_BORADO:<38}║ ║{POP3_BORADO:<38}║ ║{IMAP_BORADO:<38}║
║{SMTP_BORADS:<38}║ ║{POP3_BORADS:<38}║ ║{IMAP_BORADS:<38}║
║{NONE_STRNG: ^38}║ ║{NONE_STRNG: ^38}║ ║{NONE_STRNG: ^38}║
╚{NONE_STRNG:═^38}╝ ╚{NONE_STRNG:═^38}╝ ╚{NONE_STRNG:═^38}╝"""

    printCentered(interface)

# HELPER FUNCTIONS
    
def chosenColor(color: str) -> str:
    supportedColors = ["BLACK", "RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN", "WHITE", "RESET", "LIGHTBLACK_EX", "LIGHTRED_EX", "LIGHTGREEN_EX", "LIGHTYELLOW_EX", "LIGHTBLUE_EX", "LIGHTMAGENTA_EX", "LIGHTCYAN_EX", "LIGHTWHITE_EX"]

    if color.upper() not in supportedColors:
        print(f"ERROR: unsupported color given, supported colors:\n{supportedColors}")

    return color if color.upper() in supportedColors else "white"

def printCentered(str: str):
    terminal_size = shutil.get_terminal_size()
    lines = str.split('\n')
    centered_lines = [(line.center(terminal_size.columns, ' ') if len(line.strip()) > 0 else ' ' * terminal_size.columns) for line in lines]
    print('\n'.join(centered_lines))

def makeBold(str: str) -> str:
    return f'\033[1m{str}\033[0m'

def numberBoarder(num: str) -> str:
    return f'{Fore.YELLOW}[{Fore.GREEN}{num}{Fore.YELLOW}]{Fore.RESET}'

def makePadding(str: str) -> str:
    return " " * len(str)