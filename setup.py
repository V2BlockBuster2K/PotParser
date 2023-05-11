from setuptools import setup

__VERSION__ = "1.0.0"

def get_requirements(file_path):
    with open(file_path, 'r') as f:
        requirements = f.read().splitlines()
    return requirements

setup(
    name = "potparser",
    packages=['potparser', 'potparser.helpers', 'potparser.utils', 'potparser.views', 'potparser.webscrapers'],
    version = __VERSION__,
    description = "A strain webscraper",
    long_description = open('README.md', 'r').read(),
    long_description_content_type = 'text/markdown',
    author = "V2BlockBuster2K",
    url = "https://github.com/V2BlockBuster2K/PotParser",
    license = "GPLv3",

    entry_points={
        'console_scripts': ['potparser=potparser.cli:main']
    },
    classifiers = [
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    install_requires=get_requirements('requirements.txt'),
)