#!/usr/bin/env python3

from __future__ import print_function, division, absolute_import

import re
from mdorrst import __version__


def find_typical_markers(content):
    """Try to find typical markdown or rst markers:
    """
    markdown = {
        'titles': len(re.findall('^#+ ', content, re.M)),
        'links': content.count(']('),
        'code_blocks': len(re.findall('^ *```$', content, re.M)),
        'images': content.count('!['),
        'ref_link': len(re.findall('^\[[0-9]\]:', content, re.M))
    }

    restructuredtext = {
        'titles': (len(re.findall('^~{5,}$', content, re.M)) +
                   len(re.findall('^`{5,}$', content, re.M))),
        'compat_titles': (len(re.findall('^={5,}$', content, re.M)) +
                          len(re.findall('^-{5,}$', content, re.M))) / 1000,
        'links': content.count('`_'),
        'code': content.count('.. code'),
        'images': content.count('.. image::'),
        'block': content.count('::\n'),
        'reference': len(re.findall('`[a-zA-Z0-9]+`_', content)),
        'include': content.count('.. include::'),
        'substitutions': content.count('\n.. |')
    }

    return markdown, restructuredtext


def sniff(content):
    """Deduce the format (md|rst|txt) of a given string.
    """
    markdown, restructuredtext = find_typical_markers(content)
    markdown_points = sum(markdown.values())
    restructuredtext_points = sum(restructuredtext.values())
    if markdown_points == restructuredtext_points == 0:
        return 'txt'
    return 'md' if markdown_points > restructuredtext_points else 'rst'


def parse_args(args):
    import argparse
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Tell appart rst or md for a given file.")
    parser.add_argument(
        '--version',
        action='version',
        version='mdorrst {ver}'.format(ver=__version__))
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help="Tell why I think like this.")
    parser.add_argument(
        dest="file_path",
        help="Path of a file",
        metavar="README.rst")
    return parser.parse_args(args)


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)
    if args.verbose:
        import pprint
        with open(args.file_path) as readme_file:
            markdown, restructuredtext = find_typical_markers(
                readme_file.read())
            print("Markdown points:")
            pprint.pprint(markdown)
            print("reStructuredText points:")
            pprint.pprint(restructuredtext)
            return
    with open(args.file_path) as file_to_sniff:
        print(sniff(file_to_sniff.read()))


def run():
    """Entry point for console_scripts
    """
    import sys
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
