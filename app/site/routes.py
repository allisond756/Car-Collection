from flask import Blueprint, render_template

site = Blueprint('site', __name__, template_folder = 'site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/account')
def account():
    return render_template('account.html')
