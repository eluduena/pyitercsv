# setup.py
from setuptools import setup, find_packages

setup(
    name='pyitercsv',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pyitercsv = pyitercsv.pyitercsv:main',
        ],
    },
    install_requires=[],
    author='Emilio',
    author_email='eluduena@gmail.com',
    description='Python script to iter over csv file',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='URL del proyecto',
)
