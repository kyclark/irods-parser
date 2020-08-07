#!/usr/bin/env python3
"""tests for irods_parser.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput, getoutput

prg = './irods_parser.py'
input1 = './tests/input1.txt'
input2 = './tests/input2.txt'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_bad_file():
    """usage"""

    bad = random_string()
    rv, out = getstatusoutput(f'{prg} {bad}')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_file_input1():
    """file input1"""

    out = getoutput(f'{prg} {input1}')
    assert out.strip() == '\n'.join([
        '/iplant/home/kyclark/project/sample/data.xlsx',
        '/iplant/home/kyclark/project/sample/data.csv',
        '/iplant/home/kyclark/project/sample/README.md'
    ])


# --------------------------------------------------
def test_file_input2():
    """file input2"""

    out = getoutput(f'{prg} {input2}')
    assert out.strip() == '\n'.join([
        '/iplant/home/kyclark/foo/bar/PhaseI_Plant_Metal_Conc_02.13.2020.csv',
        '/iplant/home/kyclark/foo/bar/PhaseI_Plant_Weed_Cover_02.13.2020.csv',
        '/iplant/home/kyclark/foo/bar/Soil_Chemistry_02.13.2020.csv',
        '/iplant/home/kyclark/foo/bar/PhaseI_Plant_Metal_Conc_02.13.2020.csv',
        '/iplant/home/kyclark/foo/bar/PhaseI_Plant_Weed_Cover_02.13.2020.csv',
        '/iplant/home/kyclark/foo/bar/Soil_Chemistry_02.13.2020.csv',
        '/iplant/home/kyclark/foo/bar/PhaseI_Plant_Metal_Conc_02.13.2020.csv',
        '/iplant/home/kyclark/foo/bar/PhaseI_Plant_Weed_Cover_02.13.2020.csv',
        '/iplant/home/kyclark/foo/bar/Soil_Chemistry_02.13.2020.csv',
        '/iplant/home/kyclark/foo/bar/PhaseI_Plant_Metal_Conc_02.13.2020.csv',
        '/iplant/home/kyclark/foo/bar/PhaseI_Plant_Weed_Cover_02.13.2020.csv',
        '/iplant/home/kyclark/foo/bar/Soil_Chemistry_02.13.2020.csv',
        '/iplant/home/kyclark/foo/bar/ReadMe.md',
        '/iplant/home/kyclark/foo/census-acs5/scrutinizer.csv'
    ])

# --------------------------------------------------
def test_stdin():
    """stdin"""

    out = getoutput(f'{prg} < {input1}')
    assert out.strip() == '\n'.join([
        '/iplant/home/kyclark/project/sample/data.xlsx',
        '/iplant/home/kyclark/project/sample/data.csv',
        '/iplant/home/kyclark/project/sample/README.md'
    ])

# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
