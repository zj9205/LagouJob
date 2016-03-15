import xlrd
import os
import json


def json_to_excel(json_file_dir):
    for each_json_file in os.listdir(json_file_dir):
        with open(json_file_dir + '/' + each_json_file, 'r', encoding='utf-8') as f:
            for each_job in f.readlines():
                print(each_job)


if __name__ == '__main__':
    json_to_excel('h:/Java')
