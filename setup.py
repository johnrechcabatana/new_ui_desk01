from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in new_ui_desk01/__init__.py
from new_ui_desk01 import __version__ as version

setup(
	name='new_ui_desk01',
	version=version,
	description='UI',
	author='John Rech G. Cabatana',
	author_email='cabatana.johnrech.g@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
