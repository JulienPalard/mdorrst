=======
RQAlpha
=======

..  image:: https://raw.githubusercontent.com/ricequant/rqalpha/master/docs/source/_static/logo.jpg

..  image:: https://img.shields.io/travis/ricequant/rqalpha/master.svg
    :target: https://travis-ci.org/ricequant/rqalpha/branches
    :alt: Build

..  image:: https://coveralls.io/repos/github/ricequant/rqalpha/badge.svg?branch=master
    :target: https://coveralls.io/github/ricequant/rqalpha?branch=master

..  image:: https://readthedocs.org/projects/rqalpha/badge/?version=stable
    :target: http://rqalpha.readthedocs.io/zh_CN/stable/?badge=stable
    :alt: Documentation Status

..  image:: https://img.shields.io/pypi/v/rqalpha.svg
    :target: https://pypi.python.org/pypi/rqalpha
    :alt: PyPI Version

..  image:: https://img.shields.io/pypi/l/rqalpha.svg
    :target: https://opensource.org/licenses/Apache-2.0
    :alt: License

..  image:: https://img.shields.io/pypi/pyversions/rqalpha.svg
    :target: https://pypi.python.org/pypi/rqalpha
    :alt: Python Version Support


RQAlpha 从数据获取、算法交易、回测引擎，实盘模拟，实盘交易到数据分析，为程序化交易者提供了全套解决方案。RQAlpha 具有灵活的配置方式，强大的扩展性，用户可以非常容易地定制专属于自己的程序化交易系统。

RQAlpha 所有的策略都可以直接在 `Ricequant`_ 上进行回测和实盘模拟，并且可以通过微信和邮件实时推送您的交易信号。

`Ricequant`_ 是一个开放的量化算法交易社区，为程序化交易者提供免费的回测和实盘模拟环境，并且会不间断举行实盘资金投入的量化比赛。

特点
============================

*   易于使用: RQAlpha让您集中于策略的开发，一行简单的命令就可以执行您的策略。
*   完善的文档: 您可以直接访问 `RQAlpha 文档`_ 或者 `Ricequant 文档`_ 来获取您需要的信息。
*   活跃的社区: 您可以通过访问 `Ricequant 社区`_ 获取和询问有关 RQAlpha 的一切问题，有很多优秀的童鞋会解答您的问题。
*   稳定的环境: 每天都有会大量的算法交易在 Ricequant 上运行，无论是 RQAlpha，还是数据，我们能会做到问题秒处理，秒解决。
*   灵活的配置: RQAlpha 提供了一系列的配置选项，用户可以通过简单的配置来构建适合自己的交易系统。
*   强大的扩展性: RQAlpha 定义了一系列的 Mod Hook 接口，开发者可以基于 Mod 的开发模式，扩展 RQAlpha，无论是做实时监控，还是归因分析，RQAlpha 都可以通过扩展来实现。

快速指引
============================

*   `RQAlpha 介绍`_
*   `安装指南`_
*   `10分钟学会 RQAlpha`_
*   `策略示例`_

RQAlpha API
============================

*   `参数配置`_ : 启动 RQAlpha 参数配置
*   `API`_ : RQAlpha API 文档

Mod
============================

RQAlpha 提供了极具拓展性的 Mod Hook 接口，这意味着 RQAlpha 可以非常容易的对接其他量化库，安装和使用 Mod 也非常简单，当您安装好 RQAlpha 后，可以直接通过如下命令对管理您的Mod:

..  code-block:: bash
    
    # 查看当前安装的 Mod 列表及状态
    $ rqalpha mod list
    # 安装 Mod
    $ rqalpha mod install xxx
    # 卸载 Mod
    $ rqalpha mod uninstall xxx
    # 启用 Mod
    $ rqalpha mod enable xxx
    # 禁用 Mod
    $ rqalpha mod disable xxx

