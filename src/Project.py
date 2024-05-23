import os
import Premake

class Project:
    def __init__(self, name) -> None:
        self.name = name
        self.git_repo = ""

    def set_git_repo(self, url) -> None:
        self.git_repo = url

    def create(self) -> None:
        self.create_folder()
        self.premake_conf()
        if not self.as_git_repo(): self.init_git_repo()

    def premake_conf(self) -> None:
        wks = open("./premake5.lua", "w")
        wks.write(Premake.Wks.get(self.name))
        wks.close()
        app = open("./app/premake5.lua", "w")
        app.write(Premake.App.get())
        app.close()

    def create_folder(self) -> None:
        try:
            os.mkdir("./app")
            os.mkdir("./vendor")
            os.mkdir("./app/src")
        except: raise Exception("A directory already exists.")
        create_file("./app/src/app.cpp")
        create_file("./premake5.lua")
        create_file("./app/premake5.lua")

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

   
  