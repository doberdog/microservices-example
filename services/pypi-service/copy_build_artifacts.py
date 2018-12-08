import os
import glob
from shutil import copyfile, SameFileError

SERVICES_HOME = os.environ.get("SERVICES_HOME")

for filename in glob.iglob(RR_HOME + '/services/**/*tar.gz', recursive=True):
    if "site-packages" not in filename:
        head, fname = os.path.split(filename)
        dest = os.path.join(RR_HOME, "packages", "python", fname)
        try:
            print("Copying [{}] to: {}".format(fname, dest))
            copyfile(filename, dest)
        except SameFileError:
            pass
