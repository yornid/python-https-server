FROM ubuntu:18.04

ARG wd

RUN apt-get update && apt-get install -y \
    python3

WORKDIR $wd

CMD ["python3", "./https.py"]
