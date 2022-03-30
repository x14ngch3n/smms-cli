# smms-cli

![PyPI](https://img.shields.io/pypi/v/smms-cascades)
![PyPI - License](https://img.shields.io/pypi/l/smms-cascades)

A command line HTTP client of <https://sm.ms>

## Usage

```python=
$ smms -h
usage: smms [-h] [-f FILENAME] [-o OUTPUT] method

A simple command line HTTP client of https://sm.ms

positional arguments:
  method                API method: [upload | delete | getprofile | gethistory]

optional arguments:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME
                        used with [upload | delete], select image to be uploaded or deleted
  -o OUTPUT, --output OUTPUT
                        used with upload, specify the output format: [json | md | url], default is json
```

## Links

* API Docs: <https://doc.sm.ms/#api>
* My blog: <https://cascadeschen.cn/2022-03-28-smms-cli/>
