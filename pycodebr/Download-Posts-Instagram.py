# before: pip install instaloader

from datetime import datetime
import instaloader

# Load the Lib and do login with wish account:
var = instaloader.Instaloader()
var.login('***Your Instagram Account***', '***Your password***')

# Load all posts to profile selecioned:
posts = instaloader.Profile.from_username(var.context, "Content").get_posts()

# The day that want do download the posts:
since = datetime(2021, 1, 16)
until = datetime(2021, 2, 16)

# Checking all posts and download only are within the period:
for post in posts:
    if (post.date >= since and post.date <= until):
        print(post.date)
        var.download_post(post, "Download-Post-Instagram")