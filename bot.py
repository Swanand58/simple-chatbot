import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import numpy
import random
import json
import tensorflow as tf
import tflearn
import pickle 
import os 
import time
from app import *


with open("intents.json") as file: 
    data = json.load(file)

try:
    swanand.py
    with open("data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)

except:    
    words = []
    labels = []
    docs_x = []
    docs_y = []
 
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])

            if intent["tag"] not in labels:
                labels.append(intent["tag"])    


    words = [stemmer.stem(w.lower()) for w in words if w not in "?"] 
    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = []
    output = []
    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []

        wrds = [stemmer.stem(w) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)


    training = numpy.array(training)
    output = numpy.array(output)

    with open("data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f) 


tf.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation = "softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

#insert some random code in try to train the model if intents file updated
try:
    #model.load("model.tflearn")
    swanand.py
except:    
    model.fit(training, output, n_epoch = 500, batch_size = 8, show_metric = True)
    model.save("model.tflearn")

def word_list(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for sw in s_words:
        for i, w in enumerate(words):
            if w == sw:
                bag[i] = 1

    return numpy.array(bag)        


def chat():      #add text param for app.py
    print("Start Talking with the BOT !! press q to stop")
    while True:
        #inp = text
        inp = input("YOU :")
        if inp.lower() == "q":
            break
        
        results = model.predict([word_list(inp, words)])[0]
        results_index = numpy.argmax(results)
        tag = labels[results_index]
        
        
        if results[results_index] > 0.7:
            for tg in data["intents"]:
                if tg ['tag'] == tag:
                    responses = tg['responses']
            rc = random.choice(responses)
            print("BOT :",rc)
            #return rc
        else:
            print("I did'nt quite get that, try asking something else!")
            #incorrect_res = "I did'nt quite get that, try asking something else!"           
            #return incorrect_res

chat()
