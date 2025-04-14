# pyitercsv/pyitercsv.py

import csv
import os
import argparse

def load_file_command(f):
    
    res = []
    
    f = open(f, "r")
    for l in f:
        res.append(l.rstrip())
    f.close()
    
    return res


def load_file(f, delimiter=","):
    
    res = []
    
    f = open (f, "r")
    r = csv.reader(f, delimiter=delimiter)
    for l in r:
        res.append(l)
    
    f.close()
    
    return res

def run_list(command, csv_list, e) :
    
    cols = len(csv_list[0])
    
    if type(command) == str:
        command = [command]
    
    qty = len(csv_list)
    c = 0
    
    for l in csv_list:
        c = c + 1
        print ("c/qty", c, "/", qty)
        for cn in command:
            
            t = cn
            for col_n in range(0,cols):
                t = t.replace("#" + str(col_n+1) + "#", l[col_n])
            
            print(t)
            if e == True:
                os.system(t)
                
            
def main():
    
    parser = argparse.ArgumentParser(
        description='My first argparse attempt',
        epilog=""" Example of use | pyitercsv.py -s "echo '#1#' -l file.csv -e" #this prints element of col 1 | or | pyitercsv.py -s "echo '#2#' -l file.csv -e #this prints element of col 2""")
    parser.add_argument('-l', '--filelist', help='filename csv')
    parser.add_argument('-s', '--stringcommand', help='string to execute with #con_number# in the string')
    parser.add_argument('-f', '--filecommand', help='file with string to execute with #col_number# in the strings')
    parser.add_argument('-e', '--execute', help='execute commands, add this option when you are sure what you are going to do', action='store_true')
    parser.add_argument('-d', '--delimiter', help='delimiter default is,')
    args = parser.parse_args()
    
    l = []
    
    execute = False
    
    if args.execute is not None:
        if args.execute == True:
            execute = True
    
    delimiter = ','
    if args.delimiter is not None:
        if type(args.delimiter) == str:
            print ("new delimiter", args.delimiter)
            delimiter = args.delimiter
    
    if args.filelist is not None:
        if type(args.filelist) == str:
            print ("read list", args.filelist)
            l = load_file(args.filelist, delimiter)
            
    if args.stringcommand is not None:
        if type(args.stringcommand) == str:
            print("stringcommand", args.stringcommand)
            if len(l)>0:
                run_list(args.stringcommand, l, execute)
            else:
                print("list is empty")

    if args.filecommand is not None:
        if type(args.filecommand) == str:
            
            print("filecommand", args.filecommand)
            fc = load_file_command(args.filecommand)
            print ("filecommand", fc)
            
            if len(l)>0:
                run_list(fc, l, execute)
            else:
                print("list is empty")

if __name__ == '__main__':
    main()
    
