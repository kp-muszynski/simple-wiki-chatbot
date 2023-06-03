import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
import warnings
import wikipedia

wikipedia.set_lang("en")
warnings.filterwarnings("ignore")

nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('punkt')

lemmatizer = WordNetLemmatizer()

def lemma_me(sent):
    sentence_tokens = nltk.word_tokenize(sent.lower())
    pos_tags = nltk.pos_tag(sentence_tokens)

    sentence_lemmas = []
    for token, pos_tag in zip(sentence_tokens, pos_tags):
        if pos_tag[1][0].lower() in ['n', 'v', 'a', 'r']:
            lemma = lemmatizer.lemmatize(token, pos_tag[1][0].lower())
            sentence_lemmas.append(lemma)

    return sentence_lemmas

def process(text, question):
  sentence_tokens = nltk.sent_tokenize(text)
  sentence_tokens.append(question)

  tv = TfidfVectorizer(tokenizer=lemma_me)
  tf = tv.fit_transform(sentence_tokens)
  values = cosine_similarity(tf[-1], tf)
  index = values.argsort()[0][-2]
  values_flat = values.flatten()
  values_flat.sort()
  coeff = values_flat[-2]
  if coeff > 0.3:
    return sentence_tokens[index]


while True:
    continue_i = 0
    topic = input("What topic do you want to search for? (insert 'quit' to exit)\n")
    if topic == 'quit':
        break
    try:
        wikipedia.summary(topic, sentences=1)
    except wikipedia.exceptions.PageError:
        print("Incorrect topic, please try again.")
        continue
    except wikipedia.exceptions.DisambiguationError:
        pass
    text = None
    str1 = ''
    while text is None:
        try:
            text = wikipedia.page(topic).content
        except wikipedia.exceptions.DisambiguationError as e:
            topic = random.choice(e.options)
            str1 = 'Too broad, I chose randomly from related options. '
        except wikipedia.exceptions.PageError:
            print("I tried to choose randomly and encountered an error. Please try again.")
            continue_i = 1
            break
    if continue_i == 1:
        continue
    print(f'{str1}The topic is: {topic}.')
    while True:
        question = input("What do you want to know? (insert 'end' to exit, 'quit' to go back)\n")
        output = process(text, question)
        if question == 'quit':
            break
        elif question == 'end':
            exit()
        elif output:
            print(output)
        else:
            print("I don't know.")