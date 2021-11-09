

# Requirements



pip3 install --upgrade pip
pip3 install tqdm
pip3 install requests
pip3 install requests-toolbelt
pip3 install schedule
pip3 install pysocks
pip3 install responses
pip3 install future
pip3 install six
pip3 install huepy


# Functions


comment_hashtags(`Comments medias of given hashtag`) Parameters: hashtags, commentText
follow_last_user_likers(`Follows the users who liked targeted user's last post`) Parameters: username, numberOfFollows 
follow_user_followers(`Follows targeted user's followers`) Parameters: user, numberOfFollows
follow_users_by_hahstags(`Follows users by given hashtags`) Parameters: hashtags
like_feed_infinitly(`Likes your feed infinitly`) Parameters: none
like_hashtags(`Likes the medias of given hashtags`) Parameters: hashtags, numberOfLikesPerHashtag
like_medias_by_location(`Likes the medias of given location`) Parameters: location, numberOfLikes
message_user_likers(`Messages users who liked targeted user's last post`) Parameters: user, text, numberOfMessages
unfollow_everyone(`Unfollows everyone`) Parameters: none
unfollow_nonfollowers(`Unfollows users who are not following you`) Parameters: numberOfUnfollows
post_scheduler(`Posting regularly`) Parameters: postsPerDay


