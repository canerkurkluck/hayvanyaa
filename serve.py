import os, http.server, socketserver
os.chdir('/Users/i535645/Desktop/hayvanya-temp')
PORT = 7788
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
