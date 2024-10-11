import platform
import os
import json
import Command
import Log

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
    Log.info(f"Verifing build tools")
    none_tools: str = []
    match platform.system():
        case "Windows": 
            none_tools = search_tools(["git", "premake5"])
        case "Linux":
            none_tools = search_tools(["git", "g++", "premake5", "make"])
        case _:
            Log.error("Platform not supported")
    if len(none_tools) > 0:
        Log.error(f"Tools missing {none_tools}")

def run(config) -> None:
    Log.info("Running app")
    Log.info(f"./bin/{platform.system().lower()}-{platform.machine().lower()}-{config}/App/App")
    if not os.path.exists(f"./bin/{platform.system().lower()}-{platform.machine().lower()}-{config}/App/App"): 
        Log.error("Executable not found")
    Command.exec(f"chmod +x ./bin/{platform.system().lower()}-{platform.machine().lower()}-{config}/App/App && ./bin/{platform.system().lower()}-{platform.machine().lower()}-{config}/App/App")


def build(config) -> None:
    Log.info(f"Starting build with config {config}")
    verifie_build_tools()
    match platform.system():
        case "Windows": 
            Command.exec("premake5 vs2022")
            Log.info("Build with vscode 2022")
        case "Linux":
            Command.exec("premake5 gmake2")
            Command.exec("premake5 export-compile-commands")
            Command.exec(f"mv ./compile_commands/{config.lower()}.json ./compile_commands.json")
            Command.exec(f"make config={config.lower()}")
        case _:
            Log.error("Platform not supported")
    Log.info("Finished build")
    
   