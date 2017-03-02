import os , argparse
import builtins
from collections import ChainMap
pylookup = ChainMap(locals(), globals(), vars(builtins))
defaults = {'color':'red','user':'guest'}
parser = argparse.ArgumentParser()
parser.add_argument('-u','--user')
parser.add_argument('-c','--color')
namespace = parser.parse_args()
command_line_args = {k:v for k,v in vars(namespace).items() if v}

combined = ChainMap(command_line_args,os.environ,defaults)

print(combined['color'])
