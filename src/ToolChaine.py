import platform
import os
import json
import Command

def tool_exist(name: str) -> bool:
    from shutil import which
    return which(name) is not None

def search_tools(tools: str) -> str:
    none_tools: str = []
    for tool in tools:
        if not tool_exist(tool):
            none_tools.append(tool) 
    return none_tools

def verifie_build_tools() -> None:
    none_tools: str = []
    match platform.system():
        case "Windows": 
            none_tools = search_tools(["git", "dotnet", "premake5"])
        case "Linux":
            none_tools = search_tools(["git", "g++", "premake5", "make"])
        case _:
            raise Exception("Platform not supported")
    if len(none_tools) > 0:
        raise Exception(f"Tools missing {none_tools}")

def run(config) -> None:
    if not os.path.exists("./config.json"): raise Exception("Project not found")
    conf = json.loads(open("./config.json").read())
    name = conf["name"].lower()
    print(f"./bin/{platform.system().lower()}-{platform.machine().lower()}-{config.lower()}/{name}/{name}")
    if not os.path.exists(f"./bin/{platform.system().lower()}-{platform.machine().lower()}-{config.lower()}/{name}/{name}"): 
        raise Exception("Executable not found")
    Command.exec(f"./bin/{platform.system().lower()}-{platform.machine().lower()}-{config.lower()}/{name}/{name}")


def build(config) -> None:
    verifie_build_tools()
    match platform.system():
        case "Windows": 
            Command.exec("premake5 vs2022")
            Command.exec("dotnet build")
        case "Linux":
            Command.exec("premake5 gmake2")
            Command.exec("make")
        case _:
            raise Exception("Platform not supported")
   