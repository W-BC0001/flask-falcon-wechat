# -*- coding: utf-8 -*-

import sys
from flask import Flask, request
from settings import logger
from utils import (
    parse_message,
    send_message,
    get_wechat_token
)
from settings import HOST, PORT, DEBUG

app = Flask(__name__)


@app.route('/v1/token/', methods=['GET'])
def get_token():
    reload(sys)
    sys.setdefaultencoding('utf8')

    response = get_wechat_token()

    return response, 200


@app.route('/v1/send/', methods=['GET', 'POST'])
def main():
    reload(sys)
    sys.setdefaultencoding('utf8')

    if request.method == 'GET':
        return '<h1>Hello, this is flask falcon wechat ~<h1>', 200
    elif request.method == 'POST':
        content = request.form.get('content')
        logger.info('Receive content: {}'.format(content))

        user = request.form.get('tos').replace(',', '|')
        logger.info('Receive user: {}'.format(user))

        message = parse_message(content=content)
        logger.info('parse_message: {}'.format(message))

        send_result = send_message(user=user, message=message)
        logger.info('send_result: {}'.format(send_result))

        return send_result, 201


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')

    app.run(host=HOST, port=PORT, debug=DEBUG)
