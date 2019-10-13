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

    def __init__(self, parent_folder, url):
        super.__self__
        self.parent_folder = parent_folder
        self.host = url
        self.port = 0
        self.request_method = ''
        self.requested_file = ''
        self.requested_body = ''
        self._encoding = 'UTF-8'
        self._extension = ''
        self.Files = FileSystem(self.parent_folder, self.host)
        self._content_length = 0
        self.raw_headers = ""
        self.status_code = 0
        self.headerPair = {}
        self.status_stat = {
                200: 'OK', 300: 'NOT FOUND', 301: 'MOVED PERMANENTLY',
                302: 'FOUND', 303: 'SEE OTHER', 304: 'NOT MODIFIED',
                            307: 'Temporary Redirect',
                            308: 'Permanent Redirect',
                            400: 'Bad Request',
                            401: 'Unathourized',
                            402: 'Payment Required',
                            403: 'Forbidden',
                            404: 'NOT FOUND',
                            405: 'Method Not Allowed',
                            406: 'Not Acceptable',
                            407: 'Proxy Authentication Required',
                            408: 'Request Timeout',
                            409: 'Conflict',
                            410: 'Gone',
                            411: 'Length Required',
                            412: 'Precondition Failed',
                            413: 'Payload Too Large',
                            414: 'URI Too Long',
                            415: 'Unsupported Media Type',
                            416: 'Requested Range Not Satisfiable',
                            417: 'Expectation Failed',
                            418: "I'm a teapot",
                            421: 'Misdirected Request',
                            422: 'Unprocessable Entity',
                            423: 'Locked',
                            424: 'Failed Dependency',
                            425: 'Too Early',
                            426: 'Upgrade Required',
                            428: 'Precondition Required',
                            429: 'Too Many Requests',
                            431: 'Request Header Fields Too Large',
                            451: 'Unavailable For Legal Reasons',
                            500: 'Internal Server Error',
                            501: 'Not Implemented',
                            502: 'Bad Gateway',
                            503: 'Service Unavailable',
                            504: 'Gateway Timeout',
                            505: 'HTTP Version Not Supported',
                            506: 'Variant Also Negotiates',
                            507: 'Insufficient Storage',
                            508: 'Loop Detected',
                            510: 'Not Extended',
                            511: 'Network Authentication Required'}

        self.send_headers = {'Server': 'Peter (Python/3.7)',
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
                        'png': 'image/png', 'jpeg': 'image/jpeg',
                        'gif': 'image/gif', 'svg': 'image/svg+xml',
                        'tiff': 'image/tiff', 'aces': 'image/aces',
                        'avci': 'image/avci', 'avcs': 'image/avcs',
                        'bmp': 'image/bmp', 'cgm': 'image/cgm',
                        'dicom-rle': 'image/dicom-rle',
                        'emf': 'image/emf', 'example': 'image/example',
                        'fits': 'image/fits', 'g3fax': 'image/g3fax',
                        'heic': 'image/heic',
                        'heic-sequence': 'image/heic-sequence',
                        'heif': 'image/heif',
                        'heif-sequence': 'image/heif-sequence',
                        'hej2k': 'image/hej2k', 'hsj2': 'image/hsj2',
                        'ief': 'image/ief', 'jls': 'image/jls',
                        'jp2': 'image/jp2', 'jph': 'image/jph',
                        'jphc': 'image/jphc', 'jpm': 'image/jpm',
                        'jpx': 'image/jpx', 'jxr': 'image/jxr',
                        'jxrA': 'image/jxrA', 'jxrS': 'image/jxrS',
                        'jxs': 'image/jxs', 'jxsc': 'image/jxsc',
                        'jxsi': 'image/jxsi', 'jxss': 'image/jxss',
                        'ktx': 'image/ktx', 'naplps': 'image/naplps',
                        'prs.btif': 'image/prs.btif',
                        'prs.pti': 'image/prs.pti',
                        'pwg-raster': 'image/pwg-raster',
                        't38': 'image/t38', 'tiff-fx': 'image/tiff-fx',
                        'wmf': 'image/wmf', 'ico': 'image/ico'}
        self.functions = {'Host': self._getHost, 'X-Powered-By': self._powered,
                          'Cookie': self._getCookies}
        self.cookies = {}
        self.cookie_str = ""

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
        self.Files = FileSystem(self.parent_folder, self.host)
        self.Files.request_method = self.request_method
        self._extension = self.Files._file_extension
        self.Files.post_data = self.requested_body
        self.Files.cookies = self.cookies
        self.Files.cookie_str = self.cookie_str
        self.Files.search(self.requested_file)

        # All variables
        self.data = self.Files.data
        self._encoding = self.Files.encoding
        self._content_length = self.Files.contentLength
        self._extension = self.Files._file_extension
        self._contentType()
        self.send_headers['Content-Length'] = str(self._contentLength())
        self.status_code = self.Files.status_code

        # status code
        string += self._status(self.status_code)

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
        if type(self.data) == str:
            total = bytes(string + self.data, self._encoding)
        else:
            total = bytes(string, self._encoding) + self.data
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
        print('_getCookies')
        self.cookie_str = cookie_str
        splits = cookie_str.split('; ')

        for pair in splits:

            # split into key-value pairs
            pairs = pair.split('=')

            # Add the key-value pairs to the cookies variable
            self.cookies[pairs[0]] = pairs[1]
        print('cookies: ', self.cookies)

    def _status(self, digit):
        string = 'HTTP/1.1 '
        string += str(digit) + " " + self.status_stat[digit] + "\r\n"
        return string

    def _date(self):
        string_time = "Date: "
        string_time += time.strftime('%a, %d %b %Y %H:%M:%S %Z')
        return string_time + "\r\n"

    def _contentLength(self):

        if self._content_length:
            return self._content_length
        else:
            if type(self.data) == bytes:
                self._content_length = len(self.data)
    
            else:
                ddata = bytes(self.data, self._encoding)
        
                # len of data from outside
                self._content_length = len(ddata)
    
            """string = 'Content-Length: '
    
            # Now we are just continuing with the content length string
            if 'Content-Disposition' in self.send_headers:
                string = ''
            else:
                string += str(self._content_length) + '\r\n'"""
    
            return self._content_length

    def _cookie(self, cookies=None):

        # set string to empty
        print('cooki: ', cookies)
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

        print(string)
        return string

    def _powered(self, statement):

        string = 'X-Powered-By: ' + statement
        return string + "\r\n"

    def _contentType(self):

        # If content type has already been set
        if self.Files.mime_type:

            self.send_headers['Content-Type'] = self.Files.mime_type
            if self.send_headers['Content-Type'] == 'text/html':
                self.send_headers['Content-Type'] += '; charset=' + self._encoding

        # find the extension in the extension map
        elif self._extension in self._extMap:

            # add the corresponding format to the string
            self.send_headers['Content-Type'] = self._extMap[self._extension]

        # if its a css file
        elif self._extension in ['css', 'js']:
            pass
        
        elif 'image' in self._extMap[self._extension]:
            pass

        else:

            # it is not a css file
            self.send_headers['Content-Type'] += '; charset=' + self._encoding

        return
