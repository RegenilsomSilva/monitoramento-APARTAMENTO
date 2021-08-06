import os
import pathlib
import glob
from time import time
from time import sleep
import random
from datetime import datetime


print(os.linesep)
targetPatter  = os.path.join(os.getcwd() + os.sep  + '*.xlsx')
emails_em_anexos = glob.glob(targetPatter)

print(os.linesep)
print(str(emails_em_anexos))