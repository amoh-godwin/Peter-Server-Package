# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 15:52:27 2018
@author: Amoh - Gyebi Godwin
"""
import threading
import socketserver

import sys
import os

from headers import Header

from settings import Sets
sets = Sets()

class Peter(socketserver.BaseRequestHandler):


    """
    The Peter Server Implementation



    """


    def handle(self):

        """
        This is the handler,

        handles the request and response from the server
        """

        # self.request is the request from the client
        #TODO
        # Use real memory size
        max_length = 1000000000
        self.data = self.request.recv(1024).strip()

        current_thread = threading.current_thread()
        #print(current_thread.name)

        useful = str(self.data.split(b'\r\n\r\n')[0], 'utf-8')
        line = useful.splitlines()

        if len(line) > 0:
            req = line[0]
        else:
            req = ""

        req_length = 0
        for l in line:
            if l.startswith('Content-Length:'):
                if ' ' in l:
                    req_length = int(l.split(': ')[-1])
                else:
                    req_length = int(l.split(':')[-1])

        if req_length > max_length:
            return 'Exceeded Maximum limit'
        elif req_length < 1024:
            pass
        else:
            self.data += self.request.recv(req_length).strip()

        # This would be used for logging
        print("{} [Request ] {}".format(self.client_address[0], req))

        # Initialise the header class
        # Make path innocent on any OS
        parent_folder = os.path.realpath(sets.parent_folder)
        peter = Header(parent_folder, sets.addr)

        # send the request to be proccesed
        peter.getRequest(self.data)

        # This is the response from the server
        # to the browser
        resp = peter.computeResponse()

        if len(resp) < 1:
            resp = b''

        # print('{} [Response] {}'.format(self.client_address[0], str(peter.status_code)))

        # Send the complete data to the browser
        self.request.sendall(resp)


class ThreadTCP(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


def _test_another_port(HOST, PORT):

    # Using fallback Peter Port
    _run_server(HOST, 7773)


def _run_server(HOST, PORT):

    try:
        with ThreadTCP((HOST, PORT), Peter) as server:
            pass

    except:
        # Test for another port
        print('Error: Wrong port, testing another port')
        _test_another_port(HOST, PORT)

    else:
        try:
            with ThreadTCP((HOST, PORT), Peter) as server:
                # interrupt the program with Ctrl-C

                print('\n')
                print('Server Started at PORT:', str(PORT))
                print('**********************************')
                print('\n\n')

                server.serve_forever()

        except KeyboardInterrupt:
            print('Keyborad Interrupt, Server has exited')

if __name__ == "__main__":

    # if user passed in any other value
    # should be in the second index
    if len(sys.argv) > 1:

        # set as the new port
        port = int(sys.argv[1])

    else:

        # set it to the native that we are using
        port = 7773

    HOST, PORT = "localhost", port

    # Run the Server
    _run_server(HOST, PORT)
