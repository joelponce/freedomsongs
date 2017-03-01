from project import app
import os

if os.environ.get('ENV') == 'production':
    debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
else:
    debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/freedomsongs-db'

if __name__ == '__main__':
    app.run(port=5000, debug=debug)
