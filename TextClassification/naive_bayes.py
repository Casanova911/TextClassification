

class NaiveBayes(object):
    def __init__(self, data, feature_extractor, vocabulary, load_model, model_name):
        '''
            Training (and save) classify model or load model from data using 
            feature_extractor ( and maybe using vocabulary)  
            
            Args:
                data: label text to training model
                feature_extractor: a function to extract feature from a text
                vocabulary: a vocabulary to limit feature 
                load_model: option to load model from specific file without
                    training
                model_name: name of model (to save or load)
            Return:
                a classifier using bayes method
        '''
        print 'New Naive Bayes object was created'
        self.labels = [label for label in data]
        self.feature_extract = feature_extractor
        self.model = {}
        self.training_model(data)        
    
    def counting_feature(self, data):
        '''
            Args:
            Return:
        '''
        count_label = {}
        all_features = {}        
        for label in self.labels:
            count_label[label] = float(len(data[label]))
            for text_id in data[label]:
                features_of_text = self.feature_extract(data[label][text_id])
                for feature in features_of_text:
                    if feature not in all_features:
                        all_features[feature] = {}
                    if label not in all_features[feature]:
                        all_features[feature][label] = {'found_doc': 0, 'found_key': 0}
                    all_features[feature][label]['found_doc'] += 1
                    all_features[feature][label]['found_key'] += data[label][text_id].lower().count(feature)
        return (all_features, count_label)
    
    def quantization(self, value):
        '''
            Measurement a value in quantization
            Args:
                a value
            Return:
                a measure 
        '''
        if value <= 0.01:
            return 1
        elif value <= 0.06:
            return 2
        elif value <= 0.09:
            return 3
        elif value <= 0.15:
            return 4
        elif value <= 0.2:
            return 5
        elif value <= 0.3:
            return 7
        elif value <= 0.4:
            return 10
        elif value <= 0.6:
            return 15
        elif value <= 0.8:
            return 20
        else: 
            return 30               
                                 
    def probability_calculate(self, all_features, count_label):
        for feature in all_features:
            self.model[feature] = {}
            sum = 0.0            
            for label in all_features[feature]:
                sum += all_features[feature][label]['found_doc'] * all_features[feature][label]['found_key'] / count_label[label]                        
            for label in all_features[feature]:
                probability = ((all_features[feature][label]['found_doc'] * all_features[feature][label]['found_key']) / count_label[label]) / sum                                           
                self.model[feature][label] = self.quantization(probability) 
                    
    def training_model(self, data):
        print 'Training classification model (Bayes)'              
        (all_features, count_label) = self.counting_feature(data)
        self.probability_calculate(all_features, count_label)
        
    def classify(self, text):        
        feature_of_text = self.feature_extract(text)
        label_result = 0
        prob_result = 0.0        
        for label in self.labels:
            probability = 1.0
            for feature in feature_of_text:
                if feature in self.model:
                    if label in self.model[feature]:
                        probability *= self.model[feature][label]
                    else:
                        probability *= 0.001
                else:
                    probability *= 0.001
            if probability >= prob_result:
                prob_result = probability
                label_result = label
        return label_result         
        
        
               
                                   
        
