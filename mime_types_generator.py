# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re
from kk import dd

#ff = "C:/Users/Ampofo/Downloads/Media Types.html"

"""ddd = "<tr>
          <td>set-registration-initiation</td>
          <td>
            <a href="https://www.iana.org/assignments/media-types/application/set-registration-initiation">application/set-registration-initiation</a>
          </td>
          <td>[<a href="#Brian_Korver">Brian_Korver</a>]</td>
        </tr>"""

"""with open(ff, mode='r', encoding='utf-8') as html_file:
    data = html_file.read()

founds = re.findall('<tr>\n[\s]+<td>.*?.*?.*?</td>', data)
fix = []
for each in founds:
    fix.append(each.split('<td>')[1].split('</td>')[0])

print(fix)"""



f_ind = dd.index('3gpdash-qoe-report+xml')

als = dd[f_ind:]
left_alone = dd[:f_ind]
#print(left_alone)
print(als)
