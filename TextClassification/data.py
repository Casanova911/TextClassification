


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
        print path
        
        
    
        
