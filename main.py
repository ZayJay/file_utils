# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import sys

CMD_LIST_DIR = "--ld"
CMD_RENAME_WEX_HEALTH_RECEIPT = "--wex-rename"

#
# List Directory -ld path
#
def run_ld(args):
    idx_cmd = args.index("-ld")
    path = args[idx_cmd + 1]
    print("CONTENTS START (\"{}\"):".format(path))
    for item in os.listdir(path):
        print(item)
    print("CONTENTS END")

def run_wex_receipt_rename(args):
    original_dir = os.getcwd()

    idx_cmd = args.index("--wex-receipt-rename")


    os.chdir(path)
    files = os.listdir()

    for f in files

def get_command_index(cmd, args):
    if cmd in args:
        return args.index(cmd)
    else:
        return None
def execute(args):
    if get_command_index(CMD_LIST_DIR) : run_ld(args)
    if "--wex-receipt-rename" in args: run_wex_receipt_rename(args)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    args = sys.argv[1:]
    execute(args)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
