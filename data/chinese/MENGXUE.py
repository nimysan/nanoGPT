import os
import json

def process_json_files(root_dir, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk(root_dir):
            for file in files:
                if file.endswith('.json'):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as json_file:
                            print(file_path)
                            # data = json.load(json_file)json_file
                            # print('data '+ json_file)
                            data = json.load(json_file)
                            if 'title' in data and 'author' in data and 'paragraphs' in data:
                                    # 将标题和作者写入
                                    outfile.write(f"{data['title']}\n作者:{data['author']}\n")

                                    # 将paragraphs中的每个元素作为单独的一行写入
                                    if isinstance(data['paragraphs'], list):
                                        for paragraph in data['paragraphs']:
                                            outfile.write(f"{paragraph}\n")
                                    else:
                                        # 如果不是列表，就直接写入
                                        outfile.write(f"{data['paragraphs']}\n")

                                    # 在每个条目之后添加额外的换行
                                    outfile.write('\n')

                    except Exception as e:
                        print(f"Error processing {file_path}: {str(e)}")

# 设置根目录和输出文件
root_directory = "chinese-poetry"
output_file = "output.txt"

# 遍历根目录下的所有子目录
for dir_name in os.listdir(root_directory):
    dir_path = os.path.join(root_directory, dir_name)
    if os.path.isdir(dir_path) and "蒙学" in dir_name:
        print(f"Processing directory: {dir_path}")
        process_json_files(dir_path, output_file)

print(f"All JSON files have been processed and written to {output_file}")