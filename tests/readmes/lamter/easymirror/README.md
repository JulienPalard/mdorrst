# easymirror
进行时间序列数据库的索引同步

## 说明
1. `easymirror`使用Redis作为消息转发。
2. 本地使用`easymirror`的`mirror.Mirror`做基类，进一步开发供各种数据录入程序的接口。参考`easymirror.vnpy.py`文件。
3. 多个相同的行情录入程序可以在盘中(未实现)、盘后对齐缺失的 ticker 数据。

## 环境
将仓库`clone`到本地后，运行以下命令安装：
```bash
pip install -e .
```
### 配置文件
主要的配置文件是`conf/conf.json`。

### Redis
1. 这里`Redis`使用的端口是23002，对应的`Redis`配置文件是`23002.conf`。
2. 基本上只需要简单地配置一下端口号和异地访问密码即可。
3. 生产环境下，在公网部署部署该`

## 使用
1. 实盘中对齐
2. 盘后对齐
3. 二次开发

### 1. 实盘中对齐（未实现）
1. demo见`debug.py`文件。
2. 在子进程中建立服务后，通过`api.pushTickerIndex`接口推入Ticker数据。
3. 代码基于`python3.5`的协程来实现。如果实盘数据录入不是`python3.5`以上，那么只能使用`盘后对齐`的功能

### 2. 盘后对齐
1. demo见`makeup.py`文件。
2. 先从数据库中加载 ticker 数据，并缓存。
3. 开始广播前，所有在线的节点都需要在本地做好缓存。
4. 通过调用`api.pushTickerIndex`接口开始广播。
5. 使用的`python3.5`的协程来实现并发。

### 3. 二次开发
参考`easymirror.vnpy.py`，通过继承`easymirro.mirror.Mirror`来重写部分接口。

