FROM python:3.11

RUN apt-get update && apt-get install -y ffmpeg

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "./main.py"]