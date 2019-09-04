The Folder 'LEXICONS' contains lexicons from predefined topics from three countries i.e. USA, UK and India. 

The lexicons for each country is generated independently using country specific Wikipedia pages and Tweets. We have total of 2179, 2330 and 2551 lexicons from the country USA, UK and India respectively. 

Since lexicon generation is independent for each country, same lexicon can be present in another country as well. The given lexicons are all lowercased and are lemmatized using NLTK to aid lexicon matching. For preprocessing we suggest you using our code in this repository namely preprocess.py. First call change_alphabet, then call clean_sent to get a list of preprocessed tokens. valid for both plain text and tweets. 

For tagging your text with a topic, we suggest to follow the similar preprocessing. Tokenize the lowercased text and then lemmatize each token. Then search of topic lexicons in your preprocessed text. 

Tag a topic according to the majority matches. 

NOTE: 1. For a generic topic assignment(irrespective of the country) for your text, combine all the lexicons of a topic from each country and then follow the same process. 
      2. These can also be used as seed lexicons and then can further be extended using any Information Retrieval Techniques(such as Query Expansion, Pseudo Relevance Feedback, Synonyms, etc.)
	
