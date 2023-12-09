# advent-of-code-scraper

*Disclaimer: Please refrain from using this script to send large quantities of **automated requests** to the Advent of Code [website](https://adventofcode.com).*

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

## Sample Output (2020)

```
------------------------------------------------------------------------
Completion statistics for Advent of Code 2020:
** = completed both parts of a puzzle, * = completed only the first half
------------------------------------------------------------------------
Day 25: 14160 **, 4597 *, Total: 18757 (75.49% **)
Day 24: 17477 **, 1047 *, Total: 18524 (94.35% **)
Day 23: 16686 **, 2537 *, Total: 19223 (86.80% **)
Day 22: 18754 **, 3489 *, Total: 22243 (84.31% **)
Day 21: 19442 **, 252 *, Total: 19694 (98.72% **)
Day 20: 16305 **, 5036 *, Total: 21341 (76.40% **)
Day 19: 20991 **, 3730 *, Total: 24721 (84.91% **)
Day 18: 28470 **, 1960 *, Total: 30430 (93.56% **)
Day 17: 29417 **, 839 *, Total: 30256 (97.23% **)
Day 16: 32964 **, 4520 *, Total: 37484 (87.94% **)
Day 15: 38241 **, 2100 *, Total: 40341 (94.79% **)
Day 14: 37241 **, 4344 *, Total: 41585 (89.55% **)
Day 13: 38441 **, 11433 *, Total: 49874 (77.08% **)
Day 12: 47753 **, 3993 *, Total: 51746 (92.28% **)
Day 11: 48752 **, 5373 *, Total: 54125 (90.07% **)
Day 10: 53464 **, 12187 *, Total: 65651 (81.44% **)
Day 9: 67716 **, 1802 *, Total: 69518 (97.41% **)
Day 8: 69668 **, 5916 *, Total: 75584 (92.17% **)
Day 7: 69184 **, 7061 *, Total: 76245 (90.74% **)
Day 6: 90925 **, 3235 *, Total: 94160 (96.56% **)
Day 5: 97005 **, 2423 *, Total: 99428 (97.56% **)
Day 4: 101842 **, 13965 *, Total: 115807 (87.94% **)
Day 3: 124612 **, 4774 *, Total: 129386 (96.31% **)
Day 2: 150383 **, 5768 *, Total: 156151 (96.31% **)
Day 1: 179625 **, 14769 *, Total: 194394 (92.40% **)
------------------------------------------------------------------------
Retrieved 2023-12-09 00:55:52+00:00.
```

