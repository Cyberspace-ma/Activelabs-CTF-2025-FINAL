# Base image
FROM ubuntu:24.04

# Install dependencies
RUN apt-get update && apt-get install -y socat

# Create non-root user for security
RUN useradd -m pwn

# Copy binary and files
WORKDIR /home/scratch
COPY from_scratch /home/scratch 
COPY flag.txt /home/scratch 
RUN chmod +x /home/scratch/from_scratch

# Change ownership to chall user
RUN chown -R pwn:pwn /home/scratch

# Expose the correct port
EXPOSE 8002

# Run the challenge
USER pwn
CMD ["socat", "TCP-LISTEN:8002,reuseaddr,fork", "EXEC:./from_scratch,pty,stderr"]
