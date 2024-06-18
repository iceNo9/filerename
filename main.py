import os
import sys
import re

def rename_items(path):
    for root, dirs, files in os.walk(path):
        items = dirs + files  # 合并文件和目录列表
        for name in items:
            # 正则表达式匹配数字，同时允许数字前后有任意非数字字符
            matches = re.findall(r'(?<=\D)(\d+)(?=\D)', name)
            if matches:
                new_name = name  # 初始化新名称为原名称
                for num_str in matches:
                    # 对每个匹配的数字进行四位数补零处理，并替换回原名称中
                    num = int(num_str)
                    formatted_num = f"{num:04d}"
                    new_name = re.sub(rf"(?<=\D){re.escape(num_str)}(?=\D)", formatted_num, new_name)
                # 如果名称有变化，则进行重命名
                if new_name != name:
                    old_path = os.path.join(root, name)
                    new_path = os.path.join(root, new_name)
                    os.rename(old_path, new_path)
                    print(f"Renamed '{old_path}' to '{new_path}'")

def main():
    if len(sys.argv) != 2:  # 检查是否提供了一个参数
        print("Usage: python script.py <directory_path>")
        sys.exit(1)
    
    target_path = sys.argv[1]  # 获取拖放或命令行指定的路径
    rename_items(target_path)

if __name__ == "__main__":
    main()
