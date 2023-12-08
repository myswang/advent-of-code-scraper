# advent-of-code-scraper: A Python script that fetches Advent of Code completion statistics

*Disclaimer: Please refrain from using this script to send large quantities of **automated requests** to the Advent of Code [website](https://adventofcode.com).*

This Python script scrapes the [stats page](https://adventofcode.com/2023/stats) from Advent of Code and displays completion statistics per day for a given year.

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

You may optionally specify a year to fetch completion stats from:

```
$ python aoc_scraper.py --year 2020
```

When no year argument is supplied, the most recent event year is returned instead. However, the method used is a bit hacky and may not return the correct year. Therefore, it is best to use the `--year` argument.

## Sample Output (2020)

```
$ python aoc_scraper.py --year 2020
------------------------------------------------------------------------
Completion statistics for Advent of Code 2020:
** = completed both parts of a puzzle, * = completed only the first half
------------------------------------------------------------------------
Day 25: 14160 **, 4597 *, Total: 18757 (75.49% **)
Day 24: 17477 **, 1047 *, Total: 18524 (94.35% **)
Day 23: 16686 **, 2537 *, Total: 19223 (86.8% **)
Day 22: 18754 **, 3489 *, Total: 22243 (84.31% **)
Day 21: 19442 **, 252 *, Total: 19694 (98.72% **)
Day 20: 16305 **, 5036 *, Total: 21341 (76.4% **)
Day 19: 20991 **, 3730 *, Total: 24721 (84.91% **)
Day 18: 28470 **, 1960 *, Total: 30430 (93.56% **)
Day 17: 29417 **, 839 *, Total: 30256 (97.23% **)
Day 16: 32964 **, 4520 *, Total: 37484 (87.94% **)
Day 15: 38241 **, 2100 *, Total: 40341 (94.79% **)
Day 14: 37241 **, 4344 *, Total: 41585 (89.55% **)
Day 13: 38441 **, 11432 *, Total: 49873 (77.08% **)
Day 12: 47753 **, 3993 *, Total: 51746 (92.28% **)
Day 11: 48752 **, 5373 *, Total: 54125 (90.07% **)
Day 10: 53464 **, 12187 *, Total: 65651 (81.44% **)
Day 9: 67715 **, 1803 *, Total: 69518 (97.41% **)
Day 8: 69668 **, 5916 *, Total: 75584 (92.17% **)
Day 7: 69184 **, 7061 *, Total: 76245 (90.74% **)
Day 6: 90923 **, 3236 *, Total: 94159 (96.56% **)
Day 5: 97002 **, 2425 *, Total: 99427 (97.56% **)
Day 4: 101842 **, 13964 *, Total: 115806 (87.94% **)
Day 3: 124610 **, 4775 *, Total: 129385 (96.31% **)
Day 2: 150381 **, 5769 *, Total: 156150 (96.31% **)
Day 1: 179622 **, 14770 *, Total: 194392 (92.4% **)
------------------------------------------------------------------------
Retrieved 2023-12-08 23:36:05+00:00.
```

