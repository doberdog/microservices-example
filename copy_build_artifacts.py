import glob
import os
from shutil import copyfile, SameFileError

from setuptools import sandbox

PETRICHOR_HOME = os.environ.get("PETRICHOR_HOME")
SETUP_FILES = PETRICHOR_HOME + '/services/**/*setup.py'
WHLS = PETRICHOR_HOME + '/services/**/*whl'
PACKAGES_HOME = os.path.join(PETRICHOR_HOME, "packages")

if not os.path.exists(PACKAGES_HOME):
    print(f"Creating location for serving packages: {PACKAGES_HOME}")
    os.makedirs(PACKAGES_HOME)

setup_files = []

print(f"Step 1: Exploring {PETRICHOR_HOME} for setup files")
for filename in glob.iglob(SETUP_FILES, recursive=True):
    setup_files.append(filename)
    print(f"Running setup for: {filename}")
    sandbox.run_setup(filename, ['clean', 'bdist_wheel'])

print("\n")
print(f"{len(setup_files)} packages built.")

print("\n")
print(f"Step 2: Exploring {PETRICHOR_HOME} for python packages")


whl_files = []

for filename in glob.iglob(WHLS, recursive=True):
    print(filename)
    if "site-packages" not in filename:
        head, fname = os.path.split(filename)
        whl_files.append(fname)
        dest = os.path.join(PACKAGES_HOME, fname)
        try:
            print(f"Copying [{fname}] to: {dest}")
            copyfile(filename, dest)
        except SameFileError:
            pass

print("\n")
print(f"Build and copy complete. PyPI Can now serve the following packages:")
for whl in whl_files:
    print(whl)

print("----------------------------------------")

