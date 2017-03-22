from app import app
import os
"""
    this script is to run the application
"""
if os.environ.get('HEROKU') is None:
    app.run(host='0.0.0.0', debug=True)
else:
    app.run(debug=True, port=5000)
