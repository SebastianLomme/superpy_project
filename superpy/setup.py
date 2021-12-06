from setuptools import setup, find_packages

setup(
    name='superpy',
    version='0.0.1',
    packages=find_packages(where="src", exclude=("tests",)),
    entry_points={
        'console_scripts' : ['superpy=app.main:main']
    },
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)