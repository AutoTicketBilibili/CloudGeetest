# CloudGeetest

B站验证码云通过部署

基于bili_ticket_gt_python库，只是做了个上云功能

> 什么你问我怎么用？ 直接运行喵！

> 仅支持Windows环境，跑不了就是你Windows版本太老了or缺库！

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