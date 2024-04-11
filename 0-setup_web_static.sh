#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

# install Nginx
sudo apt-get update
sudo apt-get install -y nginx

# create the folders
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/current/
echo "Holberton School" > /data/web_static/releases/test/index.html

# create symbolic link
if [ -d "/data/web_static/releases/test/" ]; then
  sudo ln -sf /data/web_static/releases/test /data/web_static/current/
 else
	 exit 1
fi

# owerniship to ubuntu
sudo chown -R ubuntu:ubuntu /data/

# updata nginx conf
sudo tee /etc/nginx/sites-available/web_static <<EOF
server {
  listen 80;
  server_name _;
  location /hbnb_static {
    alias /data/web_static/current/;
  }
}
EOF

# Create symbolic link to enable the site
sudo ln -sf /etc/nginx/sites-available/web_static /etc/nginx/sites-enabled/

# update
sudo systemctl restart nginx
