import os
import glob
from shutil import copyfile, SameFileError

PETRICHOR_HOME = os.environ.get("PETRICHOR_HOME")

for filename in glob.iglob(PETRICHOR_HOME + '/**/*tar.gz', recursive=True):
    if "site-packages" not in filename:
        head, fname = os.path.split(filename)
        dest = os.path.join(PETRICHOR_HOME, "packages", "python", fname)
        try:
            print("Copying [{}] to: {}".format(fname, dest))
            copyfile(filename, dest)
        except SameFileError:
            pass
