req:
	chmod +x *
	pip install gensim
	pip install pandas

split:
	split -d -n l/22 --additional-suffix=".txt" --verbose data/hi/hi.txt data/hi/hi_

Q1_preprocessing:
	echo "preprocessing the cbow model"
	python3 Ques1/cbow.py
	echo "preprocessing the fasttext model"
	python3 Ques1/fasttext.py
	echo "preprocessing the skipgram model"
	python3 Ques1/sg.py
	echo "preprocessing the glove model"
	python3 Ques1/glove.py

runq1_models:
	echo "Generating output in accuracy.csv for cbow model"
	python3 Ques1/run_cbow.py
	echo "Generating output in accuracy.csv for fasttext model"
	python3 Ques1/run_fasttext.py
	echo "Generating output in accuracy.csv for sg model"
	python3 Ques1/run_sg.py
	echo "Generating output in accuracy.csv for glove model"
	python3 Ques1/run_glove.py

runq3_char_ngram:
	echo "Generating Top 100 most frequent char Unigrams"
	python3 Ques3/char_ngram/char_unigram.py
	echo "Generating Top 100 most frequent char Bigrams"
	python3 Ques3/char_ngram/char_bigram.py
	echo "Generating Top 100 most frequent char Trigrams"
	python3 Ques3/char_ngram/char_trigram.py
	echo "Generating Top 100 most frequent char Quadrigrams"
	python3 Ques3/char_ngram/char_quadrigram.py

runq3_word_ngram:
	echo "Generating Top 100 most frequent word Unigrams"
	python3 Ques3/word_ngram/word_unigram.py
	echo "Generating Top 100 most frequent word Bigrams"
	python3 Ques3/word_ngram/word_bigram.py
	echo "Generating Top 100 most frequent word Trigrams"
	python3 Ques3/word_ngram/word_trigram.py

runq3_syllable:
	echo "Generating Top 100 most frequent syllable Unigrams"
	python3 Ques3/word_ngram/word_unigram.py
	echo "Generating Top 100 most frequent syllable Bigrams"
	python3 Ques3/word_ngram/word_bigram.py
	echo "Generating Top 100 most frequent syllable Trigrams"
	python3 Ques3/word_ngram/word_trigram.py


run_mapping:
	python3 Ques3/Mapping.py

run_ques2:
	python3 Ques2/indicbertmodel.py