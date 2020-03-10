from tweepy import Stream, OAuthHandler, streaming
import sys
TweetListener = streaming.StreamListener

class TweetsExtractor():

	def stream_tweets(self, file_name, hash_tag_list):
		listener = MyListener(file_name)
		auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
		auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

		stream = Stream(auth, listener)

		stream.filter(track=hash_tag_list)


class MyListener(TweetListener):

	def __init__(self, file_name1):
		self.file_name = file_name1
		self.count=0

	def check_count(self):
		print()
		if self.count>4000:
			sys.exit()
		else:
			print(self.count)
			self.count+=1


	def on_data(self, data):
		self.check_count()
		with open(self.file_name,'a') as f:
			f.write(data)

		return True
       
		

ACCESS_TOKEN = "1222330761723961344-LdAaO50otl31M6HkCJmT49yciD5oQK"
ACCESS_TOKEN_SECRET = "Ry9stlEjoHnV7NldXupoKLwyiByS9a93ViqSjBFqz34K5"
CONSUMER_KEY = "kK4Ic4hBGWlwmzb9I8Tfs7FBc"
CONSUMER_SECRET = "DQDcrHAwn1FT7Buf16RwWFXReS79ZDnyn1v3rC3K6mdlHDijVi"

hash_tags = ['Canada','University','Dalhousie University','Halifax','Canada Education']
myFile = 'Extracted_Tweets.json'

Tweet_counter=0
ts = TweetsExtractor()
ts.stream_tweets(myFile,hash_tags)

