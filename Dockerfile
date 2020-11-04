FROM python:3
# We can move compiled libraries into new docker image and use python:3-slim for example.
# This will reduce the size

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Prepare uWSGI
RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi

WORKDIR /app
COPY cmd.sh /

EXPOSE 9090 9191
USER uwsgi

CMD ["/cmd.sh"]
