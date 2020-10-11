#!/usr/bin/env python3

import argparse
import os
import re
import sys

pattern = None

def walk(input_path, output_path):
    print('walk({}, {})'.format(input_path, output_path))

    for root, _, files in os.walk(input_path):
        print(root)
        for f in files:
            if pattern.match(f):
                print(f)
                src = os.path.normpath('{}/{}'.format(root, f))
                dst = os.path.normpath('{}/{}'.format(output_path, f))
                os.symlink(src, dst)

def parse_args():
    epilog = 'Ex: ./symlink_pattern.py /work/foo /tmp/links \'.*\\.jp[e]?g$\''
    parser = argparse.ArgumentParser(prog='PROG', epilog=epilog)
    parser.add_argument('input_path',  help='path help')
    parser.add_argument('output_path', help='path help')
    patter_help = 'A real python regex to pass to re.match, eg \'.*\\.jp[e]?g$\''
    parser.add_argument('pattern',     help=patter_help)

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    if os.path.isdir(args.output_path) != True:
        print('ERROR: {} is not a directory or does not exist'.format(args.output_path))
        sys.exit(1)
    pattern = re.compile(args.pattern)
    walk(args.input_path, args.output_path)