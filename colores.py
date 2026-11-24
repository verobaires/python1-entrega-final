from colorama import init, Fore

init(autoreset=True)


def exito(mensaje):
    print(Fore.GREEN + "[OK👍🏻] " + mensaje)


def error(mensaje):
    print(Fore.RED + "[ERROR😥] " + mensaje)
