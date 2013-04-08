#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import sys
import subprocess


if __name__ == '__main__':
  argv = sys.argv  
  argc = len(argv)
  if argc > 2:
    exit()
  elif argc == 2:
    findre = argv[1]
  else:
    findre = "*"

  # execute command
  cwd = "/"
  #cmd = ['find', './', '-type', 'f']
  #subprocess_args = { 'stdin': subprocess.PIPE,
  #    'stdout': subprocess.PIPE,
  #    'stderr': subprocess.STDOUT,
  #    'cwd': cwd,
  #    'close_fds': True,
  #    }
  cmd = 'find ./ -type f'
  try:
    #p = subprocess.Popen(cmd, **subprocess_args)
    p = subprocess.Popen(cmd,
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        )
  except OSError:
    print "Failed to execute command: %s" % cmd[0]
    sys.exit(1)

  stdout = p.stdout
  for line in stdout:
    print line.strip()
  exit()
  #(stdout, stderr) = p.communicate()
  #(stdouterr, stdin) = (p.stdout, p.stdin)
  print "-" * 80
  print stdout
  #for line in stdouterr.readline():
  #  print line,
  print "-" * 80
  print "Retrun code: %d" % p.wait()
