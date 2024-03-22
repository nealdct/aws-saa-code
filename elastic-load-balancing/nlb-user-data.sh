#!/bin/bash
# Update the system
yum update -y
# Install Python 3
yum install -y python3
# Create a simple Python web server script
cat > /home/ec2-user/webserver.py << EOF
import http.server
import socketserver

PORT = 8181
Handler = http.server.SimpleHTTPRequestHandler

class CustomHandler(Handler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes("Welcome to My Custom SaaS App", "utf8"))

httpd = socketserver.TCPServer(("", PORT), CustomHandler)
print("serving at port", PORT)
httpd.serve_forever()
EOF
# Run the web server in the background
nohup python3 /home/ec2-user/webserver.py > /dev/null 2>&1 &