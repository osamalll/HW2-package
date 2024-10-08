from setuptools import setup, find_packages

setup(
    name='hello_package',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'sayhello=hello_package.hello:sayHello',
        ],
    },
)
