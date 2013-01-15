import os
import codecs
import pickle

class Data(object):
    def __init__(self):
        '''
            initial a data object
        '''
        print 'New data object was created!'
        
    def load_text(self, path):
        '''
            load all text data from file .txt in a directory as a 
            structure of "topic data"
             
            Args:
                path: address of directory to get text data
            
            Return:
                {"topic_name_1":{
                        "file_name_1": text data
                        "file_name_2": text data
                        ...
                        "file_name_n": text data
                    }                        
                "topic_name_2":{
                        "file_name_1": text data
                        "file_name_2": text data
                        ...
                        "file_name_n": text data
                }
                ...
                "topic_name_n":{
                        "file_name_1": text data
                        "file_name_2": text data
                        ...
                        "file_name_n": text data
                    }
                }
                            
            Raises:
                IOError: An error occurred accessing the directory.
                          
        '''
        print 'Load text in: ' + path
        text_data = {}
        for topic in os.listdir(path):
            if os.path.isdir(path + topic):
                text_data[topic] = {}
                topic_path = path + topic + '\\'
                for file in os.listdir(topic_path):                    
                    if os.path.isfile(topic_path + file):
                        txt = codecs.open(topic_path + file, 'r', 'utf-8')
                        content = txt.read()
                        txt.close()                        
                        text_data[topic][file] = content.encode('utf-8')
                
        return text_data
    
    def load_vocabulary(self, path):
        input = open(path, 'rb')
        vocabulary = pickle.load(input)
        input.close()    
        return vocabulary
                    
        
    
        
