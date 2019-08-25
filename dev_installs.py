# -*- coding: utf-8 -*-
import os

BASE_FOLDER = 'C:/Deuteronomy Works/Peter/Server'
BASE_TEST_FOLDER = 'C:/Deuteronomy Works/Peter/Server/_tests'


def install_files(folder, file):
    destination = os.path.join(BASE_TEST_FOLDER, file)
    target = os.path.join(folder, file)

    with open(target, mode='rb') as read_file:

        data = read_file.read()

    with open(destination, mode='wb') as write_file:
        write_file.write(data)


def dev_base():
    if not os.path.exists('C:/Deuteronomy Works/Peter/Server/_tests'):
        os.makedirs('C:/Deuteronomy Works/Peter/Server/_tests')
    else:
        pass

def dev_tests():
    # check if files exist
    cont = os.listdir('_tests')
    if os.listdir(BASE_TEST_FOLDER) == []:
        # copy every to the server's base tests folder
        for each in cont:
            install_files('_tests', each)
    else:
        # contains tests files probably
        pass


def dev_php():
    pass


def dev_mysql():
    pass


def dev_python():
    pass


def install():
    # start installs
    dev_base()
    
    # tests
    dev_tests()
    
    # php
    dev_php()

    # mysql
    dev_mysql()

    # python
    dev_python()


install()
