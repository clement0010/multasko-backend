from app import app, cross_origin, json, jsonify, os, request, db
from app.models import Memo, Category
from sqlalchemy import desc

@app.route('/', methods=['GET'])
@cross_origin()
def index():
    return 'Index route works!'

@app.route('/api', methods=['GET','POST'])
@cross_origin()
def api():
    method = request.method

    if method == 'GET':
        memos = Memo.query.order_by(desc(Memo.date_posted)).all()

        response = jsonify(json_list=[memo.serialize for memo in memos])
        return response

    elif method == 'POST':
        data = request.get_json()

        memo = Memo(text=data['text'])
        db.session.add(memo)
        db.session.commit()
        
        return jsonify(memo.serialize)

    else:
        return jsonify('Nothing to get')

    # with open('./result.json',encoding='UTF8') as json_file:
    #     data = json.load(json_file)
    #     # ML integration goes in here
    # # ML Controller insert here
    # return jsonify(data)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
