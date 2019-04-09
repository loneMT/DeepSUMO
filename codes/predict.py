import argparse
import sys
import pandas as pd
import numpy as np
from get_frag import extract_predict
from detection import detect
from keras.models import load_model


###### one-of-k coding ######
def onehot_encode(frag):
    num = int(len(frag)/2)
    AAs = 'ACDEFGHIKLMNPQRSTVWYO'
    BE=[]
    for i in range(num):
        replace=[]
        for j in range(33):
            Binstr=[0.]*21
            pos=AAs.index(frag[2*i+1][j])
            Binstr[pos]=1.
            replace.extend(Binstr)
        BE.append(replace)
    binary=np.array(BE)
    test_images = binary.reshape((num,33,21)) /255
    test_images = test_images.astype('float32')
    return test_images

###### main function ######
def main():
    parser=argparse.ArgumentParser(description='DeepSUMO: a deep learning framework for the prediction of lysine SUMOylation sites.')
    parser.add_argument('-input',  dest='inputfile', type=str, help='Query protein sequences to be predicted in txt format.', required=True)
    parser.add_argument('-threshold', dest='threshold_value', type=float, help='Please input a value between 0 and 1', required=True)
    parser.add_argument('-output',  dest='outputfile', type=str, help='Saving the prediction results in csv format.',required=False)
    args = parser.parse_args()
    inputfile = args.inputfile;
    threshold = args.threshold_value;
    outputfile = args.outputfile;
    inputfile = 'example.txt'
    print('Sequence fragment are loading...')
    

    frag = extract_predict(inputfile, size_windows=33)
    right_frag,wrong_frag = detect(frag)
    print('Features are extracting...')
    data = onehot_encode(right_frag)
    
    print('Loading model...')
    model = load_model('bestmodel.h5')
    prediction = model.predict(data)
    n = int(len(right_frag)/2)
    m = int(len(wrong_frag)/2)
    Fragments_name = []
    Sequence = []
    Probability = []
    print('DeepSUMO sites were predicted as follows.')
    print('-------------------------------')
    for i in range(n):
        if prediction[i][1] > threshold:
            Fragments_name.append(right_frag[2*i])
            Sequence.append(right_frag[2*i+1])
            print(right_frag[2*i])
            print(right_frag[2*i+1])
            var = '%.11f' % prediction[i][1]
            Probability.append(var)
            print('probability value:'+str(var))
            print('-------------------------------')
            
    if wrong_frag!=[]:   
        print('The following sequence fragment contains other amino acids.')
        print('The accepted amino acids are:A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W,Y and a virtual amino acid O.')
        print('-------------------------------')
        for j in range(m):
            print(wrong_frag[2*j])
            print(wrong_frag[2*j+1])
            print('-------------------------------')
    
    AA = {'a':Fragments_name,'b':Sequence,'c':Probability}
    DeepSUMO = pd.DataFrame(AA)
    DeepSUMO.to_csv(outputfile,index=False,header=['Fragments name','Sequence','Probability value'])
            
if __name__ == "__main__":
    main()   