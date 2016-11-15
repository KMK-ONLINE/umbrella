#!/usr/bin/env python

# run on task files to ensure tasks have tags

from __future__ import division, absolute_import, print_function, unicode_literals

import sys
import yaml


err = 0


def complain(s):
    global err
    print(s, file=sys.stderr)
    err = 1


def run_lint(filename, stream):
    objs = yaml.safe_load(stream)
    if not isinstance(objs, list):
        complain('%s: top level object not a list' % (filename,))
        return
        
    for i in objs:
        if ('tags' not in i) and ('include' not in i):
            complain('%s: tags not in %s' % (filename, repr(i)))


def main(argv):
    if len(argv) == 0:
        run_lint("<stdin>", sys.stdin)
    else:
        for fn in argv:
            with open(fn, 'r') as f:
                run_lint(fn, f)
    sys.exit(err)
            

if __name__ == '__main__':
    main(sys.argv[1:])
