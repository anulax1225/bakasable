import os
import sys
import platform
import numpy as np

def tool_exist(name: str) -> bool:
    from shutil import which
    return which(name) is not None

def search_tools(tools: str) -> str:
    none_tools: str = []
    for tool in tools:
        if not tool_exist(tool):
            none_tools.append(tool) 
    return none_tools

def verifie_tools():
    none_tools: str = []
    match platform.system():
        case "Windows": 
            none_tools = search_tools(["git"])
        case "Linux":
            none_tools = search_tools(["git"])
        case _:
            print("Platform not supported")
            exit(1)
    if len(none_tools) > 0:
        print(f"Tools missing {none_tools}")
        exit(1)

def create_file(path):
    file = open(path, "w")
    file.close()


def setup():
    if len(sys.argv[1]):
        os.chdir(sys.argv[1])
    verifie_tools()
    os.mkdir("./app")
    os.mkdir("./vendor")
    os.mkdir("./app/src")
    create_file("./app/src/app.cpp")
    create_file("./premake5.lua")
    create_file("./app/premake5.lua")

if __name__ == "main":
    setup()