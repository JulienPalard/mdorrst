
# VidMe API

This is an entry-level extracted API for VidMe. Please see `main.py` for many use-case examples.

Now on pip! `pip install vidme`.

GitHub IO Page: https://kingfredrickvi.github.io/VidMeAPI/

## Installation

This package needs the following pips:

* `pip install requests`

Please see `requirements.txt` for an up-to-date list.

## Settings

In order to set up your account, just copy and paste 'settings.json.example' to 'settings.json' and add your username and password. If you would rather not, if you do not add a username or password, it will prompt you for the ones you didn't add when you run it. Please be aware it is stored in plain text.

Example:

```
Settings.json:

{"username": "AwesomeFred", "password": "chivermetimbers"}
```

## OAuth

Right now there is basic OAuth support.

```
Settings.json:

{
	"username": "asdf",
	"password": "asdf",

	"oauth": {
		"client_id": "asdfasdf",
		"key": "asdfasdf",
		"secret": "asdfasdf",
		"redirect_uri": "http://localhost:5010",
		"scope": ["auth_management", "videos", "account", "etc"]
	},

	"code": "asdfasdf-optional",
	"token": "asdfasdf-optional"
}
```

When you try to authenticate a user via oauth, this application will open a new window to vidme and wait for the user to click 'authorize account'. Once it does, vidme will redirect to localhost:5010 (this application) and this application will grab the authorization code. If you would like to skip this process because you are doing it your own way, just pass in the parameter 'code' on creation of the session with the code and it will not run through that whole process.

