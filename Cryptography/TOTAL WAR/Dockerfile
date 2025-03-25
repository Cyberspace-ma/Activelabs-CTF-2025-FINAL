# Base image
FROM ubuntu:24.04

# Install dependencies
RUN apt-get update && apt-get install -y socat python3 python3-venv

# Create a virtual environment and install pycryptodome
RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/pip install pycryptodome

# Create non-root user for security
RUN useradd -m crypto

# Copy binary and files
WORKDIR /home/totalwar
COPY chall.py /home/totalwar
COPY flag.txt /home/totalwar
RUN chmod +x /home/totalwar/chall.py

# Change ownership to chall user
RUN chown -R crypto:crypto /home/totalwar/

# Expose the correct port
EXPOSE 9002

# Run the challenge using the virtual environment
USER crypto
CMD ["socat", "TCP-LISTEN:9002,reuseaddr,fork", "EXEC:/opt/venv/bin/python3 /home/totalwar/chall.py,pty,stderr"]