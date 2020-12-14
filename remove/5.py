# remove if file exist else not

import os
if os.path.exists('demo1.txt'):
    os.remove('demo1.txt')
else:
    print('not exist')
    
    