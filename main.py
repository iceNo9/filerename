import os
import re
import sys


def rename_files_and_dirs(path, pad_width=4):
    for item in os.listdir(path):
        old_item_path = os.path.join(path, item)
        if os.path.isfile(old_item_path):
            new_name = pad_numbers_in_name(item, pad_width)
            new_item_path = os.path.join(path, new_name)
            os.rename(old_item_path, new_item_path)
            print(f"File renamed: {item} -> {new_name}")
        elif os.path.isdir(old_item_path):
            new_name = pad_numbers_in_name(item, pad_width)
            new_item_path = os.path.join(path, new_name)
            os.rename(old_item_path, new_item_path)
            print(f"Directory renamed: {item} -> {new_name}")
            rename_files_and_dirs(new_item_path, pad_width)


def pad_numbers_in_name(name, width):
    """
    查找名称中的所有数字序列，并将其格式化为指定的宽度。
    """
    # 正则表达式匹配所有的数字序列
    return re.sub(r'\d+', lambda x: x.group().zfill(width), name)


def main(dir_path):
    rename_files_and_dirs(dir_path)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
    else:
        main(sys.argv[1])
