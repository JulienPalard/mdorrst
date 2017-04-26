Install
-------

Install system requirements for ``lxml``

::

    % sudo apt-get install -y libxml2 libxslt1.1 libxml2-dev libxslt1-dev zlib1g-dev

    Try ``brew install libxml2`` if using a Mac.

Install with ``pip``

::

    % pip install parse-helper

Usage
-----

.. code:: python

    In [1]: import parse_helper as ph

    In [2]: ph.USER_AGENT
    Out[2]: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/55.0.2883.87 Chrome/55.0.2883.87 Safari/537.36'

    In [3]: ph.youtube_serp('scaling redis')
    Out[3]:
    [{'duration': '1:14:51',
      'link': 'https://www.youtube.com/watch?v=rP9EKvWt0zo',
      'title': 'Scaling Redis at Twitter',
      'uploaded': '2 years ago',
      'user': 'Rackspace Developers',
      'views': '52,375 views'},
     {'duration': '19:47',
      'link': 'https://www.youtube.com/watch?v=oLjryfUZPXU',
      'title': 'Scaling Redis and Memcached at Wayfair',
      'uploaded': '2 years ago',
      'user': '@Scale',
      'views': '4,222 views'},
     {'duration': '18:29',
      'link': 'https://www.youtube.com/watch?v=3zxYaI3RQyM',
      'title': 'Horizontally scaled data processing architecture using Redis  - Ophir Hordan',
      'uploaded': '9 months ago',
      'user': 'Redis Labs',
      'views': '321 views'},
     {'duration': '20:12',
      'link': 'https://www.youtube.com/watch?v=0g9Jag4az0g',
      'title': 'Node.js & Redis at Scale',
      'uploaded': '1 year ago',
      'user': 'ViennaJS',
      'views': '1,146 views'},
     {'duration': '46:33',
      'link': 'https://www.youtube.com/watch?v=fyMXt2wI47E',
      'title': 'Fast Data at Internet Scale with Amazon ElastiCache for Redis',
      'uploaded': '4 months ago',
      'user': 'Amazon Web Services - Webinar Channel',
      'views': '1,028 views'},
     {'duration': '42:54',
      'link': 'https://www.youtube.com/watch?v=p3ytSdUQZzA',
      'title': 'FOWA 2013. Sharding and Scaling Your Database. Neha Narula',
      'uploaded': '2 years ago',
      'user': 'Future Insights',
      'views': '10,431 views'},
     {'duration': '22:56',
      'link': 'https://www.youtube.com/watch?v=a19OfVfqsa8',
      'title': 'Scaling Real-time Apps on Cloud Foundry Using Node.js and Redis',
      'uploaded': '4 years ago',
      'user': 'Cloud Foundry',
      'views': '3,063 views'},
     {'duration': '37:45',
      'link': 'https://www.youtube.com/watch?v=7tL2Eoiab7U',
      'title': 'Monitoring and  Scaling Redis at DataDog--Ilan Rabinovitch, DataDog',
      'uploaded': '8 months ago',
      'user': 'Redis Labs',
      'views': '150 views'},
     {'duration': '34:57',
      'link': 'https://www.youtube.com/watch?v=g69-3He_IYs',
      'title': 'Scaling Redis Cluster  Deployments for Genome Analysis--Terry Weatherland, IBM',
      'uploaded': '8 months ago',
      'user': 'Redis Labs',
      'views': '213 views'},
     {'duration': '22:22',
      'link': 'https://www.youtube.com/watch?v=pdrzRx0QHcU',
      'title': 'Sourav Sachin - Scaling with Unconventional Tech Stack nodejs + redis + mongodb',
      'uploaded': '4 years ago',
      'user': 'HasGeek TV',
      'views': '877 views'},
     {'duration': '25:58',
      'link': 'https://www.youtube.com/watch?v=6OvrFkLSoZ0',
      'title': 'Flight Lightning - Scaling Twitter core infrastructure',
      'uploaded': '2 years ago',
      'user': 'Twitter Dev',
      'views': '2,505 views'},
     {'duration': 'playlist',
      'link': 'https://www.youtube.com/watch?v=CoQcNgfPYPc&list=PL6QyeBG3jUEawDdZU-4DwBRYY0zyP_Rfn',
      'title': 'Redis',
      'uploaded': 'View full playlist (58 videos)',
      'user': 'Евгений Даниленко',
      'views': 'View full playlist (58 videos)'},
     {'duration': '49:35',
      'link': 'https://www.youtube.com/watch?v=UXnVYb-mqoo',
      'title': 'Josiah Carlson: Scaling Postgres With Some Help from Redis',
      'uploaded': '3 years ago',
      'user': 'PostgresOpen',
      'views': '449 views'},
     {'duration': '1:14:50',
      'link': 'https://www.youtube.com/watch?v=ahT006O7S9k',
      'title': 'AustinPHP - Scaling PHP Applications with Redis',
      'uploaded': '4 years ago',
      'user': 'AustinTechVideos',
      'views': '1,536 views'},
     {'duration': '34:39',
      'link': 'https://www.youtube.com/watch?v=p-XNGlUoPQg',
      'title': 'Scaling Rails Using Redis  with Limited Dev Resources-- Dmitry Polyakovsky, Snap Raise',
      'uploaded': '8 months ago',
      'user': 'Redis Labs',
      'views': '184 views'},
     {'duration': '27:04',
      'link': 'https://www.youtube.com/watch?v=nFJ7LD-2yXc',
      'title': 'Scaling with Redis Enterprise',
      'uploaded': '2 weeks ago',
      'user': 'Redis Labs',
      'views': '19 views'},
     {'duration': '39:22',
      'link': 'https://www.youtube.com/watch?v=A4xmIV0viv4',
      'title': 'How Hulu Scales Services to Support 400 Million Plays: C* , Redis, and SSD-Based Hardware',
      'uploaded': '2 years ago',
      'user': 'Hakka Labs',
      'views': '3,258 views'},
     {'duration': '27:04',
      'link': 'https://www.youtube.com/watch?v=3S-SXAxhgEQ',
      'title': 'Scaling with Redis Enterprise',
      'uploaded': '3 weeks ago',
      'user': 'Redis Labs',
      'views': '41 views'},
     {'duration': '10:37',
      'link': 'https://www.youtube.com/watch?v=S_jA39Uayak',
      'title': 'Predis in Laravel - Redis Series Episode 1',
      'uploaded': '1 year ago',
      'user': 'Christophe Limpalair',
      'views': '14,958 views'},
     {'duration': '45:53',
      'link': 'https://www.youtube.com/watch?v=jQNCuD_hxdQ',
      'title': 'GOTO 2014 • Scaling Pinterest • Marty Weiner',
      'uploaded': '2 years ago',
      'user': 'GOTO Conferences',
      'views': '5,904 views'}]

    In [4]: ph.google_serp('scaling redis')
    Out[4]:
    [{'link': 'https://redis.io/topics/partitioning',
      'title': 'Partitioning: how to split data among multiple Redis instances. – Redis'},
     {'link': 'http://highscalability.com/blog/2014/9/8/how-twitter-uses-redis-to-scale-105tb-ram-39mm-qps-10000-ins.html',
      'title': 'How Twitter Uses Redis to Scale - 105TB RAM ... - High Scalability'},
     {'link': 'http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Scaling.RedisReplGrps.html',
      'title': 'Scaling Redis Clusters with Replica Nodes - Amazon ElastiCache'},
     {'link': 'http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Scaling.RedisStandalone.ScaleUp.html',
      'title': 'Scaling Up Single-Node Redis Clusters - Amazon ElastiCache'},
     {'link': 'https://redislabs.com/ebook/part-3-next-steps/chapter-10-scaling-redis/',
      'title': 'Chapter 10: Scaling Redis - Redis Labs'},
     {'link': 'https://redislabs.com/blog/scaling-out-redis-read-only-slaves-or-cluster/',
      'title': 'Scaling Out Redis: Read-Only Slaves or Cluster? - Redis Labs'},
     {'link': 'http://petrohi.me/post/6323289515/scaling-redis',
      'title': 'ten thousand hours • Scaling Redis'},
     {'link': 'https://www.quora.com/How-scalable-is-Redis',
      'title': 'How scalable is Redis? - Quora'},
     {'link': 'https://www.linkedin.com/pulse/how-twitter-uses-redis-scale-105tb-ram-39mm-qps-10000-iravani',
      'title': 'How Twitter Uses Redis To Scale - 105TB RAM, 39MM QPS ... - LinkedIn'},
     {'link': 'https://docs.microsoft.com/en-us/azure/redis-cache/cache-how-to-scale',
      'title': 'How to Scale Azure Redis Cache | Microsoft Docs'}]
