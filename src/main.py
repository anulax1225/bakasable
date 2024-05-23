import os
import sys
from Buildtools import verifie_tools
from Project import Project

def setup() -> None:
    if len(sys.argv) >= 2:
        if not os.path.exists(sys.argv[1]): os.mkdir(sys.argv[1])
        os.chdir(sys.argv[1])
    verifie_tools()
    project: Project = Project("Test")
    project.create()


if __name__ == "__main__":
    setup()