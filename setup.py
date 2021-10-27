from setuptools import find_packages, setup


setup(
    name='qb',
    version='0.0.1.alpha.PATCHES.0',
    packages=find_packages(exclude=('test*',)),
    author='Queensbarry',
    python_requires='>3.8'
)
