#!/usr/bin/env python3

''' Cryptoline preprocessor script for mass renaming procedure arguments
to a more readable format and injecting an initialization block
'''
arg_str = ''
nargs = 256
arg_type = 'sint16'
arg_prefix = 'c'
arg_ft = '{} {}_{:02x}'
init_fmt = 'mov {} {}_{:02x};'

def pp_args():
    for i in range(0,nargs,4):
        print(arg_ft.format(arg_type, arg_prefix, i) + ', ' +
              arg_ft.format(arg_type, arg_prefix, i + 1) + ', ' +
              arg_ft.format(arg_type, arg_prefix, i + 2) + ', ' +
              arg_ft.format(arg_type, arg_prefix, i + 3) + ',')

def pp_init(args):
    for i in range(0,nargs,2):
        print(init_fmt.format(args[i], arg_prefix, i) + ' ' + init_fmt.format(args[i+1], arg_prefix, i+1))
    return

arg_str = input()
args = arg_str.split(',')[:nargs]
pp_args()
pp_init(args)
