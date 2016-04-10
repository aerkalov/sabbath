#!/usr/bin/env python

from __future__ import print_function

import datetime
import collections
import argparse
import sys


DAYS_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
MIN_SATURDAY = 1
MIN_SUNDAY = 1

weekdays = collections.Counter()
dates = []
total = 0


def parse_stdin():
    global dates
    global total

    for line in sys.stdin:
        date = line.strip().split(' ')[3]

        if date not in dates:
            dates.append(date)
            # yes :)
            d2 = date.split('-')
            d = datetime.datetime(int(d2[0]), int(d2[1]), int(d2[2]))
            weekdays[d.weekday()] += 1
            total += 1


def show_report(use_colours):
    print('\nRemember the sabbath day')
    print('-' * 80)

    for days in range(7):
        num = weekdays[days]
        try:
            per = float(num) / float(total) * 100
        except ZeroDivisionError:
            per = 0

        colour_start, colour_end = '', ''

        if use_colours:
            colour_start, colour_end = '\033[32m', '\033[0m'

            if days >= 5:
                if days == 5 and num > MIN_SATURDAY:
                    colour_start = '\033[31m'
                if days == 6 and num > MIN_SUNDAY:
                    colour_start = '\033[31m'

        print('{day:>10} : {cs}{percent:>2} %{ce} : {cs}{graph}{ce}'.format(
            day=DAYS_OF_WEEK[days],
            cs=colour_start,
            ce=colour_end,
            percent=int(round(per)),
            graph='#' * int(per)
        ))
    print('-' * 80)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='''Check how much do you work on weekends.
  https://github.com/aerkalov/sabbath''',
        epilog='''Usage:
  $ git log --date=short | grep "^Date:" | sabbath.py -s -c
  $ git log --date=short --since="2013-01-01" | grep "^Date:" | sabbath.py -s

  $ git log --date=short --author=Erkal | grep "^Date:" | sabbath.py -5
  $ echo $?
  ''',
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-s', '--show', action='store_true', default=False, dest='show', help='Show Git activity.')
    parser.add_argument('-5', '--have-i-sinned', action='store_true', default=False, dest='sinner', help='Are you a sinner?')
    parser.add_argument('-c', '--colour', action='store_true', default=False, dest='colour', help='Use colours in report.')

    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    if args.sinner:
        parse_stdin()
        if weekdays[5] > MIN_SATURDAY or weekdays[6] > MIN_SUNDAY:
            sys.exit(1)

    if args.show:
        parse_stdin()
        show_report(args.colour)

    sys.exit(0)
