import os
import sys
from Log import ShColors
def exec(command):
    print(ShColors.OKGREEN)
    os.system(f"{command}")
    print(ShColors.ENDC)
