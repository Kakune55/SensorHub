FROM python:3.12.6-alpine3.20
WORKDIR /app
COPY . /app
RUN python3 -m pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
CMD ["python3", "main.py"]
EXPOSE 8000