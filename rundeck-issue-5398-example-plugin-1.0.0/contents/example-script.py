#!/usr/bin/env python -u

import os

def main():
    script = os.environ.get('RD_CONFIG_SCRIPT_CONFIG_OPT')

    print("HELLO I AM THE EXAMPLE PLUGIN. I'LL OUTPUT THE SCRIPT I RECEIEVED STARTING ON THE NEXT LINE")
    print(script)

if __name__ == '__main__':
    main()
