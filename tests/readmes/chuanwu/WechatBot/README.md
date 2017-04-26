# WechatBot
[![Build Status](https://travis-ci.org/chuanwu/WechatBot.svg?branch=master)](https://travis-ci.org/chuanwu/WechatBot)
[![codecov](https://codecov.io/gh/chuanwu/WechatBot/branch/master/graph/badge.svg)](https://codecov.io/gh/chuanwu/WechatBot)
[![PyPI version](https://badge.fury.io/py/wechatbot.svg)](https://badge.fury.io/py/wechatbot)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


*WechatBot* is a wechat bot built for geeks.

### Quick Start

#### 0. 支持pip安装


    pip install wechatbot

已支持pip安装，但是文档还没有更新，请等待更新。

#### 1. 安装依赖并执行测试脚本


   ```
   make test
   ```

#### 2. 启动WechatBot


   ```
   make mybot
   ```

   扫描二维码之后，机器人就跑起来啦。
   这时，可以向机器人发送一个!ping的消息来看看服务是否正常。

   ![Ping](https://ooo.0o0.ooo/2017/03/29/58db399dd2ca6.jpeg)

#### 3. 功能开发

将你所实现的程序放到plugin/目录下，并使用该装饰器即可。

   ```
   from wechatbot import r
   @r.register('COMMAND_STRING')
   ```

具体细节请看`plugin/ping_demo.py`。

## 规划

接下来会把Bot做成一个更加基础的服务，只对外暴露两个模块:

1. 在接受指令之后发送定制消息

   后续会增加session的概念，可能会支持AI，并通过向机器人发送消息来开关AI。

   来自用户的每一条消息都是作为一个命令。


2. 主动向某个用户发送消息


### Docs

For more details, you may like [reading the docs](http://tinker.readthedocs.io/).


In the end, thanks to [@elezhangwen](https://github.com/elezhangwen).
