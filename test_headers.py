# -*- coding: utf-8 -*-
import pytest
from headers import Header

head = Header()

# set varibles


@pytest.mark.parametrize('filename,cont_type', [
        ('/css.html', 'text/html; charset=utf-8'),
        ('/its.css', 'text/css'),
        ('/its.js', 'application/javascript')])
def test_computeResponse(filename, cont_type):
    head.requested_file = filename
    resp = head.computeResponse()

    str_resp = str(resp, 'utf-8')
    splitted = str_resp.split('\r\n\r\n')
    body_str = splitted[-1]
    body_bytes = bytes(body_str, 'utf-8')
    header_str = splitted[0]
    header_pair = {}

    # see headers
    lines = header_str.split('\r\n')
    for pair in lines:

        # for now we are breaking with ': ' to escpace
        # the port no. eg. localhost':'9999
        splits = pair.split(": ")

        # if it was a key-value pair
        if len(splits) > 1:

            # make it a part of the header pair dict
            header_pair[splits[0]] = splits[1]

    assert type(resp) == bytes
    assert header_pair['Server'] == 'Peter (Python/3.6.1)'
    assert int(header_pair['Content-Length']) == len(body_bytes)
    assert header_pair['Content-Type'] == cont_type


def test__getHost():
    pass
    # head._getHost()

  
def test__getFile():
    pass
    # head._getFile()


def test__getCookies():
    pass
    # head.__getCookies()


def test__status():
    pass
    # head.__status()


def test__date():
    pass
    # head.__date()


def test__contentLength():
    pass
    # head._contentLen()


def test__cookie():
    pass
    # head


@pytest.mark.parametrize('extension,cont_type', [
        ('html', 'text/html; charset=utf-8'),
        ('css', 'text/css'),
        ('js', 'application/javascript')])
def test__contentType(extension, cont_type):
    head._extension = extension
    head._contentType()
    assert head.send_headers['Content-Type'] == cont_type
