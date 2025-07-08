import requests
from flask import Flask, render_template, request, redirect, flash, send_from_directory
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = '86b671517fe72e222216f30d17955b7a617959814ea34fb8ab0f10cbb14427ab'

#Flask mail config
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-sender-email'
app.config['MAIL_PASSWORD'] = 'your-app-password' 

mail = Mail(app)

RECAPTCHA_SECRET_KEY = 'your-recaptcha-secret-key'

#Verify recaptcha
def verify_recaptcha(token):
    response = requests.post(
        "https://www.google.com/recaptcha/api/siteverify",
        data={
            'secret': RECAPTCHA_SECRET_KEY,
            'response': token
        }
    )
    result = response.json()
    print("reCAPTCHA result:", result)  # For debugging
    return result.get('success', False)

#App route
@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/Resume')
def resumePage():
    return render_template('resume.html')

@app.route('/Portfolio')
def PortfolioPage():
    return render_template('portfolio.html')

@app.route('/Contact', methods=['GET', 'POST'])
def ContactPage():
     #To send contact message to my email
    if request.method == 'POST':
        token = request.form.get('g-recaptcha-response')
        if not token or not verify_recaptcha(token):
            flash("reCAPTCHA failed. Try again.", "danger")
            return redirect("/Contact")
            
        name = request.form['name']
        sender_email = request.form['email']
        phone_number = request.form['phone']
        msg_subject = request.form['subject']
        message = request.form['message']

        msg = Message(subject=msg_subject,
                      sender=sender_email,
                      recipients=['your-receiver-email'],
                      body=f"Name: {name}\nEmail: {sender_email}\nPhone: {phone_number}\n\nMessage:\n{message}")

        mail.send(msg)
        flash('Message sent successfully!', 'success')
        return redirect('/Contact')
    
    return render_template('contact.html')

#for download
@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory('static/docs', filename, as_attachment=True)

#Main
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
