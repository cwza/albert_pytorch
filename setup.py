from setuptools import setup, find_packages

setup(
        name='albert-zh-pytorch',
        version='1.0',
        author='cwza',
        packages=find_packages(),
        install_requires=['torch>=1.1.0', 'sentencepiece', 'scikit-learn']
)