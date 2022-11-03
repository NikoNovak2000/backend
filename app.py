from flask import Flask, jsonify, request
from pymongo import MongoClient
from extensions.extensions import mongo
from flask_cors import CORS

app = Flask (__name__)
app.config ['MONGO_URI'] = 'mongodb+srv://admin:123@cluster0.95hrdhh.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(app.config['MONGO_URI'])
db = client['itemFoodDb']
mongo.init_app(app)

CORS(app)

@app.route('/')
def index():
    return "hello"

if __name__ == "__main__":
    app.run(debug=True)

#get metoda za dohvacanje svih proizvoda
@app.route('/app/cart', methods=['GET'])
def data():
    allData = db['cart'].find()
    dataJson = []
    for data in allData:
        id = data['_id']
        name = data['name']
        price = data['price']
        img = data['img']
        quantity = data['quantity']
        category = data['category']
        dataDict = {
            'id': str(id),
            'name': name,
            'price': price,
            'img': img,
            'quantity': quantity,
            'category': category
        }
        dataJson.append(dataDict)
    print(dataJson)
    return jsonify(dataJson)

#post metoda za dodavanje prozivoda u kosaricu(cart)
@app.route('/app/cart/dodaj', methods=['POST'])
def adddata():
        body = request.get_json()
        print(body)
        name = body.get('name')
        price = body.get('price')
        img = body.get('img')
        quantity = body.get('quantity')
        category = body.get('category')

        db['cart'].insert_one({
            'name': name,
            'price': price,
            'img': img,
            'quantity': quantity,
            'category': category
        })
        return jsonify({
            'status': 'Data posted to MongoDB!',
        })

#get metoda za dohvacanje svih prozivoda u kosarici
@app.route('/items', methods=['GET'])
def data2():
    allData = db['itemFood'].find()
    dataJson = []
    for data in allData:
        id = data['_id']
        name = data['name']
        price = data['price']
        img = data['img']
        quantity = data['quantity']
        category = data['category']
        dataDict = {
            'id': str(id),
            'name': name,
            'price': price,
            'img': img,
            'quantity': quantity,
            'category': category
        }
        dataJson.append(dataDict)
    print(dataJson)
    return jsonify(dataJson)


#delete metoda za micanje proizvoda van kosarice
#@app.route('/app/cart/delete', methods=['DELETE'])
#def adddata2():