======================    ==============================================================================================================
Mod名                      说明
======================    ==============================================================================================================
`sys_analyser`_           【系统模块】记录每天的下单、成交、投资组合、持仓等信息，并计算风险度指标，并以csv、plot图标等形式输出分析结果
`sys_funcat`_             【系统模块】支持以通达信公式的方式写策略
`sys_progress`_           【系统模块】在控制台输出当前策略的回测进度。
`sys_risk`_               【系统模块】对订单进行事前风控校验
`sys_simulation`_         【系统模块】支持回测、撮合、滑点控制等
`sys_stock_realtime`_     【系统模块】Demo 模块，用于展示如何接入自有行情进行回测/模拟/实盘
`vnpy`_                   【第三方模块】通过 VNPY 对接期货实盘行情和实盘交易
`sentry`_                 【第三方模块】集成 sentry 的扩展，实现错误日志全自动采集、处理
`tushare`_                【第三方模块】Demo Mod，用于展示如何通过tushare 获取实时Bar数据并组装以供RQAlpha使用
`shipane`_                【第三方模块】集成实盘易SDK，用于对接股票实盘跟单交易
======================    ==============================================================================================================

如果您基于 RQAlpha 进行了 Mod 扩展，欢迎告知我们，在审核通过后，会在 Mod 列表中添加您的 Mod 信息和链接。

机构版
============================

..  image:: https://raw.githubusercontent.com/ricequant/rqalpha/master/docs/source/_static/rqalpha_plus.png

目前 RQAlpha 开源版仅开放了日级别的历史数据和日回测功能，如果您是机构用户，需要做算法交易亦或是量化研究，都可以联系我们的机构端产品销售获得机构端产品功能支持。「销售电话」：0755-33967716 「QQ」：4848371

机构端产品功能：

*   可以本地部署，使用pycharm、anaconda等工具做本地策略研发、模拟以及实盘交易，效率大大加强，本地管理自己的策略提高保密性
*   极速调取经过清洗处理的历史数据接口服务，包括了：400多项指标的财务数据，股票、期货、ETF、LOF、分级基金等等10年+的日和分钟、tick级别的历史数据以及每日更新，股票、期货的实时数据支持，指数以及构成，板块分类，股本、换手率、融资融券等，天猫等电商销量数据，公募基金数据，舆情、公告类
*   股票、期货的实盘交易订单管理系统以及实盘下单支持，从回测到实盘交易的一条龙系统以及服务支持
*   策略的管理以及实盘的收益、风险计算等
*   交易数据的保存以及提取分析
*   业绩分析和风险管理系统
*   技术支持及定制化开发

Feature Status
============================

*   VNPY 对接 --> `vnpy`_

    * ✅ 扩展VNPY_Gateway
    * ✅ 实盘交易对接
    * ✅ 数据源对接
    * ✅ 事件源对接

*   Tushare 对接

    * ✅ 数据源对接 --> `rqalpha_mod_sys_stock_realtime`_
    * ✅ 合成分钟线 --> `rqalpha_mod_tushare`_

*   Tick 相关支持

    * ✅ TICK 相关事件支持 --> `EVENT.PRE_TICK` | `EVENT.TICK` | `EVENT.POST_TICK`
    * ✅ handle_tick 函数支持

*   Mod Manager --> `通过 Mod 扩展 RQAlpha`_

    * ✅ 定义 Mod 编写规范, workflow && Doc
    * ✅ 提供 Mod Demo && Tutorial
    * ✅ 提供 `rqalpha install xx_mod` 等命令 加载第三方 Mod

*   Third-party Tools Integration

    * ✅ 集成 Sentry --> `sentry`_

*   i18n

    * 🚫 English Doc

*   Support Options

    * 🚫 OptionAccount
    * 🚫 OptionPosition

*   Support BitCoin

    * 🚫 BitcoinAccount
    * 🚫 BitcoinPosition


加入开发
============================

*   `如何贡献代码`_
*   `基本概念`_
*   `RQAlpha 基于 Mod 进行扩展`_

