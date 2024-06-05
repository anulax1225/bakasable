class ShColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def logo() -> None:
    print(
f""" 
 {ShColors.BOLD}____    _    _  __    _    ____    _    ____  _     _____ 
| __ )  / \\  | |/ /   / \\  / ___|  / \\  | __ )| |   | ____|
|  _ \\ / _ \\ | ' /   / _ \\ \\___ \\ / _ \\ |  _ \\| |   |  _|  
| |_) / ___ \\| . \\  / ___ \\ ___) / ___ \\| |_) | |___| |___ 
|____/_/   \\_\\_|\\_\\/_/   \\_\\____/_/   \\_\\____/|_____|_____|        
{ShColors.ENDC}""")

def info(message) -> None:
    print(f"{ShColors.OKGREEN}[INFO] {message}{ShColors.ENDC}")

def warning(message) -> None:
    print(f"{ShColors.WARNING}[WARNING] {message}{ShColors.ENDC}")

def error(message) -> None:
    print(f"{ShColors.FAIL}[ERROR] {ShColors.UNDERLINE}{message}{ShColors.ENDC}")
    exit(1)