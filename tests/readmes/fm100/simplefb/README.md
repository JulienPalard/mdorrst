# simplefb
A simplefb is the simple facebook graph api library. Python >= 3.5 is required.

## Basic Usage

### import module
    >>> import simplefb

### me
    >>> simplefb.me('my-access-token')
A simplefb module provides function for facebook me api, and it simply requires access token only.

### fb_exchange_token
    >>> simplefb.fb_exchange_token('my-app-id', 'my-app-secret', 'my-short-lived-token')
To get a long-lived access token from facebook, you can use a fb_exchange_token function. It requires app-id, app-secret, and short-lived access token.

### api
    >>> simplefb.api('/me', 'GET', {'access_token': 'my-access-token'})
You may also call api to the any of endpoints via "api" function.
It only supports api which returns JSON objects. Almost every facebook api returns response as the JSON object but some does not, for example, fb_exchange_token.


## Async APIs(coroutine)
Since 0.2.0, simplefb has started to support async coroutine APIs.

### me_async
    >>> await simplefb.me_async('my-access-token')
Same as simplefb.me but it's coroutine.

### fb_exchange_token_async
    >>> await simplefb.fb_exchange_token_async('my-app-id', 'my-app-secret', 'my-short-lived-token')
Same as simplefb.fb_exchange_token but it's coroutine.

### api_async
    >>> await simplefb.api_async('/me', 'GET', {'access_token': 'my-access-token'})
Same as simplefb.api but it's coroutine.

## Mixins
Since 0.2.0, simplefb provides Mixins for Facebook Auth.

```
import simplefb.auth

class MyHandlerSync(simplefb.auth.FBAuthMixin):
    def handler(self):
        long_lived_token = self.exchange_token('short-lived-token')
        fb_user_info = self.me(long_lived_token)
        # Do your stuffs
```

```
import simplefb.auth

class MyHnalderAsync(simplefb.auth.FBAuthAsyncMixin):
    async def handler(self):
        long_lived_token = await self.exchange_token('short-lived-token')
        fb_user_info = await self.me(long_lived_token)
        # Do your stuffs
```
