#Author: Ishan Thilina Somasiri
#E-mail: ishan@ishans.info
#Blog: www.blog.ishans.info

from distutils.core import setup

PACKAGE = ""
NAME = "setBrightness"
DESCRIPTION = ""
AUTHOR = ""
AUTHOR_EMAIL = ""
URL = ""
VERSION = 1

setup(
    name = NAME,
    version = VERSION,
    packages = ['src',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README').read(),
)
