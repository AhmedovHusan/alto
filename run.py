from general import app
from general import db

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
