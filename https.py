import os
import sys
import http.server, ssl

#userPath =  os.path.expanduser("~/Documents/python-https-server")
userPath = os.path.dirname(os.path.realpath(__file__))
host = '10.116.105.93'
port = 4443

keyFile = userPath + "/key.pem"
certFile = userPath + "/server.pem"

for x in sys.argv:
  item = x.split('=')
  if (item[0] == 'ip'):
    host = item[1]

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map['.wasm'] = 'application/wasm'
server_address = (host, port)

httpd = http.server.HTTPServer(server_address, Handler)
httpd.socket = ssl.wrap_socket(httpd.socket,
                               keyfile=keyFile,
                               certfile=certFile,
                               server_side=True,
                               ssl_version=ssl.PROTOCOL_TLSv1)
print('server ' + host + ' running at port ' + str(port))
httpd.serve_forever()
