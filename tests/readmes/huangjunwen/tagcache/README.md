# TagCache

## Support platform

- linux
- macos

## How to install

```base
$ pip install tagcache
```

## Example usage

Suppose you have a blog. And want to cache blog pages (e.g. home page).

- First you need to create and configure a `Cache` object.

```python
from tagcache import Cache, NotCache

cache = Cache()

# configure the main directory to store cache files
cache.configure('/tmp/blog_cache')

```

- Decorate the content function with the `Cache` object. In the following example
  - `blog-home` is the key name of the cache
  - `expire` specify the expiration in seconds of the cache (7 days), never expire if omitted
  - `blog-new` and `bio` are the tags of the cache
  - finally call the decorated function to get content, the function will use cache or call the original function to generate new content when cache miss

```python
@cache("blog-home", expire=3600*24*7, tags=("blog-new", "bio"))
def home_page_content():
    # generate home page content ...
    ...
    return {"bio": {...}, "recent_blogs": [...]}

    ...
    # in some case content is not available and you don't want
    # to cache the return value.
    return NotCache(return_value)

content = home_page_content()

```

- Later, you make changes to your bio (which is displayed on home page), then you can invalidate all caches containing the bio

```python
cache.invalidate_tag("bio")
```

- Periodically, you need to clean up those expired or invalid files.

```python
cache.cleanup()
```

## How it works

The cache directory looks like:

```bash
.
├── data
│   ├── 18
│   │   └── ae
│   │       └── tag:62696f                  <-- tag directory: hexlify('bio')
│   │           └── 85
│   │               └── 3:110235185         <-- hardlink of 'key:626c6f672d686f6d65'
│   ├── 37
│   │   └── 64
│   │       └── tag:626c6f672d6e6577        <-- tag directory: hexlify('blog-new')
│   │           └── 85
│   │               └── 3:110235185         <-- hardlink of 'key:626c6f672d686f6d65'
│   └── ae
│       └── 08
│           └── key:626c6f672d686f6d65      <-- cache file: hexlify('blog-home')
└── tmp
```

Load process:

1. Try to open exists cache file: `"key:" + hexlify(key)`
1. If not found, generate content (see below)
1. If found, check expiration (`st_mtime` as expire time) and tags validation (`st_nlink`)
    1. If all checks were passed, return the cache directly
    1. Try to flock the cache file in non-blocking mode, generate content if success, return cache otherwise


Generate content process:

1. Create a temporary file under tmp and save serialized content (with tags info as well)
1. Hardlink the temporary file into tag directories (`nlinks + inode number` as link name)
1. Change the `mtime` of the temporary file to the expire time
1. Atomic move (rename) the temporary file to the final destination: `"key:" + hexlify(key)`

Invalidate tag process: just remove the tag directory

## Author

Huang junwen (email: <kassarar@gmail.com>)

## Licence

MIT
