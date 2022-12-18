FROM python:3.9

WORKDIR /app
ADD . /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Port Forwarding
EXPOSE 80

CMD ["python", "app.py"]
