import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt
# all 4 authentication keys to access twitter API
# to connect as OAth handler or jump serever / revers proxy server
consumer_key = "8AO6OU5ubyi4XO47b1C7Sjdlz"
consumer_sec = "FS1usPrfPolvjLXbwGka5N8TWkOZhUsdxGmmTwuO016koesUSt"

# from proxy server we need to connect
access_token = "1151573806680592384-OUFeUtpsRFZM6jQxl1AG99NEjlY0Kt"
access_token_sec = "KKHmkHkDGVaDof8XK4fKKI52DmNl4vZlaXnx85WRfd4Lr"
# connected to jump server of twitter
auth =tweepy.OAuthHandler(consumer_key,consumer_sec)
#now we can connect from jump server to web server of twitter
auth.set_access_token(access_token,access_token_sec)
#new we can connect to API strong server of twitter
api_connect=tweepy.API(auth)
tweet_data = api_connect.search('riya',count=100)
tweet_data
for tweet in tweet_data:
  print(tweet.text)
  pos=0
neg=0
neu=0

# printing line by line
for tweet in tweet_data:
   print(tweet.text)
   analysis=TextBlob(tweet.text)
   print(analysis.sentiment)
  
   if analysis.sentiment.polarity > 0:
      print("positive")
      pos=pos+1
   elif analysis.sentiment.polarity == 0 :
      print("Neutral")
      neu=neu+1
   else :
      print("Negative")
      neg=neg+1
      

plt.xlabel("tags")
plt.ylabel("polarity")

plt.pie([pos,neg,neu],labels=['pos','neg','neu'],autopct="%1.1f%%")
plt.show()
   
