from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in general_manager/__init__.py
from general_manager import __version__ as version

setup(
	name="general_manager",
	version=version,
	description="A business Management Web App",
	author="koncrete.tech",
	author_email="dialslic.com[D[D",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
