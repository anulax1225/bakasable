import os
import sys
import argparse
import Package
from Buildtools import verifie_tools
from Project import Project

def init(args) -> None:
    if not os.path.exists(args.path): os.mkdir(args.path)
    os.chdir(args.path)
    project = Project(args.name, args.repo, args.owner)
    project.create()

def add(args) -> None:
    Package.add(args.author, args.name)

def install(args) -> None:
    Package.install_root()

def bakasable() -> None:
    program_parser = argparse.ArgumentParser(prog="bakasable", description="baka developpement enviromment")
    sub_parsers = program_parser.add_subparsers(title="subcommmands", help="operations on your project")

    init_parser = sub_parsers.add_parser("init", help="initialise a new project")
    init_parser.add_argument("-n", "--name", type=str, required=True, dest="name")
    init_parser.add_argument("-p", "--path", type=str, default="./", dest="path")
    init_parser.add_argument("-r", "--repo", type=str, default="", dest="repo")
    init_parser.add_argument("-o", "--owner", type=str, default="", dest="owner")
    init_parser.set_defaults(func=init)

    add_parser = sub_parsers.add_parser("add", help="add a module to your project")
    add_parser.add_argument("-n", "--name", type=str, required=True, dest="name")
    add_parser.add_argument("-a", "--author", type=str, required=True, dest="author")
    add_parser.set_defaults(func=add)

    install_parser = sub_parsers.add_parser("install", help="add a module to your project")
    install_parser.set_defaults(func=install)

    args = program_parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    print(""" ____    _    _  __    _    ____    _    ____  _     _____ 
| __ )  / \\  | |/ /   / \\  / ___|  / \\  | __ )| |   | ____|
|  _ \\ / _ \\ | ' /   / _ \\ \\___ \\ / _ \\ |  _ \\| |   |  _|  
| |_) / ___ \\| . \\  / ___ \\ ___) / ___ \\| |_) | |___| |___ 
|____/_/   \\_\\_|\\_\\/_/   \\_\\____/_/   \\_\\____/|_____|_____|        
""")
    bakasable()