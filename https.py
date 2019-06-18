import sys
import http.server, ssl

host = 'localhost'

for x in sys.argv:
  item = x.split('=')
  if (item[0] == 'ip'):
    host = item[1]

server_address = (host, 4443)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket,
                               keyfile="~/Documents/python-https-server/key.pem",
                               certfile="~/Documents/python-https-server/server.pem",
                               server_side=True,
                               ssl_version=ssl.PROTOCOL_TLSv1)
httpd.serve_forever()
