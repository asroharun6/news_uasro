from setuptools import setup, find_packages

setup(
    name='news_uasro',
    version='0.1.2',
    author='Asro',
    author_email='asro@raharja.info',
    description='A simple library for detecting media sources.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='http://github.com/asroharun6/news_uasro',
    packages=find_packages(),  # Automatically find all packages and subpackages
    install_requires=[
        'pandas',  # Assuming you use pandas somewhere in your package
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
