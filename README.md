# advent-of-code-scraper

This is a Python script that scrapes the [stats page](https://adventofcode.com/2023/stats) from Advent of Code and displays completion statistics for each day in a given year.

## Quick Start

This script uses the Python [requests](https://pypi.org/project/requests/) library:

```
$ python -m pip install requests
```

To get completion stats for the current year, run:

```
$ python aoc_scraper.py
```

See the [Usage](#usage) section for more details.

## Usage

You can get usage details about the script:

```
$ python aoc_scraper.py --help
usage: aoc_scraper.py [-h] [-y YEAR]

options:
  -h, --help            show this help message and exit
  -y YEAR, --year YEAR  event year to fetch
```

You may optionally specify a year to fetch completion stats:

```
$ python aoc_scraper.py --year 2020
```

When no year argument is supplied, the most recent event year is returned instead. However, the method used is a bit hacky and may not return the correct year. Therefore, it is best to use the `--year` argument.

### Example Output:

```
$ python aoc_scraper.py --year 2020
---------------------------------------------------
Completion statistics for Advent of Code 2020:
** = both parts completed, * = first part completed
---------------------------------------------------
Day     **     *  Total  ** %
 25  14160  4597  18757 75.49
 24  17477  1047  18524 94.35
 23  16686  2537  19223 86.80
 22  18754  3489  22243 84.31
 21  19442   252  19694 98.72
 20  16305  5036  21341 76.40
 19  20991  3730  24721 84.91
 18  28470  1960  30430 93.56
 17  29417   839  30256 97.23
 16  32964  4520  37484 87.94
 15  38241  2100  40341 94.79
 14  37241  4344  41585 89.55
 13  38441 11433  49874 77.08
 12  47753  3993  51746 92.28
 11  48752  5373  54125 90.07
 10  53464 12188  65652 81.44
  9  67716  1802  69518 97.41
  8  69668  5916  75584 92.17
  7  69184  7061  76245 90.74
  6  90925  3235  94160 96.56
  5  97005  2423  99428 97.56
  4 101844 13963 115807 87.94
  3 124612  4775 129387 96.31
  2 150384  5768 156152 96.31
  1 179626 14769 194395 92.40
---------------------------------------------------
Retrieved 2023-12-09 01:33:08+00:00.
```

