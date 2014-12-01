from flask import Flask

app = Flask(__name__)

@app.route('/meetupnow/api/meetup/new', methods=['POST'])
def create_new_meetup():
    pass

@app.route('/meetupnow/api/meetup/create/<int:meetup_id>', methods=['PUT'])
def join_meetup():
    pass

@app.route('/meetupnow/api/meetup/retrieve/<int:meetup_id>', methods=['GET'])
def get_meetup():
    pass

@app.route('/meetupnow/api/meetup/all', methods=['GET'])
def get_all_meetups():
    pass

@app.route('/meetupnow/api/meetup/delete/<int:meetup_id>', methods=['DELETE'])
def delete_meetup():
    pass

@app.route('/meetupnow/api/user/create', methods=['POST'])
def delete_meetup():
    pass


