from cx_Freeze import setup, Executable

setup(name='PrimeDistinguish',
      version='1.0',
      description='Prime Distinguish',
      executables = [Executable('PrimeDistinguish.py')])
