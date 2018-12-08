import os
import glob
from shutil import copyfile, SameFileError

PETRICHOR_HOME = os.environ.get("PETRICHOR_HOME")

for filename in glob.iglob(PETRICHOR_HOME + '/**/*tar.gz', recursive=True):
    print(f"Exploring {PETRICHOR_HOME} for python packages")
    if "site-packages" not in filename:
        head, fname = os.path.split(filename)
        dest = os.path.join(PETRICHOR_HOME, "packages", "python", fname)
        try:
            print(f"Copying [{fname}] to: {dest}")
            copyfile(filename, dest)
        except SameFileError:
            pass
