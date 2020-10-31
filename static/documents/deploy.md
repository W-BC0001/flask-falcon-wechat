# 部署步骤

#### 安装 virtualenv==16.7.9, 这个版本不会报错`--no-site-packages无效`
```
pip install --upgrade virtualenv==16.7.9 -i https://pypi.doubanio.com/simple/ --disable-pip-version-check
```

#### 部署虚拟环境, 安装python包
```
virtualenv --no-site-packages venv

source venv/bin/activate

pip install -r requirements.txt -i https://pypi.doubanio.com/simple/ --disable-pip-version-check
```

#### 修改企业微信信息
新建 overrides.py 文件, 和 settings.py 在同一级目录 
```
vim overrides.py 
```

写入如下内容, 并根据实际情况进行替换: 
```
DEBUG = True

WECHAT_URL = 'https://qyapi.weixin.qq.com'
WECHAT_CORPID = 'your corpid, type: string'
WECHAT_CORPSECRET = 'your secret, type: string'
WECHAT_AGENT_ID = 'your agent id, type: int'

HOST = '127.0.0.1' 
PORT = '2333'
```

#### 设置命令别名快速进入项目目录并加载 python 虚拟环境
```
echo -e '\nalias flask-falcon-wechat="cd /opt/flask-falcon-wechat/flask-falcon-wechat && source venv/bin/activate"' | tee -a ~/.bash_profile

source ~/.bash_profile

flask-falcon-wechat
```

#### 配置定时任务, 每两小时调用一次`/v1/token/`接口, 获取(刷新)token  

> 接口地址一定要加上最后的/ 

```
0 */2 * * * /usr/bin/curl -s -i http://127.0.0.1:2333/v1/token/
```

#### 启动服务, 监听`http://127.0.0.1:2333`端口
```
$ ./server start
```