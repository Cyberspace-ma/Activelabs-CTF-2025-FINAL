# Base image
FROM ubuntu:24.04

# Install dependencies
RUN apt-get update && apt-get install -y socat

# Create non-root user for security
RUN useradd -m pwn

# Copy binary and files
WORKDIR /home/rocket
COPY spaceship /home/rocket
COPY flag.txt /home/rocket
RUN chmod +x /home/rocket/spaceship

# Change ownership to chall user
RUN chown -R pwn:pwn /home/rocket/

# Expose the correct port
EXPOSE 8001

# Run the challenge
USER pwn
CMD ["socat", "TCP-LISTEN:8001,reuseaddr,fork", "EXEC:/home/rocket/spaceship,pty,stderr"]

