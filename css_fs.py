# -*- coding: utf-8 -*-
from time import time
import chardet

class CssRunner():


    def __init__(self):
        super.__self__
        self.content_length = 0
        self.encoding = ''
        self.read = b''


    def Read(self, file):

        # print the file
        with open(file, mode='rb') as css_file:
            read = css_file.read()
            self.content_length = len(read)
            self.read = read
        self._detect_encoding(file)
        return

    def _detect_encoding(self, file):

        with open(file, mode='rb') as raw_file:
            some_data = raw_file.read(1024)
            detection = chardet.detect(some_data)
            if detection['confidence'] > 0.7:
                self.encoding = detection['encoding']
            else:
                self.encoding = 'UTF-8'
