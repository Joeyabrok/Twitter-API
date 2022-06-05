import tweepy
import pandas as pd
import config


class Keywords(tweepy.Stream):
    
    def on_status(self, status):
      if status.truncated == False:
        text.append(status.text)
      else:
        text.append(status.extended_tweet["full_text"])
       #Adding data to the empty lists initialized on line 34 and below
      username.append(status.user.screen_name)
      date_time.append(status.created_at)
      id.append(status.id_str)
      is_verified.append(status.user.verified)
      num_of_followers.append(status.user.followers_count)
      num_of_favorites.append(status.user.favourites_count)
      num_of_statuses.append(status.user.statuses_count)
      
      #Adding these filled out  list to a dataframe
     user_info = pd.DataFrame({‘Username’: username, ‘ID’: id, ‘Tweet’: text})
     user_metrics = pd.DataFrame({'Verified Status': is_verified, 'Follower Count':num_of_followers, 'Favourites Count':num_of_favorites, 'Statuses Count':num_of_statuses})
     published_datetime = pd.DataFrame({'DateTime Created': date_time})
     
     #Loading the extracted data to a CSV file
     user_info.to_csv('twitteruserinfo.csv',index=False)
     user_metrics.to_csv('twitterusermetrics.csv',index=False)
     published_datetime.to_csv('twitteruserpublisheddatetime.csv',index=False)

#place consumer keys and access tokens into our Keywords class to access twitter API
API_Access = Keywords(config.consumer_key, config.consumer_secret,config.access_token, config.access_token_secret)
API_Access.filter(track=['Golf']) #Input the word you want to filter for.
  
#The empty list below are initialzied. They will store data for each category
text=[]
username= []
date_time=[]
id= []
is_verified=[]
num_of_followers=[]
num_of_favorites=[]
num_of_statuses=[]
