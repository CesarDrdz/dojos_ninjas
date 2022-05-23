from flask import Flask, session, flash
from flask_bcrypt import Bcrypt
import re
app = Flask(__name__)


app.secret_key = "asdfasdf a sdfasd fadsfasdfasdf"

bcrypt = Bcrypt(app)