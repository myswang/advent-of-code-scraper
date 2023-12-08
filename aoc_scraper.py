import argparse
from datetime import datetime, timezone
import re
import requests
import sys

def fetch_stats(year):
    url = f"https://adventofcode.com/{year}/stats"
    response = requests.get(url)
    if response.status_code == 200:
        pattern = re.compile(f"<a href=\"/{year}/day/\d+\">(.*?)</a>")
        days = re.findall(pattern, response.text)
        for idx, day in enumerate(days):
            days[idx] = tuple(int(num) for num in re.findall(r"\d+", day))
        print("------------------------------------------------------------------------")
        print(f"Completion statistics for Advent of Code {year}:")
        print("** = completed both parts of a puzzle, * = completed only the first half")
        print("------------------------------------------------------------------------")
        for day in days:
            day_num, two_star, one_star = day
            total_stars = one_star + two_star
            two_star_rate = round(two_star / total_stars * 100, 2)
            print(f"Day {day_num}: {two_star} **, {one_star} *, Total: {total_stars} ({two_star_rate}% **)")
        print("------------------------------------------------------------------------")
        print(f"Retrieved {datetime.now(timezone.utc).replace(microsecond=0)}.")
        sys.exit(0)
    elif response.status_code == 404:
        print(f"Invalid year: {year}", file=sys.stderr)
        sys.exit(1)
    else:
        print(f"Error: {response.status_code}", file=sys.stderr)
        sys.exit(1)

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-y", "--year", help="event year to fetch")
args = arg_parser.parse_args()
if args.year is not None:
    fetch_stats(args.year)
else:
    # Note: This may not return the correct year to fetch due to timezone differences.
    #       It's a bit hacky and a proper fix would be more complex than this.
    #       For best results, specify a --year argument.
    cur_year = datetime.now().year
    if datetime.now().month < 12:
        cur_year -= 1
    fetch_stats(cur_year)