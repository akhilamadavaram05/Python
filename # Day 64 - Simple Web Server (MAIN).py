# Day 64 - Simple Web Server (MAIN)
import http.server
import socketserver
from pathlib import Path

HTML_FILE = Path("day64_index.html")
HTML_CONTENT = """
<!doctype html>
<html>
<head><title>Day 64</title></head>
<body>
<h1>🎉 Day 64 - Simple Web Server</h1>
<p>Served from day64_index.html</p>
</body>
</html>
"""

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ["/", "/index.html"]:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(HTML_CONTENT.encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

def main():
    HTML_FILE.write_text(HTML_CONTENT)
    print("Created day64_index.html")

    PORT = 8000
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print(f"Server running at http://localhost:{PORT}")
        print("Press Ctrl+C to stop")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("Server stopped")

if __name__ == "__main__":
    main()