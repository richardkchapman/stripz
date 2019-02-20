#!/usr/bin/env python

from __future__ import print_function
import sys
import os
import re
import argparse

def isZonly(line):
  return re.match('[Gg][01][Zz][0-9]*[.]?[0-9]*([Ff[0-9]+[.]?[0-9+])?', line)

def checkRelative(line):
  global relative
  if line.lower().startswith('g91'):
    relative = True
    if verbose:
      print('Entering relative mode')
  elif line.lower().startswith('g90'):
    relative = False
    if verbose:
      print('Entering absolute mode')

def stripz(inputFile, outputFile):
  f1 = open(inputFile, 'r')
  f2 = open(outputFile, 'w')
  pending = None
  stripping = False
  relative = False
  stripped = 0

  for line in f1:
    checkRelative(line)
    if isZonly(line) and not relative:
      if pending:
        if verbose:
          print ('-%s' % (pending), end='')
        stripping = True
        stripped = stripped+1
      pending=line
    else:
      if pending:
        if verbose and stripping:
          print (' %s' % (pending))
        stripping = False
        f2.write(pending)
        pending = None
      f2.write(line)
  f1.close()
  f2.close()
  return stripped

files = []
verbose = False
for inputFile in sys.argv[1:]:
  if inputFile == '-v':
    verbose = True
  else:
    files.append(inputFile)

for inputFile in files: 
  base,ext = os.path.splitext(inputFile)
  outputFile = base+'_stripz'+ext
  stripped = stripz(inputFile, outputFile);
  print ('%s written to %s with %d lines stripped' % (inputFile, outputFile, stripped))
