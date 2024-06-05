import shutil
import stat
import os
import json
import Command
import ToolChaine
import webbrowser
import Log

def config(package):
    Log.info(f"Reconfiguring package {package}")
    if os.path.exists(f"./vendor/{package}/dependencies"):
        dep = open(f"./vendor/{package}/dependencies", "r")
        pkg_deps = dep.read()
        dep.close()
        if not os.path.exists("./dependencies.lua"):
            dep = open("./dependencies.lua", "w")
            dep.write("IncludeDirs = {}")
            dep.write("\n" + pkg_deps)
            dep.close()
        else:
            dep = open(f"./dependencies.lua", "a")
            dep.write("\n" + pkg_deps)
            dep.close()

    linker = []
    if os.path.exists(f"./vendor/{package}/package.json"):
        f_conf = open(f"./vendor/{package}/package.json", "r")
        conf = json.loads(f_conf.read())
        f_conf.close()
        linker.append({
            "links": conf["links"],
            "includes": conf["includes"]
        })
        if len(conf["packages"]):
            for pkg in conf["packages"]:
                linker += config(pkg["name"])
    return linker
        


def reconfig():
    Log.info("Reconfiguring build settings :")
    f_conf = open("./package.json", "r")
    conf = json.loads(f_conf.read())
    f_conf.close()
    if os.path.exists("./dependencies.lua"): os.remove("./dependencies.lua")
    if os.path.exists("./app/linker.lua"): os.remove("./app/linker.lua")
    linkers = []
    for package in conf["packages"]:
        linkers += config(package["name"])
    links = "\nlinks\n{\n"
    includes = "\nincludedirs\n{\n"
    for linker in linkers:
        if len(linker["links"]): 
            for link in linker["links"]:
                if len(link): links += '\t"' + link  + '",\n'
        if len(linker["includes"]):
            for include in linker["includes"]:
                if len(include): includes += '\t"%{IncludeDirs.' + include + '}",\n'
    links += "}\n"
    includes += "}\n"
    f_linker= open("./app/linker.lua", "w")
    f_linker.write(includes + links)
    f_linker.close()

def install(author, package) -> None:
    Log.info(f"Installing package {package}") 
    if os.path.exists(f"./vendor/{package}"):
        Log.warning("Package already added")
        return 
    if not ToolChaine.tool_exist("git"):
        Log.error("Tool missing git")
    Command.exec(f"git clone --depth 5 https://github.com/{author}/{package} ./vendor/{package}")
    if os.path.exists(f"./vendor/{package}/package.json"): 
        conf = open(f"./vendor/{package}/package.json", "r").read()
        conf = json.loads(conf)
        if len(conf["packages"]) > 0:
            for pkg in conf["packages"]:
                install(pkg["author"], pkg["name"])

def add(author, package) -> None:    
    f_conf = open("./package.json", "r")
    conf = json.loads(f_conf.read())
    f_conf.close()
    if package in conf["packages"]: Log.error("Package already added")
    f_conf = open("./package.json", "w")
    conf["packages"].append({ "author": author, "name": package})
    f_conf.write(json.dumps(conf, indent=4))
    f_conf.close()

    install(author, package)
    reconfig()

def update(package) -> None:
    Log.info(f"Updating package {package}")
    if not os.path.exists(f"./vendor/{package}"): Log.error("Package not found")
    os.chdir(f"./vendor/{package}")
    Command.exec("git pull")
    reconfig()

def save(package, message) -> None:
    Log.info(f"Saving package {package}")
    if not os.path.exists(f"./vendor/{package}"): Log.error("Package not found")
    os.chdir(f"./vendor/{package}")
    Command.exec("git add .")
    Command.exec(f'git commit -m "{message}"')
    Command.exec("git push")

def remove(package) -> None:
    f_conf = open("./package.json", "r")
    conf = json.loads(f_conf.read())
    f_conf.close()
    conf["packages"] = [pkg for pkg in conf["packages"] if pkg['name'] != package]
    r_remove(package)
    f_conf = open("./package.json", "w")
    f_conf.write(json.dumps(conf, indent=4))
    f_conf.close()
    reconfig()

def r_remove(package) -> None:  
    Log.info(f"Removing package {package}") 
    if not os.path.exists(f"./vendor/{package}/") : Log.error(f"Package {package} not the dependencies")  
    if os.path.exists(f"./vendor/{package}/package.json") :
        r_pkgs = json.loads(open(f"./vendor/{package}/package.json", "r").read())["packages"]
        for r_pkg in r_pkgs:
            r_remove(r_pkg["name"])
    os.chmod(f"./vendor/{package}/", stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)
    shutil.rmtree(f"./vendor/{package}/", ignore_errors=True)

def install_root() -> None:
    Log.info("Reinstalling all packages :")
    if not os.path.exists("./package.json"):
        Log.error("No package config file")
    f_conf = open("./package.json", "r")
    conf = json.loads(f_conf.read())
    f_conf.close()
    for pkg in conf["packages"]:
        install(pkg["author"], pkg["name"]) 
    reconfig()

def load_doc(package) -> None:
    if not ToolChaine.tool_exist("doxygen"):
        Log.error("Tool missing doxygen")
    if not os.path.exists(f"./vendor/{package}/Doxyfile"):
        Log.error("Doxygen config file not found")
    Command.exec(f"doxygen ./vendor/{package}")
    webbrowser.open("file://" + os.path.realpath(f"./vendor/{package}/docs/html/index.html"))