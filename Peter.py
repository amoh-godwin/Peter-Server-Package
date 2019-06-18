# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 15:52:27 2018
@author: Amoh - Gyebi Godwin
# To You oh, LORD i commit myself
"""
import threading
import socketserver

import sys

from headers import Header

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
        self.data = self.request.recv(1024).strip()

        current_thread = threading.current_thread()
        #print(current_thread.name)

        # This would be used for logging
        print("{} requested".format(self.client_address[0]))

        # The data that the browser came with
        # basically the request handler
        print(self.data)
        
        print('\n\n')

        # Initialise the header class
        peter = Header()

        # send the request to be proccesed
        Header.getRequest(peter, self.data)

        # This is the response from the server
        # to the browser
        resp = Header.computeResponse(peter)
        
        # print resp
        print('\n\n\n', resp, '\n\n\n')

        # Send the complete data to the browser
        self.request.sendall(resp)


class ThreadTCP(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


if __name__ == "__main__":

    # if user passed in any other value
    # should be in the second index
    if len(sys.argv) > 1:

        # set as the new port
        port = sys.argv[1]

    else:

        # set it to the native that we are using
        port = 7773

    HOST, PORT = "localhost", port

    with ThreadTCP((HOST, PORT), Peter) as server:
        # interrupt the program with Ctrl-C
        
        print('\n\n')
        print('Server Started at PORT:', str(port))
        print('**********************************')
        print('\n\n\n')
        
        server.serve_forever()
