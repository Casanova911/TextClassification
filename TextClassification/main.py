from data import Data

def main():
    data = Data()
    training_data = data.load_text('data\\10\\train\\')
    
    for topic in training_data:
        print topic
        for file in training_data[topic]:
            print file
            print training_data[topic][file]
     

if __name__ == '__main__':
    main()    
    