# coding= utf-8
from data import Data
from extractor import get_all_words
from naive_bayes import NaiveBayes
from evaluate_classifier import EvaluateClassifier

def main():
    data = Data()
    training_data = data.load_text('data\\100\\train\\')
    test_data = data.load_text('data\\100\\test\\')
    classifier = NaiveBayes(training_data, get_all_words)
    evaluate = EvaluateClassifier() 
    evaluate.print_evaluation(classifier, test_data)          
    #vocab = data.load_vocabulary('vocab.txt') 
    #print classifier.classify('du lịch')
     
if __name__ == '__main__':
    main()    
    