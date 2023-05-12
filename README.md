# PotParser 🥦 - a strain webscraper

This is a Python package that allows you to scrape information about cannabis strains and calculate the amount of THC or CBD in a given amount of cannabis flower. It includes a command-line interface and various utilities for displaying and formatting the results.

## Demo

[![asciicast](https://asciinema.org/a/584238.svg)](https://asciinema.org/a/584238)

## Requirements

This Project is compatible with Linux, Windows and OSX, it requires Python 3.9 or newer in order to run!

## Installation

After you installed Python, clone this repository and cd into it:

```bash
git clone https://github.com/V2BlockBuster2K/PotParser.git
cd PotParser
```

Then use pip to install:

```bash
pip install .
```

If you want to do all of this at once, we can chain the commands like so:

```bash
git clone https://github.com/V2BlockBuster2K/PotParser.git && cd PotParser && pip install .
```

## Usage

Here's an example of how to use PotParser in Terminal:

```bash
$ potparser
```

Or in a .py file as module:

```bash
from potparser import PotParser

parser = PotParser()
strain = parser.get_strain("Blue Dream")
```

This will output a List containing three Dicts, which hold the information about the Blue Dream strain from different websites.

## Docker

If you wan't the docker container then clone this repository and cd into it:

```bash
git clone https://github.com/V2BlockBuster2K/PotParser.git
cd PotParser
```

Then build the docker container and run it using:

```bash
docker buildx build -t potparser .
docker run -it potparser
```

If you want to do all of this at once, we can chain the commands like so:

```bash
git clone https://github.com/V2BlockBuster2K/PotParser.git && cd PotParser && docker buildx build -t potparser . && docker run -it potparser
```

## Contributing

If you'd like to contribute to PotParser, please follow the steps below:

1. Fork the repo
2. Create a new branch (git checkout -b my-feature)
3. Make your changes and commit them (git commit -am 'Added a new feature')
4. Push your changes to your fork (git push origin my-feature)
5. Create a new pull request

I welcome contributions of any kind, including bug fixes, new features, and documentation improvements. If you have any questions or need any help, please don't hesitate to open an issue.

## License

This project is licensed under the [GPLv3](https://www.gnu.org/licenses/gpl-3.0.txt). See the 'LICENSE' file for details.
