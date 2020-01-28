import argparse
import re
import os
import shutil


def clean_line(line):
    # line = line.replace(u'\u0009', '|')
    line = line.replace('\t', '|')
    line = line.replace(',', '')
    line = line.replace('%', '')
    line = line.replace('$', '')
    line = line.replace('-|', '0|')
    line = line.replace(' |', '|')
    line = re.sub(r'^Equity\|', 'Equity Growth|', line)
    line = re.sub(r'^Free Cash Flow\|', 'Free Cash Flow Growth|', line)
    return line


def main():
    parser = argparse.ArgumentParser(description='Prepare the fundamental data')
    parser.add_argument('-t', '--ticker', type=str, required=True, help='The ticker of the company (points to the csv file)')
    args = vars(parser.parse_args())
    ticker = args['ticker']

    filename = '{}.csv'.format(ticker)
    temp_file = '{}_temp.csv'.format(ticker)
    with open(filename, mode='r', encoding='utf-8') as f, open(temp_file, mode='w') as temp:
        for line in f:
            line = clean_line(line)
            temp.write(line)
            # print(line)
    
    # replace old file
    shutil.move(temp_file, filename)


if __name__ == '__main__':
    main()
