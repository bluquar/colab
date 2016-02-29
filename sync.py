import os
import sys
import subprocess

USER = os.environ['USER']
SKETCH = "/Users/%s/Library/Application\ Support/com.bohemiancoding.sketch3/Plugins/CoLab" % (
  USER)
HERE = "./CoLab"

def usage():
  print "Usage: "
  print "  Copy the repo to your Sketch plugin directory: python sync.py to"
  print "  Copy your Sketch plugin directory to the repo: python sync.py from"
  exit()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
    if sys.argv[1] == 'to':
      if os.path.exists(SKETCH):
        subprocess.call("rm -rf %s" % SKETCH, shell=True)
      subprocess.call("cp -r %s %s" % (HERE, os.path.dirname(SKETCH)), shell=True)
    elif sys.argv[1] == 'from':
      if os.path.exists(HERE):
        subprocess.call("rm -rf %s" % HERE, shell=True)
      subprocess.call("cp -r %s %s" % (SKETCH, HERE), shell=True)
