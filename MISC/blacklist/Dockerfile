# Base image
FROM ubuntu:24.04

# Install dependencies
RUN apt-get update && apt-get install -y socat python3 figlet

# Create non-root user for security
RUN useradd -m misc

# Copy binary and files
WORKDIR /home/blacklist
COPY chall.py /home/blacklist
COPY flag.txt /home/blacklist

# Add execute permissions to the script
RUN chmod +x /home/blacklist/chall.py

# Change ownership to chall user
RUN chown -R misc:misc /home/blacklist/

# Expose the correct port
EXPOSE 3002

# Run the challenge
USER misc
CMD ["socat", "TCP-LISTEN:3002,reuseaddr,fork", "EXEC:python3 /home/blacklist/chall.py,pty,stderr"]