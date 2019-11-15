# -*- coding: utf-8 -*-
import pytest
from urllib.parse import quote, quote_plus, unquote_plus
from headers import Header
from settings import Sets

sets = Sets()
head = Header(sets.parent_folder, sets.addr)

@pytest.mark.parametrize('req', [('get=love'),
                                 ('get=777&post=sure'),
                                 ('get=777&post=sure or not'),
                                 ('get=777&post=sure+or+not'),
                                 ('slash=last/laugh'),
                                 ('percent=100%20percent')])
def test_php_get_req(req):
    request = quote(req, safe='/=&')

    if '&' in req:
        main_splits = req.split('&')
    else:
        main_splits = [req]
    string = 'array(' + str(len(main_splits)) + ')' + ' {\n'
    for requ in main_splits:
        splits = requ.split('=')
        string += '  ["' + splits[0] + '"]=>\n  string(' + \
        str(len(splits[1])) + ') "' + splits[1] + '"\n'
    string += '}\n'
    ret_value = string
    print('ret: ', ret_value)

    req_string = 'GET /_tests/phpGetReq.php?' + request + ' HTTP/1.1'

    head.getRequest(bytes(req_string, 'utf-8'))
    resp = head.computeResponse()

    str_resp = str(resp, 'UTF-8')
    splitted = str_resp.split('\r\n\r\n')
    body_str = splitted[-1]
    print('splits: ', str_resp)
    
    assert body_str == ret_value


@pytest.mark.parametrize('req', [('ordinarytext'),
                                 ('ordinary text'),
                                 ('4'),
                                 ('~`!@#$%^&*()_-+=')])
def test_php_post_req(req):
    parsed = quote_plus(req)
    request = req = 'test_string=' + parsed

    if '&' in req:
        main_splits = req.split('&')
    else:
        main_splits = [req]
    string = 'array(' + str(len(main_splits)) + ')' + ' {\n'
    for requ in main_splits:
        splits = requ.split('=')
        splits[1] = unquote_plus(splits[1])
        string += '  ["' + splits[0] + '"]=>\n  string(' + \
        str(len(splits[1])) + ') "' + splits[1] + '"\n'
    string += '}\n'
    ret_value = string
    print('ret: ', ret_value)

    req_string = 'POST /_tests/phpPostReq.php HTTP/1.1\r\n\r\n' + request

    head.getRequest(bytes(req_string, 'utf-8'))
    resp = head.computeResponse()

    str_resp = str(resp, 'UTF-8')
    splitted = str_resp.split('\r\n\r\n')
    body_str = splitted[-1]
    print('splits: ', body_str)
    
    assert body_str == ret_value





