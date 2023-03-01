from flask import Flask, render_template, request

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# About Us page
@app.route('/about')
def about():
    return render_template('about.html')

# Contact page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle form submission
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Send email or save to database
        return "Thanks for your message, we'll be in touch soon!"
    else:
        return render_template('contact.html')

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login form submission
        username = request.form['username']
        password = request.form['password']
        # Validate username and password
        if username == 'admin' and password == 'password':
            return "Login successful!"
        else:
            return "Invalid username or password."
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