(That probably doesn't really make much sense but check out the Example section below).

If you would like to get the code yourself, check out this example link:

```
'https://vid.me/oauth/authorize?' + \
	'scope=' + self.scope + '&' + \
	'client_id=' + self.client_id + '&' + \
	'response_type=code&' + \
	'redirect_uri=' + self.redirect_uri + '&' + \
	'authorization=allow'
```

```
https://vid.me/oauth/authorize?
	scope=auth_management,videos,account&
	client_id=asdfasdf&
	response_type=code&
	redirect_uri=http://localhost:5010&
	authorization=allow
```

This will return the URL: http://localhost:5010/?code=sdoijfaoisjefoisjdfdsf

Token is returned both when you sign in through username/password and code. Save it in the field token if you do not want to store username/password or oauth stuff.

(This probably doesn't really make much sense either but check out the Example section below).

From here you're golden! You just pass session around the same if it's username/password or OAuth. Just remember that for each seperate account, you need a new 'session' instance.

### Setup

Go to:

https://vid.me/oauth/client/create

Create a new application. The only thing that is important is 'Redirect URI Prefix'. Set this
to 'http://localhost:5010' if you would like to use the built-in auto OAuth token fetching. The rest can be what ever you want. It won't really effect anything.

Once it has been created, you will see it in your list of OAuth clients found here:

https://vid.me/oauth/clients

In your settings.json, paste in your client_id, key, and secret. If you are only doing read-only operations, you can leave your secret key as "".

Scope is what your program can mess with on that users account. Please browse https://docs.vid.me/ to find out different permissions what what calls need what permissions. Look for the 'Permission: blah' sentence.

One last thing: Do not use the built-in OAuth token fetching feature on production lol. Please use HTTPS and a more fancy mechanism. It's there so you can do OAuth testing or local scripts, etc.

### Examples

#### Example 1

```
settings = {
	"oauth": {
		"client_id": "asedfasdfasdf",
		"key": "asdfasdfasdf",
		"secret": "afefasdfasdf",
		"redirect_uri": "http://localhost:5010",
		"scope": ["video_upload"]
	}
}

session = vidme.Session(settings, no_output=True)

video = vidme.Video(uri="C:\dir\dir\supervideo.mp4")
video.upload(session, "Cool title!")
```

#### Example 2

```
settings = {
	"code": "asoijefoisefsf"
}

session = vidme.Session(settings, no_output=True)

video = vidme.Video(uri="C:\dir\dir\supervideo.mp4")
video.upload(session, "Cool title!")
```

#### Example 3:

```
settings = {
	"token": "sadfasdfsfasdfasdf"
}

session = vidme.Session(settings, no_output=True)

video = vidme.Video(uri="C:\dir\dir\supervideo.mp4")
video.upload(session, "Cool title!")
```

## Upload

To upload a video, just do:

```
python main.py upload "c:/dir/dir/myvideo.mp4" "title" "C:/dir/dir/myThumbnail.jpg"
```

If you do not give it a title, the name of the video will be used. You also do not need to give it a thumbnail if you don't want to upload one. After thumbnail, you can give a category id, such as "270" (for Music).

## Download

To download a video, you can do one of three things:

```
python main.py download video 480p https://vid.me/WP35 "c:/dir/dir/"
python main.py download album 480p 90822 "c:/dir/dir/"
python main.py download user 480p https://vid.me/DidYouKnowGaming "c:/dir/dir/"
```

Generally, the following formats work:

* `240p`
* `480p`
* `720p`
* `1080p`

(The only way to get an album is by its ID. It's a limitation on the API).

## Commands

(If you just run `python main.py`, it will start a command terminal)

`<string>` means it's required. `[string]` means it's optional to have. If the argument you are passing has a space in it, you need to wrap it in quotes.

Example: 

Syntax: `command <arg1> [arg2]`

The following would be acceptable: `command hello`, `command hello hi`, `command hello "How are you!"`

As a note: all commands need to start with: `python main.py` if you are not running inside of the command terminal. So `python main.py command hello`.

### Upload

Syntax:

* `upload <path to video> [title] [path to thumbnail] [channel_id/category_id]`

Examples:

* `upload C:\dir\dir\myvideo.mp4`
* `upload C:\dir\dir\myvideo.mp4 "My cool title!"`
* `upload C:\dir\dir\myvideo.mp4 "My cool title!" "C:\dir\dir\mythumbnail.jpg"`
* `upload C:\dir\dir\myvideo.mp4 "My cool title!" "C:\dir\dir\mythumbnail.jpg" 270`

### Upload Folder

* `upload_folder <path to folder> [regex]`

Examples:

* `upload_folder C:\dir\dir\` (By default, targets MP4 files.)
* `upload_folder C:\dir\dir\ *.avi`

Automatically upload JPG/PNG thumbnails with the same name as video file.

IE: `C:\dir\myvideo.mp4`, `C:\dir\myvideo.jpg`: myvideo.mp4 will upload and the myvideo.jpg will be uploaded and set as thumbnail.

### Download

Accepts an album id or a video url / video code. If you give an album id, it will
download all videos in that album. The name of the video that is saved will be
the title of the video. In the future I will add an option to name video.

Syntax:

* `download <link type> <format> <video url | video code | username | user url | album id> <path to folder to download video(s) to> [args...]`

Arguments:

* `link type`: ['video', 'user, 'album']
* `format`: ['480p', '240p', '720p', '1080p']
* `video url | video code | username | user url | album id`: ['https://vid.me/qhIM', 'qhIM', 'KingFredrickVI', 'https://vid.me/KingFredrickVI', 90822]

*Note: (90822 is an id of a album)*

Flags:

* `--no-overwrites` - If file exists, skip downloading.
* `-w` - If file exists, skip downloading.
* `--write-description` - Writes the description of the video to 'title.description'.
* `--write-comments` - Writes the top-level comments to 'title.comments'. In the future, I need to make this write JSON instead of a custom format. Just dump the comment meta with a key of comment_id.
* `--write-thumbnail` - Writes the thumbnail of the video to 'title.jpg'.
* `--write-info-json` - Writes the video's meta to 'title.info.json'.
* `--no-download` - Don't download the video.

Examples:

* `download video 480p https://vid.me/qhIM C:\dir\dir\`
* `download video 480p qhIM C:\dir\dir\`
* `download video 480p vid.me/qhIM C:\dir\dir\`

* `download video 480p vid.me/qhIM C:\dir\dir\ --write-comments --write-description`
* `download video 480p vid.me/qhIM C:\dir\dir\ -w`
* `download video 480p vid.me/qhIM C:\dir\dir\ --write-info-json`

* `download album 480p 90822 C:\dir\dir\`

* `download user 480p KingFredrickVI C:\dir\dir\`
* `download user 480p vid.me/kingfredrickVI C:\dir\dir\ -w`
* `download user 480p https://vid.me/kingfredrickvi C:\dir\dir\ --write-info-json`

## Usage

### General Functions

General functions. Does not required to be logged in, etc. or settings.

Order options: `video_id`, `view_count`, `date_completed`, `score`

Direction options: `ASC` or `DESC`

#### get_featured

Options:

* offset (int)
* limit (int)
* marker (string)
* order (string)

Examples:

```
print [video.get_title() for video in vidme.get_featured()]
```

#### get_hot

Options:

* subindex (int)
* offset (int)
* limit (int)

Examples:

```
print [video.get_title() for video in vidme.get_hot(offset=10)]
```

#### get_new

Options:

* nsfw (1 for true, 0 for false)

Examples:

```
print [video.get_title() for video in vidme.get_new(nwfw=0)]
```

#### get_trending

Options:

* offset (int)
* limit (int)

Examples:

```
print [video.get_title() for video in vidme.get_trending()]
```

#### get_search(query)

Options:

* nsfw (1 for true, 0 for false)
* order (string :: 'likes_count', 'hot_score', 'date_completed')
* user (string)

Examples:

```
print [video.get_title() for video in vidme.get_search('#keyboard', user="kingfredrickvi")]
```

### Sessions

This stores the Vid.Me token that is returned when it attempts to log in. This is used to tell the server you really are who you say you are when you try to do things like edit a video's title.

Example:

```
settings = get_settings('settings')

session = vidme.Session(settings)
```

### Videos

To get a new video object, any of the three following will work:

```
video = vidme.Video(url = "https://vid.me/Z47b")

video = vidme.Video(video_id = 14854593)

video = vidme.Video(code = "Z47b")
```

Using a getter:

```
print video.get_title()
```

Getters:

* `get_video_id()`
* `get_likes()`
* `get_comments()`
* `get_url()`
* `get_full_url()`
* `get_embed_url()`
* `get_complete()`
* `get_complete_url()`
* `get_state()`
* `get_title()`
* `get_description()`
* `get_duration()`
* `get_height()`
* `get_width()`
* `get_date_created()`
* `get_date_stored()`
* `get_date_completed()`
* `get_comment_count()`
* `get_view_count()`
* `get_version()`
* `get_nsfw()`
* `get_thumbnail()`
* `get_thumbnail_url()`
* `get_score()`
* `get_private()`
* `get_total_watchers()`
* `get_watcher_countries()`
* `get_uri()` - Location of file on your disk. Only set if you set it.

Setters:

* `set_title(session, title)` - `title`: new title of video.
* `set_description(session, description)` - `desc`: new description of video.
* `set_source(session, source)` - Yeah idk either.
* `set_private(session)` - Sets video to private.
* `set_public(session)` - Sets video to public.
* `set_latitude(session, latitude)` - `latitude`: lat coords I guess?
* `set_longitude(session, longitude)` - `longitude`: long coords I guess?
* `set_place_id(session, place_id)` - `place_id`: the place_id from foursquare.
* `set_place_name(session, place_name)` - `place_name`: The place name from foursquare.
* `set_nsfw(session)` - Once set, you cannot undo.
* `flag(session, flag = 1)` - Flag the video. 1 to flag. 0 to unflag I guess.
* `vote(session, vote = True, time = 0.0)` - `vote`: upvote if True, take away upvote if false, `time`: Time in the video at which you decided to upvote.
* `delete(session)` - Deletes the video.
* `set_channel(session, channel_id)` - Sets the channel/category for a video.

### Users

To get a new user object, any of the three following will work:

```
user = vidme.User('kingfredrickvi')
user = vidme.User(username='kingfredrickvi')
user = vidme.User(user_id=15864858)
```

Using a getter:

```
print user.get_username()
```

Getters:

* `get_user_id()`
* `get_username()`
* `get_full_url()`
* `get_avatar()`
* `get_avatar_url()`
* `get_cover()`
* `get_cover_url()`
* `get_video_views()`
* `get_likes_count()`
* `is_following(ouser)` - `ouser`: user to follow. Is a class User.
* `is_blocked(ouser)` - `ouser`: user to follow. Is a class User.
* `get_videos(refresh=False, limit=15, offset=0, session=None, order="video_id", private=0)` - `refresh`: Get fresh list of videos. `session` - If you want to list videos that are unlisted or private. `private` - Show private videos or not. If you haven't called it before, it returns a generator. Please see `get_comments` for more information.
* `get_followers(refresh=False, limit=15, offset=0)` - `refresh`: Get fresh list of followers. If you haven't called it before, it returns a generator. Please see `get_comments` for more information.
* `get_following(refresh=False, limit=15, offset=0)` - `refresh`: Get fresh list of following. If you haven't called it before, it returns a generator. Please see `get_comments` for more information.
* `get_albums(refresh=False, limit=15, offset=0)` - `refresh`: Get fresh list of albums. If you haven't called it before, it returns a generator. Please see `get_comments` for more information.

Sort Values:

`"recent"`, `"older"`, `"popular"`, `"lesswatched"`

Setters:

* `set_username(session, username)` - `username`: The new username.
* `set_password(session, password, passwordCurrent)` - `password`: new password, `passwordCurrent`: current password.
* `set_bio(session, bio)` - `bio`: New biography for user profile.
* `set_displayname(session, displayname)` - `displayname`: new display name.
* `set_email(session, email)` - `email`: new email address.

Operations:

* `follow_user(session, user)` - `user`: user to follow. Is a class User.
* `unfollow_user(session, user)` - `user`: user to unfollow. Is a class User.
* `unsubscribe_user(session, user)` - `user`: user to unsubscribe. Is a class User.

### Comments

To get the comments for a video, do the following:

```
video = vidme.Video(video_id = 14854593)

comments = video.get_comments()
```

It is important to note that the first time you retrieve get_comments, it will
return a generator. This means that every time you access it, it returns the
next `limit` of comments. This is so you don't have to make a bunch of API
calls all at once if you don't have to. To get all comments, do the following:

```
comments = [comment for comment in video.get_comments()]
```

Once you run through get_comments once, it will return the complete list
of comments without having to make any calls to the API. So from that point on,
you can just do:

```
comments = video.get_comments()
```

Getters:

* `get_comment_id()`
* `get_video_id()`
* `get_user_id()`
* `get_parent_comment_id()`
* `get_full_url()`
* `get_body()`
* `get_date_created()`
* `get_made_at_date()`
* `get_score()`
* `get_comment_count()`
* `get_user()`
* `get_viewerVote()`
* `get_comments()` - Returns an array of Comment objects.

Setters:

* `vote(session, vote = True)` - `vote`: upvote if True, take away upvote if false
* `delete(session)` - Deletes the comment.

### Likes

To get the likes for a video, do the following:

```
video = vidme.Video(video_id = 14854593)

likes = video.get_likes()
```

The limit is 20 by default. To increase the number, just pass as parameter.

```
likes = video.get_likes(limit=50)
```

Getters:

* `get_vote_id()`
* `get_video_id()`
* `get_user_id()` - user_id of the person who liked video
* `get_value()` - 1 for liked, 0 for not liked. (You can unlike video. If you do, this is set to 0.)
* `get_date_created()`
* `get_date_modified()`
* `get_user()` - Returns a User instance.
