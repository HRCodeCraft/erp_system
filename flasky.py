import datetime
import os
import click
import re
from flask import current_app




from sqlalchemy import and_, func
from app import create_app, db

from datetime import date



app = create_app(os.getenv('FLASK_CONFIG') or 'default')



@app.shell_context_processor
def make_shell_context():
    return dict(db=db)

 
@app.cli.command()
@click.argument('test_names', nargs=-1)
def test(test_names):
    """Run the unit tests."""
    import unittest
    if test_names:
        tests = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

