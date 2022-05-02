import os

from flask import Flask,jsonify,request

Debug = False

app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/predict",methods=['POST'])
def load_mod():
    with open(f'phish-model-1649995335.cloudpickle', 'wb') as f:
        model = pickle.load(f)
    return model

def url_mod(urls):
  new_url = []
  final_url = []
  for i in url_list:
      if i.contains('^.*[^/]/')
      new_url.append(i.split('/',n=0).str[1].fillna(""))
  for i in new_url:
      new_str = i.split('.')
      if new_str[-1] == '.*':
          fnal_url.append(i.append('/'))
 return load_mod().predict(new_url)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))



if __name__ == '__main__':
    app.run()
