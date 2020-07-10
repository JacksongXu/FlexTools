#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Brief:
#   This tool is used to convert hex array file to bin file.
#
# Author : Jackson Xu
# Date   : 2020.7.8
# Version: 1.0

import os, re
import sys, getopt
from struct import *

def c_array_to_bin(c_array_file, bin_file):
    _bin = ''

    try:
        with open(c_array_file,'r') as cf:
            for line in cf:
                regex = r"0[xX]"
                while True:
                    match = re.search(regex, line)
                    if match == None:
                        break

                    pos = match.start()
                    b = int(line[pos+2:pos+4],16) #get hex data
                    _bin += pack('B',b)           #packet hex as bin data
                    line = line[pos+1:]           #fetch next hex data
    except IOError:
        print('Error: open {0} failed'.format(c_array_file))
        sys.exit(2)
    
    with open(bin_file,'wb') as bf:
        bf.write(_bin)


def print_usage(error_str):
    print('{0}:\n\
         Usage: C2B.py -i <inputfile> -o <outputfile>'.format(error_str)
         )

def main(argv):
   inputfile = ''
   outputfile = ''
   
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print_usage('Ivalid parameters')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg

   if inputfile == '' or outputfile == '':
        print_usage('No inputfile or outputfile parameter')
        sys.exit(2)
   
   print('\nConverting {0} to {0}'.format(inputfile, outputfile))
   c_array_to_bin(inputfile, outputfile)
   print 'B2C finished!'


if __name__ == "__main__":
   main(sys.argv[1:])
