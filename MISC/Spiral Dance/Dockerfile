# Base image
FROM ubuntu:24.04

# Install dependencies
RUN apt-get update && apt-get install -y socat dos2unix python3

# Create non-root user for security
RUN useradd -m misc

# Copy binary and files
WORKDIR /home/spiraldance
COPY chall.py /home/spiraldance

# Convert line endings to Unix-style
RUN dos2unix /home/spiraldance/chall.py

RUN chmod +x /home/spiraldance/chall.py

# Change ownership to chall user
RUN chown -R misc:misc /home/spiraldance

# Expose the correct port
EXPOSE 3003

# Run the challenge
USER misc
CMD ["socat", "TCP-LISTEN:3003,reuseaddr,fork", "EXEC:/home/spiraldance/chall.py,pty,stderr"]