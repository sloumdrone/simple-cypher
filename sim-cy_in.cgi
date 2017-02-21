#!/usr/bin/env python

import string
import cgi, cgitb


def stringin (input1):
    """Allow for input input"""
    counter = 0

    """Create dictionary lookups"""
    chars = string.printable
    charlist = []
    dict02 = {}
    dict03 = {}

    for x in chars:
        charlist.append(x)

    for y, z in enumerate(charlist):
        dict02.update({y: z})
        dict03.update({y: z})

    dict01=dict((value,key) for key,value in dict02.iteritems())

    for key in dict02.iterkeys():
        if key < 100:
            dict02[key+100] = dict02.pop(key)
        else:
            break

    dict02.update(dict03)

    conversionstep1 = list(input1)
    conversionstep2 = []
    conversionstep3 = []
    conversionstep4 = []
    for x, y in enumerate(conversionstep1):
            conversionstep2.append(dict01[str(conversionstep1[x])])
    
    conversionstep3.append(conversionstep2[0])

    for x, y in enumerate(conversionstep2,1):
        try:
            counter = conversionstep2[x] + conversionstep2[(x - 1)]
            conversionstep3.append(counter)
        except IndexError:
            pass
        continue
    
    counter = 0
    for x, y in enumerate(conversionstep3):
            conversionstep4.append(dict02[conversionstep3[x]])
    return ''.join(conversionstep4)

form = cgi.FieldStorage()
text_content = stringin(str(form.getvalue('stuff')))
#text_content = form.getvalue('stuff')

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Simple Cypher - In</title>"
print "</head>"
print "<body>"
print "<h1>Simple Cypher - Encoded</h1><br>"
print "<p>Entered Text Content is:<br> %s</p>" % (text_content)
print "<br><br><hr>"
print '<a href="http://192.168.0.3:8000/www/encode.html">Encode</a> | <a href="http://192.168.0.3:8000/www/decode.html">Decode</a> | <a href="http://192.168.0.3:8000/www/index.html">Home</a>'
print "</body>"
print "</html>"
