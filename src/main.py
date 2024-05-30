import os
import sys
import Package
from Buildtools import verifie_tools
from Project import Project

def bakasable() -> None:
    if len(sys.argv) >= 2:
        if not os.path.exists(sys.argv[1]): os.mkdir(sys.argv[1])
        os.chdir(sys.argv[1])
    project = Project("Test")
    project.create()
    Package.add("anulax1225", "bakatools")


if __name__ == "__main__":
    print(""" ____    _    _  __    _    ____    _    ____  _     _____ 
| __ )  / \\  | |/ /   / \\  / ___|  / \\  | __ )| |   | ____|
|  _ \\ / _ \\ | ' /   / _ \\ \\___ \\ / _ \\ |  _ \\| |   |  _|  
| |_) / ___ \\| . \\  / ___ \\ ___) / ___ \\| |_) | |___| |___ 
|____/_/   \\_\\_|\\_\\/_/   \\_\\____/_/   \\_\\____/|_____|_____|        
    """)
    bakasable()