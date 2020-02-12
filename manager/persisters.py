from abc import ABCMeta, abstractmethod
from util import util
import json
from time import time
from glob import glob
from os import path
from os import mkdir
from datetime import datetime


class DataSaver(metaclass=ABCMeta):

    @abstractmethod
    def persist(self, data, **kwargs):
        pass


class RawTweetSaver(DataSaver):

    def __init__(self):
        with open('manager\\environment.json') as f:
            self.__environment = json.load(f)
            base_path = self.__environment['base_path']
            prefix = self.__environment['prefix']
            escape = self.__environment ['escape']

            if not path.exists(base_path + escape + prefix):
                mkdir(base_path + escape + prefix)
                mkdir(base_path + escape + prefix + escape + 'errors')
                mkdir(base_path + escape + prefix + escape + 'execution')
                mkdir(base_path + escape + prefix + escape + 'statuses')
                mkdir(base_path + escape + prefix + escape + 'apiMessages')

            self.__out_path = base_path + escape + prefix + escape

    def persist(self, data, **kwargs):
        suffix = kwargs['suffix'] if 'suffix' in kwargs.keys() else datetime.today().strftime('%H%M%S')
        data_type = kwargs['data_type']
        if data_type != 'statuses' and data_type != 'apiMessages':
            raise TypeError('Invalid data Type for API')

        if data_type == 'statuses':
            self.__save_tweet(data, suffix)
        else:
            self.__save_message(data, suffix)

    def __save_tweet(self, data, suffix):
        # start_time = time()
        prefix = self.__environment['prefix']
        escape = self.__environment['escape']
        unicode = self.__environment['unicode']
        max_lines = self.__environment['max_lines']
        fields = self.__environment['fields']

        out_path = self.__out_path + 'statuses' + escape + datetime.today().strftime('%Y')
        if not path.exists(out_path):
            mkdir(out_path, 7777)

        out_path += escape + datetime.today().strftime('%m')
        if not path.exists(out_path):
            mkdir(out_path, 7777)

        out_path += escape + datetime.today().strftime('%d')
        if not path.exists(out_path):
            mkdir(out_path, 7777)

        file_list = glob(out_path + escape + '*')
        if not file_list:
            lastest_file = out_path + escape + prefix + '_' + suffix

        else:
            lastest_file = max(file_list, key=path.getctime)
            if util.count_file_lines(lastest_file) >= max_lines:
                lastest_file = out_path + escape + prefix + '_' + suffix

        to_save = data if fields == 'all' else {field: data[field] for field in fields}
        with open(lastest_file, 'a+', encoding=unicode) as f:
            f.write(json.dumps(to_save) + '\n')

        # last_time = time()
        # print("--- %s seconds ---" % (last_time - start_time))
        # with open('F:\\workfolder\\times\\__save_tweets.csv', 'a') as f:
        #     f.write('%s\n' % (last_time - start_time))

    def __save_message(self, data: dict, suffix: str):
        # start_time = time()
        prefix = self.__environment['prefix']
        escape = self.__environment['escape']
        unicode = self.__environment['unicode']
        max_lines = self.__environment['max_lines']

        out_path = self.__out_path + 'apiMessages' + escape + datetime.today().strftime('%Y')
        if not path.exists(out_path):
            mkdir(out_path, 7777)

        out_path += escape + datetime.today().strftime('%m')
        if not path.exists(out_path):
            mkdir(out_path, 7777)

        out_path += escape + datetime.today().strftime('%d')
        if not path.exists(out_path):
            mkdir(out_path, 7777)

        file_list = glob(out_path + escape + '*')
        if not file_list:
            lastest_file = out_path + escape + prefix + '_' + suffix

        else:
            lastest_file = max(file_list, key=path.getctime)
            if util.count_file_lines(lastest_file) >= max_lines:
                lastest_file = out_path + escape + prefix + '_' + suffix

        with open(lastest_file, 'a+', encoding=unicode) as f:
            f.write(json.dumps(data) + '\n')

        # last_time = time()
        # with open('F:\\workfolder\\times\\__save_tweets.csv', 'a') as f:
        #     f.write('%s\n' % (last_time - start_time))


