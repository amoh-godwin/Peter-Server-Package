# -*- coding: utf-8 -*-
# To you alone oh, The Father of Jesus, our Lord. I give Glory. Forever and
# Ever, AAAAAAMEN
import time
from fs import FileSystem


class Header():

    """
    This handles the calculation of the header variables.

    Apart from the computeResponse function, every one of the functions
    are returning a string and only a string
    The computeResponse output should be a byte of-course

    """

    def __init__(self):
        super.__self__
        self.host = ''
        self.port = 0
        self.request_method = ''
        self.requested_file = ''
        self.requested_body = ''
        self._encoding = 'utf-8'
        self._extension = ''
        self.Files = FileSystem()
        self._content_length = 0
        self.raw_headers = ""
        self.headerPair = {}
        self.send_headers = {'Server': 'Peter (Python/3.6.1)',
                             'X-Frame-Options': 'SAMEORIGIN',
                             'Accept-Ranges': 'bytes',
                             'Content-Length': '0',
                             'Keep-Alive': 'timeout=5, max=99',
                             'Connection': 'Keep-Alive',
                             'Content-Type': 'text/html'}
        self.data = ''
        self._extMap = {'html': 'text/html', 'htm': 'text/html',
                        'php': 'text/html', 'css': 'text/css',
                        'py': 'text/html',
                        'js': 'application/javascript',
                        'json': 'application/json',
                        'gif': 'image/gif', 'svg': 'image/svg+xml',
                        'jpeg': 'image/jpeg', 'png': 'image/png',
                        'ico': 'image/ico'}
        self.functions = {'Host': self._getHost, 'X-Powered-By': self._powered,
                          'Cookie': self._getCookies}
        self.cookies = {}

    def computeResponse(self):

        """
        Computes the response to be sent back to the browser
        """

        string = ""

        # cookies = {'phpmyadmin': {'phpMyAdmin': "onesdfk", "expires": "Fri,
        # 25-May-2018 09:46:00 GMT", "Max-Age": "2592000",
        # "path": "/phk/jhkl/"},
        # 'user-1': {"user-1": "Jesus", "path": "/path/about/",
        #   "expires": "Fri, 25-May-2018 09:46:00 GMT"}}

        if self.requested_file == '':
            return ''

        # calculation of the data the we will be sending
        self.Files = FileSystem()
        self.Files.request_method = self.request_method
        self._extension = self.Files._file_extension
        self.Files.post_data = self.requested_body
        self.Files.search(self.requested_file)

        # All variables
        self.data = self.Files.data
        self._encoding = self.Files.encoding
        self._extension = self.Files._file_extension
        self._contentType()
        self.send_headers['Content-Length'] = str(self._contentLength())
        status_code = self.Files.status_code

        # status code
        string += self._status(status_code)

        # the actual date this whole event was completed
        string += self._date()

        # *** Coming from PHP  ***
        self.send_headers.update(self.Files.additional_head_str)

        # Header calculator
        for header in self.send_headers:
            string += header
            string += ': '
            string += self.send_headers[header]
            string += '\r\n'

        # this kinda ends the response header
        string += '\r\n'

        # ----
        if self.send_headers['Content-Type'] == 'text/html':
            string += str(self.data)
            return bytes(string + '\r\n', self._encoding)

        elif self.send_headers['Content-Type'] == 'text/css':
            string += str(self.data)
            return bytes(string + '\r\n', self._encoding)

        else:
            total = bytes(string + '\r\n' + self.data, self._encoding)
            return total

    def getRequest(self, header):

        """
        Breaks the req header down to key value pairs and then send them
        to be processed by their corresponding functions.

        """

        # convert from bytes to text
        self.raw_headers = str(header, 'ascii')
        
        if self.raw_headers == '':
            return 1

        # break
        splited = self.raw_headers.split('\r\n\r\n')

        # This is the request body that came
        # if it was a post we will use it
        if len(splited) > 1:
            self.requested_body = splited[-1]
        else:
            self.requested_body = ''

        # clear it to save ram
        splited.clear()

        # Break into individual lines
        lines = self.raw_headers.split('\r\n')

        # This the request either get or post
        # It does not follow the pairing protocol of the rest
        self._getFile(lines[0])

        # Break into key-value pairs
        for pair in lines:

            # for now we are breaking with ': ' to escpace
            # the port no. eg. localhost':'9999
            splits = pair.split(": ")

            # if it was a key-value pair
            if len(splits) > 1:

                # make it a part of the header pair dict
                self.headerPair[splits[0]] = splits[1]

        # loop through the functions we have set and declared
        for func in self.functions:

            # key exist in the headers that was sent by client
            if func in self.headerPair:

                # find its corresponding function and set it to a new variable
                function = self.functions[func]

                # run the function with the self and required values
                # This means, every corresponding function must strictly
                # accept a single value
                function(self.headerPair[func])

    def _getHost(self, hostname_str):

        """
        Gets Host and its port

        """

        # for now just put everything as hostname
        # later we break it
        self.host = hostname_str

    def _getFile(self, req_str):

        """
        """

        # strip the http protocol off
        parsed = req_str[:-8]

        # Strip it by space to avoid escaping the forward-slash
        # There will be three entries
        # the last will just be empty
        splits = parsed.split(' ')

        # the request method (eg. GET or POST)
        self.request_method = splits[0]

        # to avoid an index error
        if len(splits) > 1:

            # the file requested for
            self.requested_file = splits[1]

    def _getCookies(self, cookie_str):

        """
        Breaks the cookie string into individual cookies
        And store them

        """

        # split them in main entries
        splits = cookie_str.split('; ')

        for pair in splits:

            # split into key-value pairs
            pairs = pair.split('=')

            # Add the key-value pairs to the cookies variable
            self.cookies[pairs[0]] = pairs[1]

    def _status(self, digit):
        string = 'HTTP/1.1 '
        string += str(digit) + " OK\r\n"
        return string

    def _date(self):
        string_time = "Date: "
        string_time += time.strftime('%a, %d %b %Y %H:%M:%S %Z')
        return string_time + "\r\n"

    def _contentLength(self):

        ddata = bytes(self.data, self._encoding)

        # len of data from outside
        self._content_length = len(ddata) + 2

        string = 'Content-Length: '

        # Now we are just continuing with the content length string
        if 'Content-Disposition' in self.send_headers:
            string = ''
        else:
            string += str(self._content_length) + '\r\n'
        return self._content_length

    def _cookie(self, cookies=None):

        # set string to empty
        string = ""

        if cookies:

            # cookie's name in cookies multi-dimensional array
            for name in cookies:

                string += "Set-Cookie: "

                # set actual cookie as a "cookie": {}
                cookie = cookies[name]

                # each value that has been listed
                for val in cookie:
                    string += val + "=" + str(cookie[val]) + "; "

                # add the httponly
                string += "HttpOnly\r\n"

        return string

    def _powered(self, statement):

        string = 'X-Powered-By: ' + statement
        return string + "\r\n"

    def _contentType(self):

        # if the encoding detected was ascii use utf-8 instead
        if self._encoding == 'ascii':

            # utf-8 handles a lot more
            encoding = 'utf-8'

        # use the encoding that was given by chardet
        else:

            encoding = self._encoding

        # find the extension in the extension map
        if self._extension in self._extMap:

            # add the corresponding format to the string
            self.send_headers['Content-Type'] = self._extMap[self._extension]

        # if its a css file
        if self._extension in ['css', 'js']:
            pass
        
        elif 'image' in self._extMap[self._extension]:
            pass

        else:

            # it is not a css file
            self.send_headers['Content-Type'] += '; charset=' + encoding

        return  # string + "\r\n"
