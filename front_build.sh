#!/bin/bash
cd /var/www/chatbot/material
npm install
ng build
cd ..
chown -R www-data:www-data /var/www/chatbot
systemctl restart nginx
