import os
import argparse
import Package
import ToolChaine
from Project import Project

def init(args) -> None:
    print(f"Initialising new project : {args.name} by {args.owner}")
    print(f"Path to the project : {args.path}")
    print(f"Git repository : {args.repo}")
    project = Project(args.name, args.repo, args.owner)
    project.create()
    if args.git_init: 
        print("Initialising local git folder")
        project.init_git_repo()

def add(args) -> None:
    Package.add(args.author, args.name)

def remove(args) -> None:
    Package.remove(args.name)

def install(args) -> None:
    Package.install_root()

def doc(args) -> None:
    Package.load_doc(args.package)

def build(args) -> None:
    ToolChaine.build(args.config)

def run(args) -> None:
    ToolChaine.run(args.config)

def bakasable() -> None:
    program_parser = argparse.ArgumentParser(prog="bakasable", description="baka developpement enviromment")
    program_parser.add_argument("-p", "--path", type=str, default="./", dest="path", help="path to the project")
    sub_parsers = program_parser.add_subparsers(title="subcommmands", help="operations on your project")

    init_parser = sub_parsers.add_parser("init", help="initialise a new project")
    init_parser.add_argument("-n", "--name", type=str, required=True, dest="name", help="name of your")
    init_parser.add_argument("-r", "--repo", type=str, default="", dest="repo", help="git repository where project is stored")
    init_parser.add_argument("-o", "--owner", type=str, default="", dest="owner", help="owner of the project")
    init_parser.add_argument("-g", "--git-init", action="store_const", const=True, default=False, dest="git_init", help="initialise a local git folder")
    init_parser.set_defaults(func=init)

    add_parser = sub_parsers.add_parser("add", help="add a module to your project from github")
    add_parser.add_argument("-n", "--name", type=str, required=True, dest="name", help="name of the github repository")
    add_parser.add_argument("-a", "--author", type=str, required=True, dest="author", help="name of the github user")
    add_parser.set_defaults(func=add)

    remove_parser = sub_parsers.add_parser("remove", help="remove a module from your project")
    remove_parser.add_argument("-n", "--name", type=str, required=True, dest="config", help="name of the github repository")
    remove_parser.set_defaults(func=remove)

    install_parser = sub_parsers.add_parser("install", help="installs the dependencies of your project")
    install_parser.set_defaults(func=install)

    build_parser = sub_parsers.add_parser("build", help="")
    build_parser.add_argument("-c", "--config", type=str, required=True, dest="config", help="", choices=["Debug", "Release"])
    build_parser.set_defaults(func=build)

    run_parser = sub_parsers.add_parser("run", help="")
    run_parser.add_argument("-c", "--config", type=str, required=True, dest="config", help="", choices=["Debug", "Release"])
    run_parser.set_defaults(func=run)

    args = program_parser.parse_args()
    if not os.path.exists(args.path): os.mkdir(args.path)
    os.chdir(args.path)
    args.func(args)

if __name__ == "__main__":
    print(
""" 
 ____    _    _  __    _    ____    _    ____  _     _____ 
| __ )  / \\  | |/ /   / \\  / ___|  / \\  | __ )| |   | ____|
|  _ \\ / _ \\ | ' /   / _ \\ \\___ \\ / _ \\ |  _ \\| |   |  _|  
| |_) / ___ \\| . \\  / ___ \\ ___) / ___ \\| |_) | |___| |___ 
|____/_/   \\_\\_|\\_\\/_/   \\_\\____/_/   \\_\\____/|_____|_____|        
""")
    bakasable()