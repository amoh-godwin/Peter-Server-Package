# -*- coding: utf-8 -*-
# To You Alone Oh Father, I commit myself
import os
import chardet
from time import time
from external import PHPRunner
from css_fs import CssRunner
from py_fs import PyRunner
from mime_types import mime_font_type, mime_font_aux_name, \
mime_audio_type, mime_audio_aux_name, mime_model_type, mime_model_aux_name, \
mime_multipart_type, mime_multipart_aux_name, mime_message_type, \
mime_message_aux_name, mime_text_type, mime_text_aux_name, \
mime_video_type, mime_video_aux_name, \
mime_app_type, mime_app_aux_name, mime_image_type, mime_image_aux_name

class FileSystem():


    """
    File system
    sets the actual file name (folders are treated as files)
    sets the file type
    returns the encoding
    returns the data
    """


    def __init__(self, parent_folder, url):


        super.__self__
        self.request_method = ''
        self.parent_folder = parent_folder
        self.host = url
        self.Default_LOCATION = os.path.join(self.parent_folder, "Server")
        self.status_code = 200
        self.additional_head_str = {}
        self._actual_file = ''
        self.query_string = ''
        self.post_data = ''
        self.cookies = {}
        self.cookie_str = ""
        self._no = 0
        self._steps = []
        self._depth = 0
        self.SCRIPTS_LOCATION = os.path.join(self.parent_folder, "_scripts")
        self._file_extension = 'html'
        self.mime_type = ''
        self.mime_font_type = mime_font_type
        self.mime_audio_type = mime_audio_type
        self.mime_model_type = mime_model_type
        self.mime_multipart_type = mime_multipart_type
        self.mime_message_type = mime_message_type
        self.mime_text_type = mime_text_type
        self.mime_video_type = mime_video_type
        self.mime_app_type = mime_app_type
        self.mime_image_type = mime_image_type
        self.data = ''
        self.encoding = 'UTF-8'
        self.contentLength = 0


    def _getFileName(self, requested_file):


        # first split to reveal query if any
        # query will be in the second one without the '?' if any
        splits = requested_file.split('?')

        # query should be here
        if len(splits) > 1:
            self.query_string = splits[1]

        # whether or not is a query we are still taken the file only
        self._actual_file = splits[0]

        if self._actual_file == '/':
            pass
        else:
            # the extension will be in the last one
            split = self._actual_file.split('.')
            self._file_extension = split[-1]


    def search(self, file):

        # call to find actual file name
        self._getFileName(file)
 
        # this are the steps we'll use and depth we have to go
        self._steps = self._actual_file.split('/')

        # some clean ups
        del self._steps[0]

        # the depth of the path
        self._depth = len(self._steps)

        # try to open the file
        try:

            # try to find oepn file here
            # INITIALISE THE COUNTER
            self._no = 0

            if self._steps[self._no] == '':
                self._to_list(self.Default_LOCATION)

            else:

                # call
                folders = os.listdir(self.Default_LOCATION)
                if self._steps[self._no] in folders:

                    # if that step is here then we continue
                    item = self.Default_LOCATION + '/' + self._steps[self._no]

                    if self._is_dir(item):

                        # check if blank ''
                        self._is_blank(item)

                    else:

                        # its a file return it
                        self._data(item)

                else:

                    # will couldn't find the file in the nest
                    self.status_code = 404
                    return self.status_code

            # status code found
            return self.status_code

        except:

            # status code not found
            self.status_code = 404
            return self.status_code


    def _crawl(self, path, needle):

        folders = os.listdir(path)
        if needle in folders:

            # make new path
            item = path + '/' + needle

            # find if is file or dir
            if self._is_dir(item):

                # continue crawling is a dir
                self._is_blank(item)

            else:

                # return, it is a file
                # data will be ready in self.data
                self._data(item)

        else:

            # we couldn't find it means we have ended
            self.status_code = 404
            return

    def _is_blank(self, path):

        # depths
        self._no += 1

        # check if the current no is not blank
        if self._no == self._depth:

            self._to_list(path)

        elif self._steps[self._no] != '':

            # crawl again
            # needle is second param
            self._crawl(path, self._steps[self._no])

        else:

            # to dir listing or index.html
            self._to_list(path + '/' + self._steps[self._no])


    def _is_dir(self, path):
        try:
            os.listdir(path)
            return True
        except:
            return False


    def _to_list(self, path):


        """
        checks whether this particular path has an index file in it
        or Peter should go ahead and check the .htaccess for listing perm.
        """


        files = os.listdir(path)

        if 'index.php' in files:

            # file extension sure contains gibberish
            self._file_extension = 'php'

            # call self._data to handle
            self._data(path + '/index.php')

        elif 'index.html' in files:

            # file extension sure contains gibberish
            self._file_extension = 'html'

            # call self.data to handle
            self._data(path + '/index.html')

        elif '.htaccess' in files:

            # file extension sure contains gibberish
            self._file_extension = 'html'

            # call to permission reader
            with open(path + '/.htaccess', mode='rb') as ht:
                data = ht.read()

            # working on the file line by line
            if b'Options -Indexes' in data:

                # returnt the 403 document instead
                self._data(self.SCRIPTS_LOCATION + '/403.html')

            else:

                # sure we're going to list
                self._data(self.SCRIPTS_LOCATION + '/dir.html')

        else:

            # file extension sure contains gibberish
            #self._file_extension = 'php'

            # htacces or just go ahead to list dir
            self._data(self.SCRIPTS_LOCATION + '/dir.html' )

    def _base_read(self, file):

        with open(file, 'rb') as bbin:
                read = bbin.read()
        self.data = read
        self.contentLength = len(read)

    def _data(self, file):

        # check the file extension for php
        if self._file_extension == 'py':

            pyrunner = PyRunner()
            read = pyrunner.start(file)
            
            # return values
            self.contentLength = len(read)
            self.encoding = pyrunner.encoding
            self.data = read
            return

        elif self._file_extension == 'php':

            # setting the directory to directory
            phpRunner = PHPRunner(self.parent_folder, self.host)

            # run with php and with the query
            phpRunner.encoding = self.encoding
            phpRunner.post_data = self.post_data
            phpRunner.cookie_str = self.cookie_str
            read = phpRunner.Start(file,
                                   self.query_string,
                                   self.request_method)
            self.additional_head_str = phpRunner.addition_head_str

            # set length of the content
            self.contentLength = len(read)
            self.encoding = phpRunner.encoding
            self.data = read
            return

        elif self._file_extension in mime_text_aux_name:

            self.mime_type = 'text/' + mime_text_aux_name[self._file_extension]

            Css = CssRunner()
            Css.Read(file)
            self.contentLength = Css.content_length
            self.data = Css.read
            self.encoding = Css.encoding
            return

        elif self._file_extension in self.mime_text_type:

            # The file is a text file
            self.mime_type = 'text/' + self._file_extension

            Css = CssRunner()
            Css.Read(file)
            self.contentLength = Css.content_length
            self.data = Css.read
            self.encoding = Css.encoding
            return

        elif self._file_extension in mime_image_aux_name:
            # set correct content type here
            self.mime_type = "image/" + mime_image_aux_name[self._file_extension]
            self._base_read(file)
            return

        elif self._file_extension in mime_font_aux_name:
            self.mime_type = "font/" + mime_font_aux_name[self._file_extension]
            self._base_read(file)
            return

        elif self._file_extension in mime_audio_aux_name:
                self.mime_type = "audio/" + mime_audio_aux_name[self._file_extension]
                self._base_read(file)
                return

        elif self._file_extension in mime_app_aux_name:
            self.mime_type = "application/" + mime_app_aux_name[self._file_extension]
            self._base_read(file)
            return

        elif self._file_extension in mime_video_aux_name:
            self.mime_type = "video/" + mime_video_aux_name[self._file_extension]
            self._base_read(file)
            return

        elif self._file_extension in mime_multipart_aux_name:
            self.mime_type = "multipart/" + mime_multipart_aux_name[self._file_extension]
            self._base_read(file)
            return

        elif self._file_extension in mime_message_aux_name:
            self.mime_type = "message/" + mime_message_aux_name[self._file_extension]
            self._base_read(file)
            return

        elif self._file_extension in mime_model_aux_name:
            self.mime_type = "model/" + mime_model_aux_name[self._file_extension]
            self._base_read(file)
            return

        elif self._file_extension in self.mime_image_type:
            self.mime_type = "image/" + self._file_extension
            self._base_read(file)
            return

        elif self._file_extension in self.mime_font_type:
            self.mime_type = "font/" + self._file_extension
            self._base_read(file)
            return

        elif self._file_extension in self.mime_audio_type:
            self.mime_type = "audio/" + self._file_extension
            self._base_read(file)
            return

        elif self._file_extension in self.mime_app_type:
            self.mime_type = "app/" + self._file_extension
            self._base_read(file)
            return

        elif self._file_extension in self.mime_video_type:
            self.mime_type = "video/" + self._file_extension
            self._base_read(file)
            return

        elif self._file_extension in self.mime_multipart_type:
            self.mime_type = "multipart/" + self._file_extension
            self._base_read(file)
            return

        elif self._file_extension in self.mime_message_type:
            self.mime_type = "message/" + self._file_extension
            self._base_read(file)
            return

        elif self._file_extension in self.mime_model_type:
            self.mime_type = "model/" + self._file_extension
            self._base_read(file)
            return

        else:

            # file is not php
            with open(file, 'rb') as bbin:
                read = bbin.read()

                # set length of the content
                self.contentlength = len(read)

        # Continue with encoding detection
        ## Use only 128 bytes to speed things up
        count = 0
        to_send_bytes = b''
        split_bytes = read.splitlines(keepends=True)
        for each in split_bytes:
            if count < 128:
                to_send_bytes += each
                count += 1

        detection = chardet.detect(to_send_bytes)

        if detection['confidence'] > 0.99:
            self.encoding = detection['encoding']

        # if detection in none
        elif detection['confidence'] < 0.1:
            self.data = read
            self.contentLength = len(read)
    
            # it should return, nothing else to do
            return
        else:
            self.encoding = 'ascii'

        self.data = read.decode(self.encoding)
        return
