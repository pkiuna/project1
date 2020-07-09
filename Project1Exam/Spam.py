from sklearn.naive_bayes import *
from sklearn.dummy import *
from sklearn.neighbors import *
from sklearn.calibration import *
from sklearn.linear_model import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import *
import pandas
    def doThis(classifiers, vector, train_data, test_data ):

         for allocation in classifiers:
            for points in vectorizers:
                string =''
            string += allocation.class.name + 'with' + vectorizer.class.name

        #training
        vector_text = vectorizer.fit_transform(train_data.vector2)
        classifier.fit(vector_text, train_data.vector1)
        #score
        vector_text = vectorizer.fit_transform(test_data.vector2)
        score = classifier.fit(vector_text, test_data.vector1)
        string += "Has this score: " + str(score)

        #opening data set
        data = pandas.read_csv('spam.csv')
        formulate = data[:4000]
        test = data[:4400]

        doThis(  #testing various classifiers
            (
                DummyClassifier(),
                RandomForestClassifier(numberEst=100, numberJobs=-1), #converted list to tuple
                OneVsRestClassifier(SVC(kernel='linear')),
                KNeighborsClassifier(),
            ),
        [
            TfidfVectorizer(),
            CountVectorizer(),
        ],

















