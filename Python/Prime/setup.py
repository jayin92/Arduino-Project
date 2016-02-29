from cx_Freeze import setup, Executable

setup(name='PrimeFinder',
      version='1.0',
      description='Prime Finder',
      executables = [Executable('PrimeFinder.py')])
