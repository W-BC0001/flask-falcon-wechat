# -*- coding: utf-8 -*-

import sys
import json
import requests
from settings import BASE_DIR
from settings import (
    WECHAT_AGENT_ID,
    WECHAT_SEND_MESSAGE_URL,
    WECHAT_TOKEN_URL,
    logger
)


def get_wechat_token():
    response = requests.get(WECHAT_TOKEN_URL)

    if response.json()['errcode'] == 0:
        token = response.json()['access_token']

        try:
            file = open('{}/token.txt'.format(BASE_DIR), 'w')
            file.write(token)
            file.close()
        except Exception as e:
            raise Exception(e)

        message = {
            'status': True,
            'msg': 'Get token successfully'
        }
        logger.info(message)
    else:
        message = {
            'status': False,
            'msg': 'Get token failed; Error code: {errcode}, Error msg: {errmsg}'.format(
                **response.json()
            )
        }
        logger.error(message)

    return message


def get_url():
    reload(sys)
    sys.setdefaultencoding('utf8')

    file = open('{}/token.txt'.format(BASE_DIR))
    token = file.read()
    file.close()
    url = '{}{}'.format(WECHAT_SEND_MESSAGE_URL, token)

    return url


def parse_message(content):
    reload(sys)
    sys.setdefaultencoding('utf8')

    list_content = content.replace('][', ' ').replace('[', '').replace(']', '').split(' ')
    logger.info('open-falcon post data: {}'.format(list_content))
    logger.info('open-falcon post data type: {}'.format(type(list_content)))

    text = [
        "** 触发规则: ** {alarm_rule}",
        "** 报警级别: ** {alarm_level}",
        "** 报警信息: ** {alarm_note}",
        "** 报警次数: ** {alarm_count}",
        "** 当前的值: ** {alarm_value}",
        "** 报警日期: ** {alarm_date}",
        "** 报警时间: ** {alarm_time}",
    ]

    alarm_body = {}
    alarm_body['alarm_level'] = list_content[0]

    if len(list_content[2]) > 2:
        alarm_body['alarm_host'] = list_content[2]
        alarm_body['alarm_note'] = list_content[4]
        alarm_body['alarm_count'] = list_content[5]
        alarm_body['alarm_rule'] = list_content[6]
        alarm_body['alarm_value'] = list_content[8]
        alarm_body['alarm_date'] = list_content[10]
        alarm_body['alarm_time'] = list_content[11]
    else:
        text = [
            "** 报警级别: ** {alarm_level}",
            "** 报警信息: ** {alarm_note}",
        ]

        alarm_body['alarm_host'] = '报警信息不规范'
        alarm_body['alarm_note'] = map(str, list_content[2:])

    if list_content[1] == u'OK':
        text.insert(0, "** <font color =\"info\">恢复 {alarm_host}</font> **")
    elif list_content[1] == u'PROBLEM':
        text.insert(0, "** <font color =\"warning\">故障 {alarm_host}</font> **")

    logger.info('alarm_body: {}'.format(alarm_body))

    message = '\n'.join(text)
    logger.info(message)
    markdown_message = message.format(**alarm_body)

    logger.info('markdown_message: {}'.format(markdown_message))

    return markdown_message


def send_message(user, message):
    """
    参考文档:
    https://work.weixin.qq.com/api/doc/90000/90135/90236#markdown%E6%B6%88%E6%81%AF
    """
    try:
        url = get_url()
    except IOError:
        logger.info('token.txt does not exist, try to get token.txt...')
        get_wechat_token()
        url = get_url()

    data = {
        "touser": user,
        "msgtype": "markdown",
        "agentid": WECHAT_AGENT_ID,
        "toall": 0,
        "markdown": {
            "content": message
        },
        "enable_duplicate_check": 0,
    }

    logger.info('wechat markdown content: {}'.format(data))

    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(data), headers=headers)

    result = {}
    if response.json()['errcode'] == 0:
        result['status'] = True
        result['message'] = 'Message received successfully, over'
    else:
        result['status'] = False
        result['message'] = 'Message received failed! Errmsg: {}'.format(
            response.json()
        )

    return result
