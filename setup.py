import os
from os.path import relpath, join
from setuptools import setup
# import versioneer

# https://python-packaging.readthedocs.io/en/latest/minimal.html
# build package

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def find_package_data(data_root, package_root):
    files = []
    for root, dirnames, filenames in os.walk(data_root):
        for fn in filenames:
            files.append(relpath(join(root, fn), package_root))
    return files


setup(name='mlddec',
      version='0.1',
      description='', #TODO
      author='Shuzhe Wang',
      author_email='shuzhe.wang@phys.chem.ethz.ch',
      license='MIT',
    packages=[
        'mlddec',
        'mlddec/data',
        ],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT",
    ],
    entry_points={'console_scripts': []},
    package_data={'mlddec': find_package_data('mlddec/data', 'mlddec')},
    # version=versioneer.get_version(),
    # cmdclass=versioneer.get_cmdclass(),
    )
