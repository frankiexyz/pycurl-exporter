#!/usr/bin/env python

import pycurl
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import cStringIO
import urllib
import StringIO
import threading
from io import BytesIO
import re



def fetch(url):
    buffer = BytesIO()
    c = pycurl.Curl()
    header_function = cStringIO.StringIO()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(c.USERAGENT, 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)')
    c.setopt(c.HEADERFUNCTION, header_function.write)
    c.perform()
    body = buffer.getvalue()
    header = header_function.getvalue()
    CACHEHIT = False
    for i in header.split():
        if re.search("HIT", i):
            CACHEHIT = True
    output = "NAMELOOKUP_TIME {}\n".format(c.getinfo(c.NAMELOOKUP_TIME))
    output = output + ("CONNECT_TIME {}\n".format(c.getinfo(c.CONNECT_TIME)))
    output = output + ("STATUS_CODE {}\n".format(c.getinfo(c.HTTP_CODE)))
    output = output + ("PRETRANSFER_TIME {}\n".format(c.getinfo(c.PRETRANSFER_TIME)))
    output = output + ("REDIRECT_TIME {}\n".format(c.getinfo(c.REDIRECT_TIME)))
    output = output + ("STARTTRANSFER_TIME {}\n".format(c.getinfo(c.STARTTRANSFER_TIME)))
    output = output + ("TOTAL_TIME {}\n".format(c.getinfo(c.TOTAL_TIME)))
    if CFRAY:
        output = output + ('CF_HIT 1\n')
    else:
        output = output + ('CF_HIT 0\n')
    return output
    c.close()


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

class GetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = urllib.unquote(self.path.split('=')[1])
        print url
        message = fetch(url)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(message)
        return

if __name__ == '__main__':
    server = ThreadedHTTPServer(('0.0.0.0', 9095), GetHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
