# -*- coding: utf-8 -*-

class CssRunner():


    def __init__(self):
        super.__self__


    def Read(self, file):


        # print the file
        with open(file, 'rb') as css_file:
            read = css_file.read()
        return read