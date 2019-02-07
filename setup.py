import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name='remedy-tools',
    version='0.0.1',
    url='https://github.com/RackReaver/remedy-tools',
    license='Apache License',
    author='RackReaver',
    author_email='rackreaver@gmail.com',
    description='Leverages selenium to create tickets in the back-end gui of BMC Remedy.',
    long_description=README,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: System :: Systems Administration'
    ],
    packages=['remedy_tools'],
    include_package_data=True,
    install_requirements=['requests',
                          'bs4',
                          'selenium']
)
