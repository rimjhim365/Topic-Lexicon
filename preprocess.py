# coding=utf-8
import unidecode
import inflection
import re
from nltk.corpus import stopwords
stop = stopwords.words('english')
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

def change_alphabet(sent):
	return unidecode.unidecode(sent.decode('utf-8'))

def clean_sent(sent):
	sent=re.sub(r"http\S+", "", sent.lower()).decode('utf-8')
	sent=re.sub(r"@\S+", "", sent.lower()).decode('utf-8')
	#words=sent.split(" ")
	words=tokenizer.tokenize(sent)
	words_refined=[lemmatizer.lemmatize(inflection.singularize(word)) for word in words]
	words=[inflection.transliterate(word.decode('utf-8')) for word in words_refined if not word.isdigit() and len(word)>2]
	p_stemmer = PorterStemmer()
	_digits = re.compile('\d')
	words_refined=[str(word) for word in words if not bool(_digits.search(word)) and word not in stop]
	return words_refined
#sentence="HE !!!! is a https://jbfjerferfe @rimjhim apply ...hates ....rama123 kingis singh has have their Málaga Málaga 2312423534646"
#sentence=change_alphabet(sentence)
#sentence=clean_sent(sentence)
#print sentence
			
	
