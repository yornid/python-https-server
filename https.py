import os
import sys
import signal
import http.server, ssl

def stopHandler(sig, frame):
  print("\nYou have stopped the python http server.")
  sys.exit(0)

host = 'localhost'
port = None
#userPath =  os.path.expanduser("~/Documents/python-https-server")
userPath = os.path.dirname(os.path.realpath(__file__))
keyFile = userPath + "/key.pem"
certFile = userPath + "/server.pem"
isHttps = True

for x in sys.argv:
  item = x.split('=')
  if item[0] == '-s':
    isHttps = False 
  elif item[0] == 'ip':
    host = item[1]
  elif item[0] == 'port':
    port = int(item[1])

if port is None:
  if isHttps:
    port = 4443
  else:
    port = 8080

signal.signal(signal.SIGINT, stopHandler)

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map['.wasm'] = 'application/wasm'
server_address = (host, port)
httpd = http.server.HTTPServer(server_address, Handler)

if isHttps == True:
  httpd.socket = ssl.wrap_socket(httpd.socket,
                                 keyfile=keyFile,
                                 certfile=certFile,
                                 server_side=True,
                                 ssl_version=ssl.PROTOCOL_TLSv1)
print('server ' + host + ' running at port ' + str(port))
httpd.serve_forever()
