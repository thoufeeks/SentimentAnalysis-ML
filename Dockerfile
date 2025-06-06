FROM python:3.9-slim
WORKDIR /app
COPY app/ .
RUN pip install -r requirements.txt
RUN python train.py
EXPOSE 5000
CMD ["python", "inference.py"]
