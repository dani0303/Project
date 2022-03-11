from flask import Flask, redirect, url_for, render_template
from forms import UserForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password'

@app.route("/", methods=['GET', 'POST'])
def home():
	forms = UserForm()
	if forms.validate_on_submit():
		return render_template('image.html')
	return render_template('index.html', forms=forms)


if __name__ == "__main__":
	app.run(debug=True)
