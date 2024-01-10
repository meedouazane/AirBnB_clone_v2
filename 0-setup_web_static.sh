#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir /data/web_static/shared/
echo "Hello World! this is from Airbnb" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sfT /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo apt-get update
sudo apt-get install nginx -y
sudo sed -i '/server_name _;/a \ \n    location \/hbnb_static {\n        alias \/data\/web_static\/current;\n    }' /etc/nginx/sites-available/default
sudo service nginx restart
