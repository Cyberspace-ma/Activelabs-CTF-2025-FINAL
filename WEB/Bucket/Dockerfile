FROM python:3.11

WORKDIR /bucket

# Copy requirements first (optimization for caching)
COPY requirements.txt /bucket/
RUN pip install -r requirements.txt

# Then copy everything else
COPY . /bucket

EXPOSE 5301

CMD ["python", "app.py"]