import subprocess
import os
import sys

formatters = {
    'RED': '\033[91m',
    'GREEN': '\033[92m',
    'END': '\033[0m',
}

symbol = sys.argv[1]
windows_length = sys.argv[2]
dimension = sys.argv[3]

training_start_date = "2017-01-01"
training_end_date = "2021-12-31"

testing_start_date = "2022-01-01"
testing_end_date = "2022-05-23"

download_data = True
onlytesting = True
onlytraining = True
use_volume = True

try:
    if download_data:
        if onlytesting:
            # get data testing
            print('{RED}\nGet Testing Data{END}'.format(**formatters))
            subprocess.call(
                f'python utils/get_data.py -sd {testing_start_date} -ed {testing_end_date} -t {symbol} -s yahoo -p testing', shell=True)
            print('{GREEN}Get Testing Data Done\n{END}'.format(**formatters))
        if onlytraining:
            # get data testing
            print('{RED}\nGet Training Data{END}'.format(**formatters))
            subprocess.call(
                f'python utils/get_data.py -sd {training_start_date} -ed {training_end_date} -t {symbol} -s yahoo -p training', shell=True)
            print('{GREEN}Get Training Data Done\n{END}'.format(**formatters))
except Exception as identifier:
    print(identifier)

try:
    if onlytraining:
        # create label training
        print('{RED}\nCreate Label Training Data{END}'.format(**formatters))
        subprocess.call(f'python preproccess_binclass.py -m createLabel -l {windows_length} -i stockdatas/{symbol}_training.csv', shell=True)
        print('{GREEN}Create Label Training Data Done\n{END}!'.format(**formatters))
    if onlytesting:
        # create label testing
        print('{RED}\nCreate Label Testing Data{END}'.format(**formatters))
        subprocess.call(f'python preproccess_binclass.py -m createLabel -l {windows_length} -i stockdatas/{symbol}_testing.csv', shell=True)
        print('{GREEN}Create Label Testing Data Done\n{END}'.format(**formatters))
except Exception as identifier:
    print(identifier)

try:
    if onlytraining:
        # convert to candlestick chart training data
        print('{RED}\nConvert Training Data to Candlestik{END}'.format(**formatters))
        subprocess.call(
            f'python preproccess_binclass.py -m ohlc2cs -l {windows_length} -i stockdatas/{symbol}_training.csv -t training -d {dimension} -v {use_volume}', shell=True)
        print('{GREEN}Convert Training Data to Candlestik Done\n{END}'.format(
            **formatters))
    if onlytesting:
        # convert to candlestick chart testing data
        print('{RED}\nConvert Testing Data to Candlestik{END}'.format(**formatters))
        subprocess.call(
            f'python preproccess_binclass.py -m ohlc2cs -l {windows_length} -i stockdatas/{symbol}_testing.csv -t testing -d {dimension} -v {use_volume}', shell=True)
        print('{GREEN}Convert Testing Data to Candlestik Done\n{END}'.format(
            **formatters))
except Exception as identifier:
    print(identifier)

try:
    if onlytraining:
        # labelling data training
        print('{RED}\nLabelling Training Data{END}'.format(**formatters))
        print(f'python preproccess_binclass.py -m img2dt -i dataset/{windows_length}_{dimension}/{symbol}/training -lf {symbol}_training_label_{windows_length}.txt')
        subprocess.call(
            f'python preproccess_binclass.py -m img2dt -i dataset/{windows_length}_{dimension}/{symbol}/training -lf {symbol}_training_label_{windows_length}.txt', shell=True)
        print('{GREEN}Labelling Training Data Done\n{END}'.format(**formatters))
    if onlytesting:
        # labelling data testing
        print('{RED}\nLabelling Testing Data{END}'.format(**formatters))
        subprocess.call(
            f'python preproccess_binclass.py -m img2dt -i dataset/{windows_length}_{dimension}/{symbol}/testing -lf {symbol}_testing_label_{windows_length}.txt', shell=True)
        print('{GREEN}Labelling Testing Data Done\n{END}'.format(**formatters))
except Exception as identifier:
    print(identifier)
