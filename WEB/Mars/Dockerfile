FROM node:12.13.0-alpine

# Install packages
RUN apk --no-cache add supervisor

# Setup app
RUN mkdir -p /app
WORKDIR /app

# Add application
COPY --chown=nobody challenge .

# Setup supervisor
COPY config/supervisord.conf /etc/supervisord.conf

RUN yarn

# Expose the correct port
EXPOSE 5005

# Copy entrypoint
COPY entrypoint.sh /entrypoint.sh

# Start the application
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
