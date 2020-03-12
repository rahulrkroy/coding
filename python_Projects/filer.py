import os
fpath = r'/home/shikari/coding/python_Projects/log.txt'
if not os.path.exists(fpath):
  print ('File does not exist')
else:
    with open(fpath, 'a+') as src:
        print("writing file")
        src.write("hello")
        # src.close()