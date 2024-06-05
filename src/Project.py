import os
import json
import Premake
import Command

class Builder:
    def __init__(self, conf) -> None:
        self.owner = conf["owner"]
        self.name = conf["name"]
        self.git_repo = conf["git"]

    def __init__(self, name, repo, author = "") -> None:
        self.name = name
        self.owner = author
        self.git_repo = repo

    def set_git_repo(self, url) -> None:
        self.git_repo = url

    def create(self) -> None:
        self.create_folder()
        self.config()

    def config(self) -> None:
        conf = {
            "name": self.name,
            "owner": self.owner,
            "git": self.git_repo,
            "packages": []
        }
        file_conf = open("./package.json", "w")
        file_conf.write(json.dumps(conf, indent=4))
        file_conf.close()
        wks = open("./premake5.lua", "w")
        wks.write(Premake.Wks.get(self.name))
        wks.close()
        app = open("./app/premake5.lua", "w")
        app.write(Premake.App.get())
        app.close()
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
        create_file("./app/src/app.cpp")
        create_file("./premake5.lua")
        create_file("./app/premake5.lua")
        create_file("./package.json")
        create_file("./.gitignore")

    def as_git_repo(self) -> bool:
        return os.path.exists("./.git")

    def init_git_repo(self) -> None:
        if not self.as_git_repo(): return
        Command.exec("git init --initial-branch=main")
        Command.exec("git add .")
        Command.exec('git commit -m "Initial commit"')
        if len(self.git_repo) > 0: Command.exec(f'git remote add origin ${self.git_repo}')
        

def create_file(path) -> None:
    file = open(path, "w")
    file.close()

   
  