FROM python:2.7.16-alpine

MAINTAINER <wbc>

COPY . /opt/flask-falcon-wechat/

WORKDIR /opt/flask-falcon-wechat/flask-falcon-wechat

RUN set -ex; \
    pip config set global.index-url https://pypi.doubanio.com/simple/; \
    pip install --upgrade virtualenv==16.7.9 --disable-pip-version-check; \
    virtualenv --no-site-packages venv; \
    source venv/bin/activate; \
    pip install -r requirements.txt --disable-pip-version-check

EXPOSE 2333/tcp

CMD ["./venv/bin/python", "app.py"]
