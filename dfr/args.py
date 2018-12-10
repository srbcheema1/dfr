import os
import sys

try:
    import argparse
    from argcomplete import autocomplete
except:
    err = """
    You haven't installed the required dependencies.
    """
    print(err)
    sys.exit(0)

from .Colour import Colour


class Args:
    def _is_valid_path(parser, arg):
        if not os.path.exists(arg):
            parser.error("The path %s does not exist!" % arg)
        else:
            return arg


    def get_parser():
        parser = argparse.ArgumentParser()
        subparsers = parser.add_subparsers(dest='action')


        cache_parser = subparsers.add_parser('cache')
        cache_parser.add_argument("loc",nargs='?',
                                type=lambda x: Args._is_valid_path(cache_parser,x),
                                help="folder location to be cached")

        find_parser = subparsers.add_parser('find')
        find_parser.add_argument("inp",nargs='?',
                                type=lambda x: Args._is_valid_path(find_parser,x),
                                help="location to be processed")

        autocomplete(parser)
        parsed_args = parser.parse_args()
        if(not parsed_args.action):
            Colour.print('requires atleast one command line argument',Colour.RED)
            parser.print_help(sys.stderr)
            sys.exit(1)
        return parsed_args
