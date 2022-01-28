# easy colouring for terminal prompts...
import colorama
from colorama import Fore, Back, Style

colorama.init()

def cyan(word):

    return(" " + Style.BRIGHT + Fore.CYAN + str(word) + Style.RESET_ALL + " ")
