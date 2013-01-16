

class EvaluateClassifier(object):
    def print_evaluation(self, classifier, test_data):
        scores = {}
        correct = 0
        total = 0
        labels = test_data.keys()
        for label in labels:
            scores[label] = {"true_pos": 0, "true_neg": 0, "false_pos": 0, "false_neg": 0}
        for label in test_data:
            for txt in test_data[label]:
                classification = classifier.classify(test_data[label][txt])
                total += 1
                if classification == label:                
                    correct += 1
                    scores[label]["true_pos"] += 1
                    for other_label in labels:
                        if other_label != label:
                            scores[other_label]["true_neg"] += 1
                else:
                    scores[label]["false_neg"] += 1
                    scores[classification]["false_pos"] += 1
                    for other_label in labels:
                        if other_label != label and other_label != classification:
                            scores[other_label]["true_neg"] += 1
                                    
        print "Accuracy: " + str(correct / float(total))
        
        for label in labels:
            true_pos = scores[label]["true_pos"]
            false_pos = scores[label]["false_pos"]
            true_neg = scores[label]["true_neg"]
            false_neg = scores[label]["false_neg"]
            print str(label)                        
            precision = true_pos / (true_pos + false_pos)
            recall = true_pos / (true_pos + false_neg)
            print "\tPrecision: " + str(precision)
            print "\tRecall: " + str(recall)
            if (precision != 0 or recall != 0):
                print "\tF-Measure: " + str(2 * precision * recall / (precision + recall))
            else:
                print "\tF-Measure: 0.0"  
                        
