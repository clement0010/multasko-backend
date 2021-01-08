from app import app, cross_origin, json, jsonify, os, request, db
from app.models import Memo, Category
from sqlalchemy import desc, func
from random import randrange
import datetime

@app.route('/', methods=['GET'])
@cross_origin()
def index():
    return 'Index route works!'

@app.route('/populate', methods=['POST'])
@cross_origin()
def populate():
    data = request.get_json()

    objects = []
    for i in data:
        objects.append(Memo(text=i['text'], priority_level=randrange(3), date_posted=datetime.datetime.fromisoformat(i['date_posted']), text_type=i['text_type']))

    db.session.add_all(objects)
    db.session.commit()

    return jsonify([r.serialize for r in objects])


@app.route('/api/memo', methods=['GET','POST','DELETE', 'PUT'])
@cross_origin()
def memo_api():
    method = request.method

    if method == 'GET':
        if request.args:
            if request.args.get('category'):
                category_id = request.args.get('category')
                memos = Memo.query.filter_by(category_id=category_id).order_by(desc(Memo.date_posted)).all()

                response = jsonify(json_list=[memo.serialize for memo in memos])
                return response

            elif request.args.get('text-type'):
                text_type = request.args.get('text-type')
                memos = Memo.query.filter_by(text_type=text_type).order_by(desc(Memo.date_posted)).all()

                response = jsonify(json_list=[memo.serialize for memo in memos])
                return response

        else:
            memos = Memo.query.order_by(desc(Memo.date_posted)).all()

            response = jsonify(memos=[memo.serialize for memo in memos])
            return response

    elif method == 'POST':
        data = request.get_json()

        memo = Memo(text=data['text'], priority_level=data['priority_level'])
        db.session.add(memo)
        db.session.commit()
        
        return jsonify(memo.serialize)

    elif method == 'PUT':
        if request.args:
            id = request.args.get('id')
            data = request.get_json()

            status = Memo.query.filter_by(id=id).update(data)

            db.session.commit()
            return jsonify(rows_affected=status)
        else:
            raise InvalidUsage('Please specify your parameters', status_code=500)

    elif method == 'DELETE':
        if request.args:
            id = request.args.get('id')
            status = Memo.query.filter_by(id=id).delete()

            db.session.commit()
            return jsonify(rows_affected=status)
        else:
            raise InvalidUsage('Please specify your parameters', status_code=500)

    else:
        raise InvalidUsage('No such method', status_code=500)

    # with open('./result.json',encoding='UTF8') as json_file:
    #     data = json.load(json_file)
    #     # ML integration goes in here
    # # ML Controller insert here
    # return jsonify(data)

@app.route('/api/category', methods=['GET','POST', 'DELETE', 'PUT'])
@cross_origin()
def category_api():
    method = request.method

    if method == 'GET':
        categories = Category.query.all()

        response = jsonify(categories=[category.serialize for category in categories])
        return response

    elif method == 'POST':
        data = request.get_json()

        objects = []
        for i in data:
            objects.append(Category(name=i['name']))

        db.session.add_all(objects)
        db.session.commit()

        return jsonify([r.serialize for r in objects])

    elif method == 'DELETE':
        if request.args:
            id = request.args.get('id')
            status = Category.query.filter_by(id=id).delete()

            db.session.commit()
            return jsonify(rows_affected=status)
        else:
            raise InvalidUsage('Please specify your parameters', status_code=500)

    elif method == 'PUT':
        if request.args:
            id = request.args.get('id')
            data = request.get_json()

            status = Category.query.filter_by(id=id).update(data)

            db.session.commit()
            return jsonify(rows_affected=status)
        else:
            raise InvalidUsage('Please specify your parameters', status_code=500)

    else:
        raise InvalidUsage('No such method!', status_code=500)
        

    # with open('./result.json',encoding='UTF8') as json_file:
    #     data = json.load(json_file)
    #     # ML integration goes in here
    # # ML Controller insert here
    # return jsonify(data)

class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
