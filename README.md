# CloudGeetest

B站验证码云通过部署

基于bili_ticket_gt_python库，只是做了个上云功能

> 什么你问我怎么用？ 直接运行喵！

> 仅支持Windows环境，跑不了就是你Windows版本太老了or缺库！

> 在python中，request库初始化需要>300ms，建议复用session并在调用前提前建立连接

| 特性   | 支持 |
|------|----|
| 高并发  | √  |
| 云部署  | √  |
| 身份校验 | X  |

## 调用方式
参考Python
```
def passGeetest(geetest, challenge):
    session = requests.Session()
    url = "http://" + BasicInfo.config["GeetestAddress"] + "?gt=" + geetest + "&c=" + challenge
    try:
        data = session.get(url=url, timeout=10).json()
    except Exception:
        return passGeetest(geetest, challenge)
    return data
```

## 连接测试
参考Python
```
def checkCloudGeetest(address):
    session = requests.Session()
    url = "http://" + address + "?gt=test&c=test"
    try:
        data = session.get(url=url, timeout=(9.05, 15.05)).json()
        BasicVoid.sendInfo("测试成功！数据：" + str(data))
        return True
    except Exception as e:
        print(e)
    return False
```