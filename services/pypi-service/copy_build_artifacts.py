import glob
import os
from distutils.core import run_setup
from shutil import copyfile, SameFileError

PETRICHOR_HOME = os.environ.get("PETRICHOR_HOME")
SETUP_FILES = PETRICHOR_HOME + '/**/*setup.py'
TARBALLS = PETRICHOR_HOME + '/**/*tar.gz'

for filename in glob.iglob(SETUP_FILES, recursive=True):
    print(f"Step 1: Exploring {PETRICHOR_HOME} for setup files")
    run_setup(
            filename,
            # script_args=sys.argv[1:],
            stop_after='run'
    )

for filename in glob.iglob(TARBALLS, recursive=True):
    print(f"Step 2: Exploring {PETRICHOR_HOME} for python packages")
    if "site-packages" not in filename:
        head, fname = os.path.split(filename)
        dest = os.path.join(PETRICHOR_HOME, "packages", "python", fname)
        try:
            print(f"Copying [{fname}] to: {dest}")
            copyfile(filename, dest)
        except SameFileError:
            pass
