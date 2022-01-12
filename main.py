import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
s = requests.Session()

@app.route('/image-api')
def get_img():
     sku = request.args.get('sku').upper()
     img_list = s.get(f'https://restocks.net/shop/search?q={sku}&page=1&filters[][range][price][gte]=1').json()['data']
     if len(img_list) > 1:
          return jsonify({'img': 'error'})
     else:
          img = img_list[0]['image']
          return jsonify({'img': img})

if __name__ == '__main__':
     app.run()