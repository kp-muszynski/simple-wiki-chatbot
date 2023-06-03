# Simple Wiki Chatbot

The purpose of this mini project was to build a simple chatbot working in the Python console, using wikipedia library. 

## Libraries

I'm using nltk in order to lemmatize sentences, sklearn for determining the similarity of sentences and of course wikipedia (random and warnings are used for technical purposes).

From nltk among others, wordnet is necessary, so it has to be downloaded:
```
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('punkt')
```
## Functions

Firstly, I define a lemmatizing function (lemma_me), which finds lemmas of words in a sentence and is passed to another function (process). This function calculates cosine similarity between tokenized text and a question and returns the sentence that has the best match to that question, providing that its coefficient is greater than 0.3. 

## Chatbot

The bot is initialized in the console using `while True:` loop. The user enters a topic that is searched in wikipedia library, handling the PageError and DisambiguationError expceptions. If there are more than one result, the code randomly chooses an option and continues to do so, until it finds the unique page. In case PageError is encountered, the user is asked to try again. 
The final topic is displayed and a question should be inserted, to which process function is applied. The user has an option to quit or exit the loop entirely.

Example:
![The bot](Bot_screen.png)

