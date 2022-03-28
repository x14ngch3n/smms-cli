# smms-cli

![PyPI](https://img.shields.io/pypi/v/smms-cascades)
![PyPI - License](https://img.shields.io/pypi/l/smms-cascades)

A command line HTTP client of <https://sm.ms>

## Usage

```python=
$ smms -h
usage: smms [-h] [-f FILENAME] [--hash HASH] method

A simple command line HTTP client of https://sm.ms

positional arguments:
  method                API method: upload | delete | getprofile | gethistory

optional arguments:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME
                        used with upload, select image to be uploaded
  --hash HASH           used with delete, delete image by hash value
```

## Links

* <https://doc.sm.ms/#api>
