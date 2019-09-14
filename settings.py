# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 10:44:51 2019

@author: Ampofo
"""
import os
import json
import base64

class Sets():


    def __init__(self):
        super.__init__
        self.sets_file = \
        "3ddb429e2f446edae3406bb9d0799eed7bddda600d9a05fe01d3baaa.settings"
        self.settings = None
        self.server = None
        self.port = None
        self.addr = None
        self.parent_folder = ""
        self.passcode = None
        self.read_file()

    def _encrypt(self, data):
        return base64.b64encode(bytes(str(data), 'ascii'))

    def _decrypt(self, data):
        decoded_data = base64.b64decode(data)
        str_data =  str(decoded_data, 'ascii')
        return str_data.replace("'", '"')

    def read_file(self):

        with open(self.sets_file, mode="rb") as sets_file:
            data = self._decrypt(sets_file.read())
            self.settings = json.loads(data)

        self.parent_folder = self.settings[0]["parent_folder"]
        self.server = self.settings[1]
        self.passcode = self.settings[0]['passcode']
        self.port = self.server[0]["port"]
        if self.port == 80:
            self.addr = "http://localhost/"
        else:
            self.addr = "http://localhost:" + str(self.port) + "/"

    def save_file(self):
        file_path = self.sets_file

        self.settings[1] = self.server

        with open(file_path, mode="wb") as sets_file:
            encoded_data = self._encrypt(self.settings)
            sets_file.write(encoded_data)
