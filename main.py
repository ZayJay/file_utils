# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files,
# tool windows, actions, and settings.

import os
import sys
import shutil


CMD_LIST_DIR = "--ld"
CMD_RENAME_WEX_HEALTH_RECEIPT = "--wex-rename"

#
# List Directory -ld path
#
def run_ld(args):
    idx_cmd = get_command_index(CMD_LIST_DIR, args)
    path = args[idx_cmd + 1]
    print("CONTENTS START (\"{}\"):".format(path))
    for item in os.listdir(path):
        print(item)
    print("CONTENTS END")

def run_wex_receipt_rename(args):
    original_dir = os.getcwd()

    idx_cmd = get_command_index(CMD_RENAME_WEX_HEALTH_RECEIPT, args)
    path = args[idx_cmd + 1]
    os.chdir(path)

    files = os.listdir()
    wex_files = list(filter(lambda x: is_valid_wex_file(x), files))

    print("COPYING {} FILES".format(len(wex_files)))

    result_folder = "new_files"

    # Create empty results folder
    if result_folder in files:
        shutil.rmtree(result_folder)
    os.mkdir(result_folder)

    # Copy wex files to new folder w/ changed names
    date_len = 6  # YYYYMM date format
    file_suffix = ".pdf"
    for filename in wex_files:
        idx_eofn = filename.find(file_suffix)
        datepart = filename[-(date_len + len(file_suffix)):idx_eofn]
        new_filename = "./{folder}/{filepart}_wex_payment_receipt.pdf".format(
            folder=result_folder, filepart=datepart
        )
        shutil.copy2(filename, new_filename)

    print("NEW FILES START")
    for item in os.listdir(result_folder):
        print(item)
    print("NEW FILES END")

    os.chdir(original_dir)
    

def is_valid_wex_file(file):
    is_valid = True
    if "WEX Health, Inc. - Thank You-" not in file or ".pdf" not in file:
        is_valid = False
    return is_valid


#
# Get index of command, return None if not found
#
def get_command_index(cmd, args):
    if cmd in args:
        return args.index(cmd)
    else:
        return None
#
# Execute command line commands
#
def execute(args):
    if get_command_index(CMD_LIST_DIR, args) is not None :
        run_ld(args)
    if get_command_index(CMD_RENAME_WEX_HEALTH_RECEIPT, args) is not None:
        run_wex_receipt_rename(args)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    args = sys.argv[1:]
    execute(args)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
