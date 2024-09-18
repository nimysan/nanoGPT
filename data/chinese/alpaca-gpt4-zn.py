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
                            data_list = json.load(json_file)
                            # print(data_list)
                            for data in data_list:  # 遍历列表中的每个字典
                                if 'instruction' in data and 'input' in data and 'output' in data:
                                    # 将标题和作者写入
                                    print(data['instruction'])
                                    outfile.write(f"instruction:{data['instruction']}\n")
                                    outfile.write(f"input:{data['input']}\n")
                                    outfile.write(f"output:{data['output']}\n")


                                    # 在每个条目之后添加额外的换行
                                    outfile.write('\n')
                    except Exception as e:
                        print(f"Error processing {file_path}: {str(e)}")

# 设置根目录和输出文件
root_directory = "sample_dataset"
output_file = "gpt5.txt"

# 遍历根目录下的所有子目录
for dir_name in os.listdir(root_directory):
    dir_path = os.path.join(root_directory, dir_name)
    if os.path.isdir(dir_path) and "test" in dir_name:
        print(f"Processing directory: {dir_path}")
        process_json_files(dir_path, output_file)

 # \process_json_files(os.path.join(root_directory, dir_name), "alpaca_gpt4_data_zh.json")
print(f"All JSON files have been processed and written to {output_file}")