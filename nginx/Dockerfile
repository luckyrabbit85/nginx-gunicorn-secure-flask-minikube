# Use the specific Nginx image (version 1.24.0) as the base image
FROM nginx:stable-bullseye

# Remove the default configuration file for sites (if exists)
RUN rm /etc/nginx/conf.d/default.conf

# Copy your custom project configuration to the Nginx sites-available directory
COPY ssl-proxy.conf /etc/nginx/conf.d/
