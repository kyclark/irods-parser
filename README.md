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

## Author

Ken Youens-Clark <kyclark@gmail.com>
