import string
import joblib

cv = joblib.load('./models/cv.pkl')
modelLoad = joblib.load('./models/model.pkl')

# string.punctuation- !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
def punctuation_removal(text):
    all_list = [char for char in text if char not in string.punctuation] # List of strings- ['r','i','c','h',..]
    clean_str = ''.join(all_list)
    return clean_str


def testing(text):
    punctuation_removal(text)
    new_text = cv.transform(text)   
    y_pred = modelLoad.predict(new_text)
    
    return y_pred
    