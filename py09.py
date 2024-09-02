import http.server
import socketserver

PORT = 8000
DIRECTORY = "/mnt/data/solar_system_explorer"

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

# HTTP serverni ishga tushiramiz
with socketserver.TCPServer(("", PORT), MyHttpRequestHandler) as httpd:
    print(f"Server running at http://localhost:{PORT}")
    httpd.serve_forever()
