import fnmatch
import os
import shutil

dst_dir='F:\\albumcover'
for root, dirs, files in os.walk('F:\\music'):
  for file in files:
    if fnmatch.fnmatch(file, '*.jpg'):
	  shutil.copy(os.path.join(root, file), dst_dir)
