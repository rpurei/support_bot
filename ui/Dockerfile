FROM node:18.10-bullseye
RUN apt update && DEBIAN_FRONTEND=noninteractive apt --no-install-recommends install -y nginx
COPY chatbot.conf /etc/nginx/sites-available
RUN ln -sf /etc/nginx/sites-available/chatbot.conf /etc/nginx/sites-enabled && rm -rf /etc/nginx/sites-enabled/default
WORKDIR /var/www/chatbot/ui
COPY ./package.json ./package-lock.json /var/www/chatbot/ui/
RUN npm config set strict-ssl false && npm config set registry http://registry.npmjs.org/ ## !!!!!!!
RUN npm install -g @angular/cli && npm install
COPY . .
RUN ng build
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
