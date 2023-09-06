import fileinput
import os

#row start from 0
def filter_files(target_line_numbers, replace_file, replace_char):
    filename = replace_file 

    with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
        for line_number, line in enumerate(file, start=0):
            # 如果行号在目标列表中，且行不为空
            if line_number in target_line_numbers and line.strip():
                # 使用字符串的切片将最后一个字符替换为新字符
                new_line = line[:-2] + replace_char + '\n'
            else:
                new_line = line
            print(new_line, end='')
    os.remove(f"{filename}.bak")

if __name__ == "__main__":
    rows = [0,2,4]
    filter_files(rows, "test.txt", '0')
    print("done")
