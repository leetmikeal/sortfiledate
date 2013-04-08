#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import sys
import subprocess
import time


def toDateString(n):
  #return str(n[0])+str(n[1]).rjust(2,"0")+str(n[2]).rjust(2,"0")
  return time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(n))

def printHelp():
  print "Usage:"
  print "  python %s <find file regular expression>" % __file__

if __name__ == '__main__':
  argv = sys.argv  
  argc = len(argv)
  if argc > 2:
    printHelp()
    exit(1)
  elif argc == 2:
    if argv[1] == '-help':
      printHelp()
      exit()
    findre = argv[1]
  else:
    findre = "*"

  cmd = 'find ./ -type f -name "%s"' % (findre)
  try:
    p = subprocess.Popen(cmd,
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        )
  except OSError:
    print "Failed to execute command: %s" % cmd[0]
    sys.exit(1)

  filelist = []
  stdout = p.stdout
  for line in stdout:
    updatetime = os.stat(line.strip()).st_mtime
    filelist.append(
        (updatetime, line.strip())
        )
  #sorted(filelist, key=lambda file: file[1]) # sort by datetime
  filelist.sort() # sort by datetime

  for file in filelist:
    #print "%10s %s" % (toDateString(file[1]), file[0])
    print "%20s %s" % (toDateString(file[0]), file[1])
    
