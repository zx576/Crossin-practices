import os
import time

source = ['d:/temp/from',]

target_dir = 'd:/temp/to'

target = target_dir + time.time().strftime('%Y%m%d%H%M%S') + 'zip'

zip_command = "zip -qr '%s'%s"%(target,''.join(source))

if os.system(zip_command) == 0:
    print('s')

else:
    print('f')