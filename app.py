from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary storage (for demo purposes only, not suitable for production)
users = []

@app.route('/')
def home():
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        event = request.form['event']

        user = {
            'name': name,
            'email': email,
            'event': event
        }

        users.append(user)

        return f"Registration Successful for {name}!"

    return render_template('register.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)