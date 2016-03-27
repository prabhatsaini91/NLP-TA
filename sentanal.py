from textblob import TextBlob
import nltk
from nltk.corpus import opinion_lexicon as ol
from textblob.sentiments import NaiveBayesAnalyzer

pos_sentiment = {}
neg_sentiment = {}

text = raw_input('$ ')
words = text.split()
name = 'Prabhat Saini'

def getpersonaldetails() :
	name = 'Prabhat Saini'
	sex = 'Male'
	dob = '30th November 1991'
	personality = 'ENTP'
	return (name, sex, dob, personality)

def getdetails() :
	name, sex, dob, personality = getpersonaldetails()

##check for positive terms in the text
pos_words = [word for word in ol.positive()]
##print pos_words
neg_words = [word for word in ol.negative()]
##print neg_words

##create positive and negative word indices and use as dictionary
for word in words :
	if word in pos_words :
		pos_sentiment[word] = 'positive'
	if word in neg_words :
		neg_sentiment[word] = 'negative'

##print words
print pos_sentiment
print neg_sentiment

##proceed to sentiment analysis using textblob naivebayes
text_blob_pattern = TextBlob(text)
text_blob_analysed = TextBlob(text,analyzer=NaiveBayesAnalyzer())
print text_blob_analysed.sentiment
print text_blob_pattern.polarity
print text_blob_pattern.subjectivity
count_words = len(words)

reply = 'I see ' + name + '. That was a '+('pretty short' if count_words < 15 else 'pretty long') + \
		' introduction about how you are feeling. You seem to be reeling on a bit of ' + \
		('positivity' if text_blob_analysed.sentiment.classification=='pos' else 'negativity') + \
		'. I sense ' + str(text_blob_pattern.polarity*100) + ' percent of polarity and ' + \
		str(text_blob_pattern.subjectivity*100) + ' percent of subjectivity' + \
		' in your statements. Do you want more nerd stats?'

print reply



