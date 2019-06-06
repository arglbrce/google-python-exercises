#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def utils_lines(filename):
    f = open(filename, 'r')
    lines = f.read()
    f.close()
    lines = lines  # .split('\n')
    return lines


def utils_summary_file(filename, babynames):
    filename = 'summary-' + filename.split('.')[0] + '.txt'
    with open(filename, 'w') as f:
        for item in babynames:
            f.write("%s\n" % item)
    f.close()
    return


def utils_files(*filename_patterns):
    import glob
    filenames = []
    for filename_pattern in filename_patterns:
        filenames += glob.glob(filename_pattern)
    return filenames


# print(utils_files('baby1990.html'))
# print(utils_files('baby19*.html'))
# print(utils_files('baby2000.html'))
# print(utils_files('baby20*.html'))
# print(utils_files('baby19*.html','baby20*.html'))


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    # +++your code here+++
    lines = utils_lines(filename)
    # print('lines', lines)

    # Extract the year and print it
    m = re.search('(?<=Popularity in )\d{4}', lines)
    year = m.group()
    # print(year)

    # Extract the names and rank numbers and just print them
    names_and_rank = re.findall('(?<=<td>)\w+', lines)
    names_data = dict()
    for i in range(0, len(names_and_rank), 3):
        # print(names_and_rank[i:i+3])
        # Get the names data into a dict and print it
        names_data[names_and_rank[i]] = names_and_rank[i + 1:i + 3]
    # print(names_data)

    # Build the [year, 'name rank', ... ] list and print it
    baby_names = [year]
    for k, v in names_data.items():
        name_rank_str = v[0] + ' ' + str(k)
        baby_names.append(name_rank_str)

    # print(baby_names)
    # print(sorted(baby_names))

    return sorted(baby_names)


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

    # +++your code here+++
    # For each filename, get the names, then either print the text output
    # or write it to a summary file

    for filename in utils_files(*args):
        if summary:
            babynames = extract_names(filename)
            utils_summary_file(filename, babynames)
        else:
            babynames = extract_names(filename)
            print(sorted(babynames))


if __name__ == '__main__':
    main()
