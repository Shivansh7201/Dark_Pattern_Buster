from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
model=pickle.load(open('models/dark_pattern_identifier.pkl','rb'))

@app.route('/', methods=['POST', 'GET'])
def home():
    return "Welcome! to Dark Pattern Bluster API."

@app.route('/predict/<src_code>', methods=['GET'])
def predict(menu):
    pass
#   text_nodes=webscrapper(src_code)
#     ouput=model.predict(text_nodes)
#     return jsonify(ouput)




if __name__ == '__main__':
    app.run()
