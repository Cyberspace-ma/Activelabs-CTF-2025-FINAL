# Base image
FROM ubuntu:24.04

# Install dependencies
RUN apt-get update && apt-get install -y socat python3 python3-venv

# Create a virtual environment
RUN python3 -m venv /opt/venv

# Activate the virtual environment and install pycryptodome
RUN /opt/venv/bin/pip install pycryptodome

# Create non-root user for security
RUN useradd -m crypto

# Copy binary and files
WORKDIR /home/madness
COPY chall.py /home/madness
COPY secret.py /home/madness
RUN chmod +x /home/madness/chall.py

# Change ownership to chall user
RUN chown -R crypto:crypto /home/madness/

# Expose the correct port
EXPOSE 9001

# Run the challenge using the virtual environment's Python interpreter
USER crypto
CMD ["socat", "TCP-LISTEN:9001,reuseaddr,fork", "EXEC:/opt/venv/bin/python3 /home/madness/chall.py,pty,stderr"]