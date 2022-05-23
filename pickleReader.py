import pickle

unpickleFile = open('classes.pkl', 'rb')
var= pickle.load(unpickleFile,encoding='latin1')

print(var)