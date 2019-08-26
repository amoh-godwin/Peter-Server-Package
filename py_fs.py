# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:21:19 2019

@author: Ampofo
"""
import subprocess
import threading

import os

class PyRunner():


    def __init__(self):
        super.__self__
        self.path_to_python = "python"
        self.datas = ""
        self.run_file = ''
        self.encoding = 'ascii'

    def start(self, file):
        self.run_file = file
        return self._call_python()

    def _call_python(self):
        command = self.path_to_python + ' "' + self.run_file + '" ' + self.datas
        process = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT,
                         shell=True)
        lines = process.stdout.readlines()
        d = str(lines[0], 'utf-8')
        return str(d)

