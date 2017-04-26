I've created this small framework to help myself in scraping. So it basically suits my needs. I've tried to make it as flexible as possible—because the sites I need to scrape are very diverse. Retr stands for RETRieve and RETRy. It does both.

# Features
- multiple threads (legacy version) or async functions.
- Proxy rotation. It won't stop trying new proxies until the page is retrieved. It rearranges the proxies in the list, putting bad ones in the end.
- Easy filtering to use on raw proxy lists (for example from gatherproxy.com).
- Scrapy middleware

# Usage

## Validation of pages
As it keeps retrying the page through different proxies, we need to distinguish between the situation when the proxy returns an error, or the site in question returns a (legitimate) error. To this end, you can add a validation function. Default one checks for the http response code 200, otherwise retries. You can do anything here, for example check for some string you expect in the page (some proxies return admin pages for example).

## Scrapy middleware
The following string should be added to the DOWNLOADER_MIDDLEWARES (pick your own priority):
``` python
'retr.middleware.RandomProxy': 100,
```

### Settings that influence it:
- PROXY_LIST
  Proxy list containing entries like:
  * http://host1:port
  * http://username:password@host2:port
  * host3:port
  
  It will prepend http:// automatically if it's missing.
```python
PROXY_LIST = 'proxies.lst' # Can be a file name (one proxy per line):
PROXY_LIST = ['127.0.0.1:9999', '127.0.0.2:9999'] # Or an iterable
```
 
- PROXY_MODE
  * 'random': Every request will have random proxy from the list
  * 'sequential': Every request will have a new proxy, iterating by the list of all available proxies sequentially.
  * 'once': The proxy will be tried once. Used for filtering

```python
PROXY_MODE = 'sequential'
```

It uses the following meta keys:
* proxy
  Naturally. Preserve it to go through the same proxy (one session), or delete to make a middleware pick new proxy.
* ss_request
  Set this to the Request object used to set up the session. For example you may need to select the location (see a sample), or login and have cookies bound to the chosen proxy address. Then the normal chain of parse functions follows, in the end get original_request key from meta and yield it to continue.
* original request
  The engine stores the current request here and retries it with a new proxy should it be needed after the session setup.
* proxy_mode
  Overrides global PROXY_MODE setting for the given request.