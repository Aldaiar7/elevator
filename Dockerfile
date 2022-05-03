FROM python:3
ADD modules.py /
ADD main.py /
WORKDIR  /app
COPY main.py ./
COPY modules.py ./
CMD ["python", "main.py"]
