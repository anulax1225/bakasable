import os
import json
import Premake

class Project:
    def __init__(self, conf) -> None:
        self.owner = conf["owner"]
        self.name = conf["name"]
        self.git_repo = conf["git"]

    def __init__(self, name, author = "") -> None:
        self.owner = author
        self.name = name
        self.git_repo = ""

    def set_git_repo(self, url) -> None:
        self.git_repo = url

    def create(self) -> None:
        self.create_folder()
        self.config()
        if not self.as_git_repo(): self.init_git_repo()

    def config(self) -> None:
        conf = {
            "name": self.name,
            "owner": self.owner,
            "git": self.git_repo,
            "packages": []
        }
        file_conf = open("./config.json", "w")
        file_conf.write(json.dumps(conf, indent=4))
        file_conf.close()
        wks = open("./premake5.lua", "w")
        wks.write(Premake.Wks.get(self.name))
        wks.close()
        app = open("./app/premake5.lua", "w")
        app.write(Premake.App.get())
        app.close()
        dep = open("./deps.lua", "w")
        dep.write("IncludeDirs = {}")
        dep.close()
        git_ign = open("./.gitignore", "w")
        git_ign.write("""/vendor/
/bin/
/bin-int/
/.vscode/
/.vs/
/docs/
**.log
**.sln
**.vcxproj*
**.make
**Makefile
**deps.lua
""")

    def create_folder(self) -> None:
        try:
            os.mkdir("./app")
            os.mkdir("./vendor")
            os.mkdir("./app/src")
        except: raise Exception("Directory already exists.")
        create_file("./dependencies.lua")
        create_file("./deps.lua")
        create_file("./app/src/app.cpp")
        create_file("./premake5.lua")
        create_file("./app/premake5.lua")
        create_file("./config.json")
        create_file("./.gitignore")

    def as_git_repo(self) -> bool:
        return os.path.exists("./.git")

    def init_git_repo(self) -> None:
        os.system("git init --initial-branch=main")
        os.system("git add .")
        os.system('git commit -m "Initial commit"')
        if len(self.git_repo) > 0: os.system(f'git remote add origin ${self.git_repo}')
        

def create_file(path) -> None:
    file = open(path, "w")
    file.close()

   
  