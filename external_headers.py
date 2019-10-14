# -*- coding: utf-8 -*-
# To you Alone, oh God. I commit myself

class PHPHeader():


    def __init__(self):
        super.__self__
        self.header = {}
        self.setcookiesheader = []


    def computeHeader(self, headers):


        # break on (\\r\\n) or (\r\n)
        splits = headers.split('\r\n')

        # check if splits was successful
        if len(splits) > 1:
            pass

        # else split again
        else:
            splits = headers.split('\\r\\n')
        print(splits)


        # clean it up now
        for header in splits:
            if header.startswith("Set-Cookie:"):
                self._add_send_cookie(header)
                continue
            each_splits = header.split(': ')
            item = each_splits[0]
            value = each_splits[1]
            self.header[item] = value

        if 'Set-Cookie' in self.header:
            print('something wrong')
            self.header['Set-Cookie'] = self.header['Set-Cookie'].replace("C:/Deuteronomy Works/Peter/Server/", "")

        elif 'Content-Disposition' in self.header:
            #self.header['Transfer-Encoding'] = 'chunked'
            self.header['Keep-Alive'] = 'timeout=5, max=100'

        return self.header

    def _add_send_cookie(self, line):

        cleaned = line.replace("C:/Deuteronomy Works/Peter/Server/", "")
        self.setcookiesheader.append(cleaned)
        return
