FROM python:3-alpine

WORKDIR /usr/src/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app app
WORKDIR /usr/src/app

ARG GITLAB_TOKEN
RUN sed --in-place --expression="s/<GITLAB_TOKEN>/${GITLAB_TOKEN}/" python-gitlab.cfg

CMD ["python", "main.py" ]


