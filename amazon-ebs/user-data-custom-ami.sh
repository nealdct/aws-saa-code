#!/bin/bash

# Update the system and install Apache web server
yum update -y
yum install -y httpd

# Start and enable Apache to run on boot
systemctl start httpd
systemctl enable httpd

# Create an index.html file with CSS animations for background color changing
cat > /var/www/html/index.html <<'EOF'
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Custom AMI Instance</title>
    <style>
        @keyframes backgroundChange {
            0% { background-color: #6495ED; }
            50% { background-color: #ADD8E6; }
            100% { background-color: #6495ED; }
        }

        body {
            color: white;
            font-size: 48px;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            animation: backgroundChange 4s infinite;
        }
    </style>
</head>
<body>
    <div>This Instance Was Launched from a Custom AMI</div>
</body>
</html>
EOF

# Ensure the httpd service is correctly set up to start on boot
chkconfig httpd on
