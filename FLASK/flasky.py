import os
from app import create_app, db
from app.models import User, Role, Permission, Post, Follow
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db,  User=User, Role=Role, Post=Post)

@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5010)
