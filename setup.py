from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in wizpods/__init__.py
from wizpods import __version__ as version

setup(
	name="wizpods",
	version=version,
	description="WizPods Advanced Technologies",
	author="Philgin Solutions",
	author_email="philgin007@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
