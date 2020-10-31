# docker-compose 部署步骤

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

# docker 容器部署 HOST 建议设置为 0.0.0.0
HOST = '0.0.0.0' 
PORT = '2333'
```

#### 使用docker-compose打包镜像并部署, 默认监听宿主机`2333`端口
> 打包出来的镜像名称: flask-falcon-wechat_flask-falcon-wechat:latest  
> docker-compose启动的容器名称: flask-falcon-wechat  

```
docker-compose up -d
```

#### 宿主机配置定时任务, 每两小时调用一次`/v1/token/`接口, 获取(刷新)token  

> 接口地址一定要加上最后的/  

```
0 */2 * * * /usr/bin/curl -s -i http://127.0.0.1:2333/v1/token/
```

#### 如需更新`overrides.py`配置, 直接在宿主机本地更改, 然后restart容器即可