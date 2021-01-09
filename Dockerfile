FROM alpine

RUN adduser -D -u 1000 app \
    && mkdir /app \
    && chown app:app /app

WORKDIR /app
COPY --chown=app:app . .

RUN apk add --no-cache \
    python3 \
    uwsgi-python \
    py3-flask \
    py3-pip \
    && pip install -r requirements.txt

USER app

EXPOSE 8080
CMD ["/usr/sbin/uwsgi",               \
     "--master",                      \
     "--http-socket", "0.0.0.0:8080", \
     "--uid",         "uwsgi",        \
     "--plugins",     "python",       \
     "--wsgi",        "app:app"]
