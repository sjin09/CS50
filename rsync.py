#!/usr/bin/env python

import os
from datetime import date, time, datetime

## init
today = date.today()
day = today.strftime("%d_%b_%Y")

## main
os.system("rsync -rv ubuntu@compsci:/home/ubuntu/02.CS50/ /Users/sl17/Github/CS50/pset")
os.system("git add .")
os.system("git commit -m {}".format(day))
os.system("git push")

