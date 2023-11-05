# Use the specific Nginx image (version 1.24.0) as the base image
FROM nginx:1.24.0

# Remove the default Nginx configuration file
RUN rm /etc/nginx/nginx.conf

# Copy your custom Nginx configuration file to the container's Nginx configuration directory
COPY nginx.conf /etc/nginx/

# Remove the default configuration file for sites (if exists)
RUN rm /etc/nginx/conf.d/default.conf

# Copy your custom project configuration to the Nginx sites-available directory
COPY project.conf /etc/nginx/conf.d/
