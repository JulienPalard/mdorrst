# AIST novel grab
> novel grab crawler module using python3 and lxml
>
> multiprocesssing with multithread version
>
> winxos, AISTLAB Since 2017-02-19

## INSTALL:
``` pip3 install aist_novel_grab ```

## USAGE:

``` python
    from novel_grab.novel_grab import Downloader
    d = Downloader()
    print(d.get_info())
    if d.set_url('http://book.zongheng.com/showchapter/221579.html'):
        d.start()
```

##TIPS
* When d = Downloader(), d.get_info() can get supported sites info.
* Once d.set_url(url) will return the url is valid or not.
* Of course you can use d.get_info() to access the state of d at any time.
* While finished, will create $novel_name$.zip file in your current path, default zip method using zipfile.ZIP_DEFLATED

* Just for educational purpose, take care of yourself.

