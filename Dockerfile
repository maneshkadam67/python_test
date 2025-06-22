FROM selenium/standalone-chrome:latest

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY test_selenium_python.py .

CMD ["pytest", "test_selenium_python.py"]

#docker build --platform linux/amd64 -t selenium .