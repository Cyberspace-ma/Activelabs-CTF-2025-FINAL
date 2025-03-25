# Use an official Python image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /panel

# Copy dependency files first to leverage Docker caching
COPY requirements.txt /panel/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . /panel

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
