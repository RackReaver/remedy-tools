from setuptools import setup
import versioneer

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    README = f.read()

setup(
    name='remedy-tools',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    url='https://github.com/RackReaver/remedy-tools',
    license='Apache License',
    author='Matt Ferreira',
    author_email='rackreaver@gmail.com',
    description='Leverages selenium to create tickets in the back-end gui of BMC Remedy.',
    long_description=README,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7'
    ],
    include_package_data=True,
    install_requirements=['requests',
                          'bs4',
                          'selenium']
)
