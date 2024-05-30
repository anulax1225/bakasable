import os
import json
import Command

def add(author, package) -> None:    
    f_conf = open("./config.json", "r")
    conf = json.loads(f_conf.read())
    f_conf.close()
    if package in conf["packages"]: raise Exception("Package already added")
    f_conf = open("./config.json", "w")
    conf["packages"].append({ "author": author, "name": package})
    f_conf.write(json.dumps(conf, indent=4))
    f_conf.close()

    install(author, package)

def install_root() -> None:
    if not os.path.exists("./config.json"):
        raise Exception("No package config file")
    f_conf = open("./config.json", "r")
    conf = json.loads(f_conf.read())
    f_conf.close()
    for pkg in conf["packages"]:
        install(pkg["author"], pkg["name"]) 

def install(author, package) -> None:
    if os.path.exists(f"./vendor/{package}"):
        return
    
    Command.exec(f"git clone https://github.com/{author}/{package} ./vendor/{package}")

    if os.path.exists(f"./vendor/{package}/config.json"): 
        conf = open(f"./vendor/{package}/config.json", "r").read()
        conf = json.loads(conf)
        if len(conf["packages"]) > 0:
            for pkg in conf["packages"]:
                install(pkg["author"], pkg["name"])

    if os.path.exists(f"./vendor/{package}/dependencies.lua"):
        dep = open(f"./vendor/{package}/dependencies.lua", "r")
        pkg_deps = dep.read()
        dep.close()
        if not os.path.exists("./deps.lua"):
            dep = open("./deps.lua", "w")
            dep.write("IncludeDirs = {}")
            dep.write("\n" + pkg_deps)
            dep.close()
        else:
            dep = open(f"./deps.lua", "a")
            dep.write("\n" + pkg_deps)
            dep.close()
    

    
    
    