"""Setup the package."""

from setuptools import setup, find_packages
import src


setup(
    name='read_sequencing',
    url='https://github.com',
    author='Kathleen Moriarty',
    author_email='kathleen.moriarty@swisstph.ch',
    license='MIT',
    version=src.__version__,
    install_requires=[],
    entrypoints={},
    packages=find_packages()
)
