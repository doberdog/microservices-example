import glob
import os
from shutil import copyfile, SameFileError

from setuptools import sandbox

PETRICHOR_HOME = os.environ.get("PETRICHOR_HOME")
SETUP_FILES = PETRICHOR_HOME + '/shared/**/*setup.py'
TARS = PETRICHOR_HOME + '/shared/**/*tar.gz'
PACKAGES_HOME = os.path.join(PETRICHOR_HOME, 'services', 'pypi-service', 'python')

if not os.path.exists(PACKAGES_HOME):
    print(f"Creating location for serving packages: {PACKAGES_HOME}")
    os.makedirs(PACKAGES_HOME)

setup_files = []

print(f"Step 1: Exploring {PETRICHOR_HOME} for setup files")
for filename in glob.iglob(SETUP_FILES, recursive=True):
    setup_files.append(filename)
    print(f"Running setup for: {filename}")
    sandbox.run_setup(filename, ['sdist'])

print("\n")
print(f"{len(setup_files)} packages built.")

print("\n")
print(f"Step 2: Exploring {PETRICHOR_HOME} for python packages")


tarballs = []

for filename in glob.iglob(TARS, recursive=True):
    print(filename)
    if "site-packages" not in filename:
        head, fname = os.path.split(filename)
        tarballs.append(fname)
        dest = os.path.join(PACKAGES_HOME, fname)
        try:
            print(f"Copying [{fname}] to: {dest}")
            copyfile(filename, dest)
        except SameFileError:
            pass

print("\n")
print(f"Build and copy complete. PyPI Can now serve the following packages:")
for tb in tarballs:
    print(tb)

