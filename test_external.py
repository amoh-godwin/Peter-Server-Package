# -*- coding: utf-8 -*-
import pytest
from headers import Header
from settings import Sets

sets = Sets()
head = Header(sets.parent_folder, sets.addr)

@pytest.mark.parametrize('req', [('get=love'),
                                 ('get=777&post=sure')])
def test_php_get_req(req):
    if '&' in req:
        main_splits = req.split('&')
    else:
        main_splits = [req]
    string = 'array(' + str(len(main_splits)) + ')' + ' {\n'
    for requ in main_splits:
        splits = requ.split('=')
        string += '  ["' + splits[0] + '"]=>\n  string(' + str(len(splits[1])) + ') "' + splits[1] + '"\n'
    string += '}\n'
    ret_value = string

    req_string = 'GET /_tests/phpGetReq.php?' + req + ' HTTP/1.1'

    head.getRequest(bytes(req_string, 'utf-8'))
    resp = head.computeResponse()

    str_resp = str(resp, 'UTF-8')
    splitted = str_resp.split('\r\n\r\n')
    body_str = splitted[-1]
    
    assert body_str == ret_value
