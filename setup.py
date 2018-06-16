
#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name='blockstack-proofs',
    version='0.0.10',
    url='https://github.com/blockstack/blockstack-proofs',
    license='MIT',
    author='Blockstack.org',
    author_email='support@blockstack.org',
    description='Python library for verifying proofs (twitter, github, domains etc) linked to a blockchain ID',
    keywords='blockchain bitcoin social proof verifications identity',
    packages=find_packages(),
    download_url='https://github.com/blockstack/blockstack-proofs/archive/master.zip',
    zip_safe=False,
    install_requires=[
