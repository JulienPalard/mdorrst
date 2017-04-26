Constantine
===================
Constantine is a [Python 3](https://www.python.org/downloads/) tool for automatically generating event posters from public Google Calendar events. It is primarily written for [HackSoc](https://hacksoc.org) of University of York to partially automate some publicity work, but is written in a very adaptable way for other uses. It uses [XeTeX](http://xetex.sourceforge.net/) for PDF typesetting.

Constantine requires Python 3.3+ and XeLaTeX.

# Google Calendar API Access #
First, to access Google Calendar, even just for public events, you need a Google API Key, which can be obtained by visiting Google API Console [here](https://console.developers.google.com/apis/credentials), you may wish to create a new Google API project for Constantine when prompted.

You will also need to enable Google Calendar access for your API key, which can be enabled by clicking the "Enable" button after searching for Google Calendar in the Google Developer Console, as shown below:

![Google Calendar API Access](https://i.imgur.com/QxBoJp5.png)

# Configuration #
After obtaining the API Key, **copy `Docs/settings-example.json` to a place of your liking, such as `~/.Constantine.json`**.

Edit your `settings.json` as followed:
* `logo`: either relative path or absolute path of your organisation's logo, which is highly recommended to be a background-transparent PNG file.
* `url`, `email`, `irc_network`, `irc_channel`, `twitter`, `facebook`: contact information for your organisation, modify as appropriate.
* `calendar_id`: the Google Calendar ID for the calendar you want to fetch events from, a guide for finding the ID can be found [here](https://support.appmachine.com/hc/en-us/articles/203645966-Find-your-Google-Calendar-ID-for-the-Events-block).
* `google_api_key`: the Google API Key you just obtained above, the default one is access-restricted and will **not** work for you. Make sure that the API Key's access to Google Calendar is enabled as shown above.
* `term_start_dates`: a list of dates for starts-of-terms, used for University of York's week numbering, as it appears in the generated PDF.
* `page_background_colour`, `page_normal_text_colour`, `page_emphasis_text_colour`, `page_deemphasis_text_colour`: Hex colour codes for the background and text colours in the generated PDF, modify if you would like to change the colour scheme.

# Installation and Use #
Constantine only has one dependent package, [requests](http://docs.python-requests.org/en/master/), which can be installed by:

    pip install requests

Now install Constantine via pip:

    pip install Constantine

Make sure that XeLaTeX works on your system by executing `xelatex -version`, then run Constantine like this:

    Constantine ~/Downloads/output.pdf --text=~/Documents/Constantine.txt --date=2017-02-01 --config=~/.Constantine.json

Optional arguments:

* `text`: a path to the text file containing the special text, see **Special Text** for more details. `special_text.txt` under the script directory will be used if unspecified.
* `date`: a specific date for Constantine to fetch events for the week **after** that date. Today's date will be used if unspecified.
* `config`: path to your config file, an example of which can be found in `Docs/settings-example.json`. The default configuration file `settings.json` under the script directory will be used if unspecified.

Old style arguments (`Constantine /path/to/output.pdf [YYYY-MM-DD]`) will continue to work for the time being.

And it's done. If any error occurs outputs should provide some clue.

# Special Text #
A text file can contain a section that will be automatically added to the end of the main content, allowing custom text to be added. The first line will be the section title (resembling the style of e.g. "Tuesday") and the rest of the lines will be the section text.
The default file and also the example can be found in `Constantine/special_text.txt`, you can specify a custom file to use by calling Constantine with `--text=/path/to/special/text.txt`.

# ToDo's #
* In LaTeX, `multicols*`(multiple columns without balancing) cannot be used inside a box, without which the bottom dotted line seems difficulty to fit. I am pretty terrible at LaTeX, so if you have a better solution please do send a pull request :)
* ~~Sorry for the horrible packaging, by the way. The lack of OOP in this hacked-together solution makes good packaging difficult.~~ It's done!
