from textblob.classifiers import NaiveBayesClassifier

with open('sentiment.json', 'r', encoding='utf8') as fp:
    cl = NaiveBayesClassifier(fp, format="json")

print(cl.classify("Dilma é muito boa"))