获取帮助
============================

关于RQAlpha的任何问题可以通过以下途径来获取帮助

*  查看 `FAQ`_ 页面找寻常见问题及解答
*  可以通过 `索引`_ 或者使用搜索功能来查找特定问题
*  在 `Github Issue`_ 中提交issue
*  RQAlpha 交流群「487188429」


.. _Github Issue: https://github.com/ricequant/rqalpha/issues
.. _Ricequant: https://www.ricequant.com/algorithms
.. _RQAlpha 文档: http://rqalpha.readthedocs.io/zh_CN/latest/
.. _Ricequant 文档: https://www.ricequant.com/api/python/chn
.. _Ricequant 社区: https://www.ricequant.com/community/category/all/
.. _FAQ: http://rqalpha.readthedocs.io/zh_CN/latest/faq.html
.. _索引: http://rqalpha.readthedocs.io/zh_CN/latest/genindex.html

.. _RQAlpha 介绍: http://rqalpha.readthedocs.io/zh_CN/latest/intro/overview.html
.. _安装指南: http://rqalpha.readthedocs.io/zh_CN/latest/intro/install.html
.. _10分钟学会 RQAlpha: http://rqalpha.readthedocs.io/zh_CN/latest/intro/tutorial.html
.. _策略示例: http://rqalpha.readthedocs.io/zh_CN/latest/intro/examples.html

.. _参数配置: http://rqalpha.readthedocs.io/zh_CN/latest/api/config.html
.. _API: http://rqalpha.readthedocs.io/zh_CN/latest/api/base_api.html

.. _如何贡献代码: http://rqalpha.readthedocs.io/zh_CN/latest/development/make_contribute.html
.. _基本概念: http://rqalpha.readthedocs.io/zh_CN/latest/development/basic_concept.html
.. _RQAlpha 基于 Mod 进行扩展: http://rqalpha.readthedocs.io/zh_CN/latest/development/mod.html
.. _History: http://rqalpha.readthedocs.io/zh_CN/latest/history.html
.. _TODO: https://github.com/ricequant/rqalpha/blob/master/TODO.md
.. _develop 分支: https://github.com/ricequant/rqalpha/tree/develop
.. _master 分支: https://github.com/ricequant/rqalpha
.. _rqalpha_mod_sys_stock_realtime: https://github.com/ricequant/rqalpha/blob/master/rqalpha/mod/rqalpha_mod_sys_stock_realtime/README.rst
.. _rqalpha_mod_tushare: https://github.com/ricequant/rqalpha-mod-tushare
.. _通过 Mod 扩展 RQAlpha: http://rqalpha.io/zh_CN/latest/development/mod.html
.. _sys_analyser: https://github.com/ricequant/rqalpha/blob/master/rqalpha/mod/rqalpha_mod_sys_analyser/README.rst
.. _sys_funcat: https://github.com/ricequant/rqalpha/blob/master/rqalpha/mod/rqalpha_mod_sys_funcat/README.rst
.. _sys_progress: https://github.com/ricequant/rqalpha/blob/master/rqalpha/mod/rqalpha_mod_sys_progress/README.rst
.. _sys_risk: https://github.com/ricequant/rqalpha/blob/master/rqalpha/mod/rqalpha_mod_sys_risk/README.rst
.. _sys_simulation: https://github.com/ricequant/rqalpha/blob/master/rqalpha/mod/rqalpha_mod_sys_simulation/README.rst
.. _sys_stock_realtime: https://github.com/ricequant/rqalpha/blob/master/rqalpha/mod/rqalpha_mod_sys_stock_realtime/README.rst
.. _vnpy: https://github.com/ricequant/rqalpha-mod-vnpy
.. _sentry: https://github.com/ricequant/rqalpha-mod-sentry
.. _tushare: https://github.com/ricequant/rqalpha-mod-tushare
.. _shipane: https://github.com/wh1100717/rqalpha-mod-ShiPanE
