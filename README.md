To install and run this app, several steps need to be taken.

This app requires the TwitterSearch library, which can be found at https://github.com/ckoepp/TwitterSearch

1. Setup an address for twitter data to.

If this is going to be run on a server that is exposed to the web, this step may be skipped.

For security reasons, Twitter does not like localhost or 127.0.0.1. It will let you dynamicly direct it's replies to your
your system though. Several programs let you set HOSTS which will enable remapping. Fiddler
(http://www.telerik.com/download/fiddler) can perform this service. Setting up Fiddler is somewhat browser specific, but
once you have done so, you may go tools->HOSTS and set your remapping with a string that looks like this

        127.0.0.1:8000 www.ThisIsAFakeAddress.com

which Twitter will accept.

2. Get Consumer Key, Consumer Secret, Access Token, and Access Token Secret

Twitter authentication requires that you have these four pieces. You can get all four of them from twitter at
https://apps.twitter.com/. Select Create App, fill out the information (giving the remapped address), then ask for a
Consumer Key, then ask for an Application Access Token.

3. Enter the Consumer Key, Consumer Secret, Access Token, and Access Token Secret

Go to savedata/views.py, and go to this line "ts = TwitterSearch(", Then enter the information into the four fields.

4. Setup a local database

Setup a database for django to use, and enter the information for django to use it into Hashtag_analytics/settings.py

5. Start capturing data.

If this is going to be run on a server that is exposed to the web, this step may be skipped.

Open Fiddler, make sure data capture is on, then start your server. The App is ready to use!
