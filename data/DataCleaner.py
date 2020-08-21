import argparse
import re
import os
import shutil
from utils import project_path


_data_path = os.path.join(project_path, 'data/csv/')


def clean_line(line):
    # line = line.replace(u'\u0009', '|')
    line = line.replace('\t', '|')
    line = line.replace(',', '')
    line = line.replace('%', '')
    line = line.replace('$', '')
    line = line.replace('-|', '0|')
    line = line.replace(' |', '|')
    line = re.sub(r'-$', '0', line)
    line = re.sub(r'^Equity\|', 'Equity Growth|', line)
    line = re.sub(r'^Free Cash Flow\|', 'Free Cash Flow Growth|', line)
    return line


def main():
    parser = argparse.ArgumentParser(description='Prepare the fundamental data')
    parser.add_argument('-t', '--ticker', type=str, required=True, help='The ticker of the company (points to the csv file)')
    args = vars(parser.parse_args())
    ticker = args['ticker']

    file_path = os.path.join(_data_path, f'{ticker}.csv')
    temp_file_path = os.path.join(_data_path, f'{ticker}_temp.csv')
    with open(file_path, mode='r', encoding='utf-8') as f, open(temp_file_path, mode='w') as temp:
        for line in f:
            line = clean_line(line)
            temp.write(line)
            # print(line)

    # replace old file
    shutil.move(temp_file_path, file_path)


if __name__ == '__main__':
    main()
