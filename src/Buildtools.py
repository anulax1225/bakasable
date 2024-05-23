import platform

def tool_exist(name: str) -> bool:
    from shutil import which
    return which(name) is not None

def search_tools(tools: str) -> str:
    none_tools: str = []
    for tool in tools:
        if not tool_exist(tool):
            none_tools.append(tool) 
    return none_tools

def verifie_tools() -> None:
    none_tools: str = []
    match platform.system():
        case "Windows": 
            none_tools = search_tools(["git"])
        case "Linux":
            none_tools = search_tools(["git"])
        case _:
            raise Exception("Platform not supported")
    if len(none_tools) > 0:
        raise Exception(f"Tools missing {none_tools}")