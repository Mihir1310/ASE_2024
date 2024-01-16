"""
gate: guess, assess, try, expand
(c) 2023, Tim Menzies, BSD-2
Learn a little, guess a lot, try the strangest guess, repeat

USAGE:
  python3 gate.py [OPTIONS]

OPTIONS:
  -c --cohen  small effect size               = .35
  -f --file   csv data file name              = '../data/diabetes.csv'
  -h --help   show help                       = False
  -k --k      low class frequency kludge      = 1
  -m --m      low attribute frequency kludge  = 2
  -s --seed   random number seed              = 31210
  -t --todo   start up action                 = 'help' """

import re, sys, csv
from DATA import DATA
from COLS import COLS
from ROW import ROW
from typing import List
from ast import literal_eval as val
from fileinput import FileInput as file_or_stdin

def cli():
    x = sys.argv[1:]
    i=0
    while(i<len(x)):
        if x[i] == "-f":
            csv_path = x[i+1]
            with open(csv_path, mode='r') as file:
                csv_file = csv.reader(file)

                data = DATA([])
                data.cols = COLS(ROW(next(csv_file, None)))

                for lines in csv_file:
                    for idx in range(len(lines)):
                        if lines[idx] == '?':
                            lines[idx] = '0'
                    lines = [eval(i) for i in lines]
                    data.add(lines)
            i += 1
        elif x[i] == "-t":
            func_name = x[i+1]
            if func_name == "stats":
                print(data.stats())
            elif func_name == "small":
                print(data.small())
            elif func_name == "div":
                print(data.div())
            elif func_name == "mid":
                print(data.mid())
            elif func_name == "add":
                print(data.add())
            elif func_name == "all":
                print(data.small())
                print(data.div())
                print(data.mid())
                print(data.add())
                print(data.stats())
                
        i += 1
    return
the = cli()

# ---------------------------------------------------------------------------
print(the)
