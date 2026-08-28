import http.server, os, socketserver
os.chdir(os.path.dirname(os.path.abspath(__file__)))
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("127.0.0.1", 4322), http.server.SimpleHTTPRequestHandler) as h:
    print("serving", os.getcwd(), "on 4322", flush=True)
    h.serve_forever()
