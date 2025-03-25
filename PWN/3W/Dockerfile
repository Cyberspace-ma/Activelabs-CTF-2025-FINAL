# Base image
FROM ubuntu:24.04

# Install dependencies
RUN apt-get update && apt-get install -y socat

# Create non-root user for security
RUN useradd -m pwn

# Copy binary and files
WORKDIR /home/3w
COPY write /home/3w
COPY flag.txt /home/3w
RUN chmod +x /home/3w/write

# Change ownership to chall user
RUN chown -R pwn:pwn /home/3w/

# Expose the correct port
EXPOSE 8003

# Run the challenge
USER pwn
CMD ["socat", "TCP-LISTEN:8003,reuseaddr,fork", "EXEC:/home/3w/write,pty,stderr"]

