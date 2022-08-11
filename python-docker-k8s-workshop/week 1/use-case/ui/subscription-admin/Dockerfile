# Build app

FROM node as build

WORKDIR /usr/local/app

COPY . /usr/local/app/

RUN npm install

RUN npm run build

# Deploy and lift app
FROM nginx:latest

COPY --from=build /usr/local/app/dist/subscription-admin /usr/share/nginx/html
COPY --from=build /usr/local/app/nginx.conf /etc/nginx/nginx.conf


EXPOSE 80

#docker build . -t workshop-ui    
#docker run -p 8006:80 workshop-ui