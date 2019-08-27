FROM python:3.7.4-alpine
WORKDIR /code
ENV PYTHONPATH=/code/:$PYTHONPATH

RUN apk --no-cache add ffmpeg

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

COPY mediascan ./

VOLUME /data
ENTRYPOINT ["python3", "-m", "mediascan"]