from setuptools import setup, find_packages

setup(
    name='superpy',
    version='0.0.1',
    packages=["rich"],
    entry_points={
        'console_scripts' : ['superpy=app.main:main']
    },
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)