# iRODS ils parser

The output from the "ils" command in iRODS looks like this:

```
/iplant/home/kyclark/project:
  C- /iplant/home/rwalls/ua-src-data/sample
/iplant/home/kyclark/project/sample:
  data.xlsx
  data.csv
  README.md
```

The "irods_parser.py" will create the full paths for each file like so:

```
/iplant/home/kyclark/project/sample/data.xlsx
/iplant/home/kyclark/project/sample/data.csv
/iplant/home/kyclark/project/sample/README.md
```

For usage, run with "-h" or "--help":

```
$ ./irods_parser.py -h
usage: irods_parser.py [-h] [FILE]

Parse iRODS "ils" output

positional arguments:
  FILE        A readable file (default: 
              <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>)

optional arguments:
  -h, --help  show this help message and exit
```

The program accepts a single positional argument:

```
$ ./irods_parser.py tests/input1.txt
/iplant/home/kyclark/project/sample/data.xlsx
/iplant/home/kyclark/project/sample/data.csv
/iplant/home/kyclark/project/sample/README.md
```

Or works on STDIN (so you could pipe "ils" directly to this):

```
$ cat tests/input1.txt | ./irods_parser.py
/iplant/home/kyclark/project/sample/data.xlsx
/iplant/home/kyclark/project/sample/data.csv
/iplant/home/kyclark/project/sample/README.md
```

Run "make test" for test suite.

## Author

Ken Youens-Clark <kyclark@gmail.com>
