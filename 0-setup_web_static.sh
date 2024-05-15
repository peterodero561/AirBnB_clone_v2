#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null
then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Set ownership recursively
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sudo sed -i "/server_name _;/a \ \n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default

# Restart Nginx
sudo systemctl restart nginx
exit_status=$?
if [ $exit_status -eq 0 ]; then
    echo "Command executed successfully."
else
    echo "Command failed with exit status $exit_status."
fi
