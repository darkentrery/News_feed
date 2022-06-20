#FROM nginx:1.21-alpine
#
#RUN rm /etc/nginx/conf.d/default.conf
#COPY nginx.conf /etc/nginx/conf.d

#COPY ../news_site/feed/static/ ./news_site/feed/


#FROM nginx:stable-alpine
#COPY --from=build /app/frontend/build /usr/share/nginx/html
#CMD ["nginx", "-g", "daemon off;"]
FROM nginx:1.21-alpine
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
#COPY /react_front/build /usr/share/nginx/html