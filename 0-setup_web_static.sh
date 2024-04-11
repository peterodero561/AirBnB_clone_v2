#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create necessary directories
sudo mkdir -p /data/web_static/{releases/test,shared}
sudo mkdir -p /data/web_static/current

# Create fake HTML file
echo "Fake HTML content" | sudo tee /data/web_static/releases/test/index.html >/dev/null

# Create symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Set ownership recursively
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sudo tee /etc/nginx/sites-available/default <<EOF
server {
    listen 80;
    server_name _;

    location /hbnb_static {
        alias /data/web_static/current/;
    }
}
EOF

# Enable the site
sudo ln -sf /etc/nginx/sites-available/web_static /etc/nginx/sites-enabled/

# Restart Nginx
sudo systemctl restart nginx
