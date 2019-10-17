# -*- coding: utf-8 -*-
# To you Alone oh Father, I commit myself

import os
import subprocess
from urllib.parse import urlencode, unquote
from external_headers import PHPHeader
class PHPRunner():


    """
    Handles the running of php files
    """


    def __init__(self, parent_folder, url):
        super.__self__
        self.cwd = os.getcwd()
        self.parent_folder = parent_folder
        self.host = url
        self.status_str = ""
        self.directory = os.path.join(self.parent_folder, "bin", "php")
        self.server_dir = os.path.join(self.parent_folder, "Server")
        self.document_root = self.server_dir
        self.con_document_root = self.server_dir
        self.queries = ''
        self.method = ''
        self.post_data = ''
        self.cookie_str = ""
        self.user_agent_str = ""
        self.addition_head_str = {}
        self.addition_set_cookie = []
        self.redirect_status = '200'
        self.content_type = ''
        self.encoding = ''
        self.file_name = ''
        self.script_name = ''
        self.path_info = '/'
        self.server_sig = ""
        self.server_software = "Peter (Py/3.7)"
        self.server_name = self.host.replace('http://', '')
        self.server_addr = ""
        self.server_port= ""
        self.server_protocol = 'HTTP/1.1'
        self.request_uri = ''
        self.remote_addr = ""
        self.http_host = self.server_name
        self._content_length = 0
        self.echo = ''
        self.get_stmt = ""
        self.post_stmt = ""
        self.cmd = ""


    def Start(self, file, queries, method ):


        # The variables
        self.file_name = file
        specif_file = file.replace("C:/Deuteronomy Works/Peter/Server", "")
        self.script_name = specif_file
        self.method = method
        self.queries = queries
        self.request_uri = specif_file

        # this will indicate whether we are working with raw data or not
        raw_data = False


        # The functions
        """self.RedStat()
        self.ReqMethod()
        self.ContType()
        self.DocRoot()
        self.ConDocRoot()
        self.ScrFile()
        self.ScrName()
        self.PathInf()
        self.SerSig()
        self.SerSoft()
        self.SerName()
        self.Protocol()
        self.ReqUri()
        self.HTTPHost()
        self.QueryStr()
        self.Cookie()
        self.ContLen()
        self.Echo()
        """

        # run function that make sense only to these methods
        if method == "GET":


            self.content_type = 'text/html'
            #self.QueryStr()
            self.get_stmt = "set \"" + self.RedStat() + "\" & set \"" + self.ReqMethod() + \
            "\" & set \"" + self.ContType() + "\" & set \"" + self.ScrFile() + \
            "\" & set \"" + self.ScrName() + "\" & set \"" + self.PathInf() + \
            "/\" & set \"" + self.SerName() + "\" & set \"" + self.Protocol() + \
            "\" & set \"" + self.ReqUri() + "\" & set \"" + self.HTTPHost() + \
            "\" & set \"" + self.HTTPUserAgent() + \
            "\" & set \"" + self.Cookie() + "\" & set \"" + self.SerSig() + \
            "\" & set \"" + self.SerSoft() + \
            "\" & set \"" + self.SerAddr() + "\" & set \"" + self.SerPort() + \
            "\" & set \"" + self.DocRoot() + \
            "\" & set \"" + self.ConDocRoot() + "\" & set \"" + self.QueryStr() + \
            "\" & php-cgi"
            self.cmd = self.get_stmt

        else:

            self.content_type = "application/x-www-form-urlencoded"
            self.echo = self._handle_post_data(self.post_data)
            self.post_stmt = "set \"" + self.RedStat() + "\" & set \"" + self.ReqMethod() + \
            "\" & set \"" + self.ContType() + "\" & set \"" + self.ScrFile() + \
            "\" & set \"" + self.ScrName() + "\" & set \"" + self.PathInf() + \
            "/\" & set \"" + self.SerName() + "\" & set \"" + self.Protocol() + \
            "\" & set \"" + self.ReqUri() + "\" & set \"" + self.HTTPHost() + \
            "\" & set \"" + self.HTTPUserAgent() + \
            "\" & set \"" + self.Cookie() + "\" & set \"" + self.SerSig() + \
            "\" & set \"" + self.SerSoft() + "\" & set \"" + self.SerAddr() + \
            "\" & set \"" + self.SerPort() + "\" & set \"" + self.DocRoot() + \
            "\" & set \"" + self.ConDocRoot() + "\" & set \"" + self.ConLen() + \
            "\" & set \"" + self.QueryStr() + "\" & echo " + \
            self.Echo() + " | php-cgi"
            self.cmd = self.post_stmt

        # change the directory to the PHP dir=
        os.chdir(self.directory)

        # run the subprocess
        output = subprocess.check_output(self.cmd, shell=True)

        # change dir back to normal
        os.chdir(self.cwd)

        # decode the outuput
        try:
            string = str(output, self.encoding)

            # split into header and body
            string_split = string.split('\r\n\r\n')
            body = string_split[1]

        except:

            # convert to string
            string = str(output)

            # find byte postion where break happens
            # Add four bytes since the last positon is +3, plus the jump
            start = output.find(b'\r\n\r\n') + 4

            # get those bytes only
            body = output[start:]

            # set raw data
            raw_data = True

            # remove extraneous byte data
            new_string = string[2:-1]

            # split now and get the header
            string_split = new_string.split('\\r\\n\\r\\n')

        # get the header
        headers_str = string_split[0]

        # send the header
        header = PHPHeader()
        headers_ext = header.computeHeader(headers_str)
        self.addition_head_str = headers_ext
        self.addition_set_cookie = header.setcookiesheader
        self.status_str = header.status_str
        if 'Location' in self.addition_head_str:
            print('\n', self.host, ":", string, '\n')

        # return the bin
        if raw_data:
            return body
        else:
            return(bytes(body, self.encoding))

    def _handle_post_data(self, data):

        print(unquote(data))
        return unquote(data)

    def RedStat(self):


        # make string
        string = "REDIRECT_STATUS=" + self.redirect_status
        return string


    def ReqMethod(self):


        string = "REQUEST_METHOD=" + self.method
        return string


    def ContType(self):


        string = "CONTENT_TYPE=" + self.content_type
        return string

    def DocRoot(self):

        string = "DOCUMENT_ROOT=" + self.document_root
        return string

    def ConDocRoot(self):

        string = "CONTEXT_DOCUMENT_ROOT=" + self.con_document_root
        return string

    def SerSig(self):

        string = "SERVER_SIGNATURE=" + self.server_sig
        return string

    def SerSoft(self):

        string = "SERVER_SOFTWARE=" + self.server_software
        return string

    def SerAddr(self):

        string = "SERVER_ADDR=" + self.server_addr
        return string

    def SerPort(self):

        string = "SERVER_PORT=" + self.server_port
        return string

    def ScrFile(self):


        string = "SCRIPT_FILENAME=" + self.file_name
        return string


    def ScrName(self):


        string = "SCRIPT_NAME=" + self.script_name
        return string


    def PathInf(self):


        string = "PATHINFO=" + self.path_info
        return string


    def SerName(self):

        if ":" in self.server_name:
            self.server_name = self.server_name.split(":")[0]
        string = "SERVER_NAME=" + self.server_name
        return string


    def Protocol(self):


        string = "SERVER_PROTOCOL=" + self.server_protocol
        return string


    def ReqUri(self):


        string = "REQUEST_URI=" + self.request_uri
        return string


    def HTTPHost(self):


        string = "HTTPHOST=" + self.http_host
        return string

    def Cookie(self):

        string = "HTTP_COOKIE=" + self.cookie_str + ";"
        return string

    def HTTPUserAgent(self):

        string = "HTTP_USER_AGENT=" + self.user_agent_str
        return string

    def QueryStr(self):

        string = "QUERY_STRING=" + self.queries
        return string

    def ConLen(self):

        # convert echo to bytes
        echo_bin = bytes(self.echo, 'utf-8')
        print('echo: ', self.echo, '\n')
        self._content_length = len(echo_bin)  # just an over-estimate

        # make the actual string
        string = "CONTENT_LENGTH=" + str(self._content_length)
        return string


    def Echo(self):


        # replace the ampersand(&) with ^^^&
        new_text = self.echo.replace('&', '^^^&')

        # build the string
        string = new_text
        return string
