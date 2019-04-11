# DeepSUMO
DeepSUMO uses a convolutional neural network to predit lysine SUMOylation sites. Users can run program with specified protein sequences.

# Installation
* Install [Python 3.5](https://www.python.org/downloads/) in Linux and Windows.
* Because the program is written in Python 3.5, python 3.5 with the pip tool must be installed first. DeepSUMO uses the following dependencies: numpy, pandas, scipy, keras and tensorflow. You can install these packages first, by the following commands:
```
pip install numpy
pip install pandas
pip install scipy
pip install -v keras==2.2.2
pip install tensorflow==1.50
```
* If you have run above commands in Linux for the first time, you can run the following command:
```
sudo apt install python3-pip
```
After that, users can change the commands into:
```
pip3 install numpy
pip3 install pandas
pip3 install scipy
pip3 install -v keras==2.2.2
pip3 install tensorflow==1.50
```

# Running DeepSUMO
open cmd in Windows or terminal in Linux, then cd to the DeepSUMO-master/codes folder which contains predict.py
</br>**For general DeepSUMO site prediction using our model, run:**
</br>`python predict.py -input [custom predicting data in txt format] -threshold [threshold value] -output [ predicting results in csv format]`  
</br>**Example:**
</br>`python predict.py -input ../codes/example.txt -threshold 0.5 -output ../codes/results.csv`
</br>-output is optional parameter, while -input and -threshold are required parameters. Prediction results will show in the cmd or terminal, and if you don't want to save results, you need not input -output.

</br>**Example:**
</br>`python predict.py -input ../codes/example.txt -threshold 0.5`

</br>**For details of -input,-threshold and -output, run:**
</br>`python predict.py -h`


# Announcements
* In order to obtain the prediction results, please save the query protein sequences and protein name in txt format. Users can refer to the example.txt under the codes folder. Also of note, each protein name should be added by '>', otherwise the program will occur error.
* The accepted amino acids are: A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y, and a virtual amino acid O. If the protein fragments contain other amino acids, the program only will predict fragments which contain above-mentioned 21 amino acids. 
* To save the prediction results, the -ouput should be in csv format.
