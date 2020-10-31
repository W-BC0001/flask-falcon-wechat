# flask-falcon-wechat 接口列表 & 使用介绍

> 一定要加上后面的 / 路径

- /v1/token/  
- /v1/send/  

## 功能介绍

### /v1/token/  

> 用于获取企业微信token认证

- 请求方式  
  GET, 无须携带任何参数或者头部
  
- URI格式  
  http://127.0.0.1:2333/v1/token/

- 正常返回示例
  ```
  {"status": True, "msg": "token获取成功"}
  ```

- 错误返回示例
  ```
  {"status": False, "msg": "token获取失败; 错误代码: {errcode}, 错误信息: {errmsg}"}
  ```

- status_code  
  ```
  200
  ```

### /v1/send/
> 用于发送消息至对方企业微信

- 请求方式  
  POST
  
- URI格式  
  http://127.0.0.1:2333/v1/send/

- 请求消息  

参数 | 是否必选 | 参数类型 | 描述
- | - | - | -
content | 是 | array/list | 报警内容
tos | 是 | string | 接收报警人, 多个人用&#124;号分隔  

- 正常返回示例
  ```
  {"status": True, "msg": "Message received successfully, over"}
  ```

- 错误返回示例
  ```
  {"status": False, "msg": "Message received failed! {response.json()}"}
  ```

- status_code  
  ```
  201
  ```

- 测试命令
  ```
  curl -d "content=[P5, PROBLEM, test-host, , 客户端连接数连接大于160，请检查程序是否有异常, all(#1), test-rule, tag=redis, 161>160, O1, 2020-08-15, 11:51:00]&tos=test-user" "http://127.0.0.1:2333/v1/send/"
  ```