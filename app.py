from flask import Flask, render_template, request, redirect, flash, send_from_directory
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = '86b671517fe72e222216f30d17955b7a617959814ea34fb8ab0f10cbb14427ab'

#Flask mail config
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email'
app.config['MAIL_PASSWORD'] = 'your-app-password' 

mail = Mail(app)

#App route
@app.route('/', methods=['GET', 'POST'])
def homepage():
    
    #To send contact message to my email
    if request.method == 'POST':
        name = request.form['name']
        sender_email = request.form['email']
        phone_number = request.form['phone']
        msg_subject = request.form['subject']
        message = request.form['message']

        msg = Message(subject=msg_subject,
                      sender=sender_email,
                      recipients=['receiver-email'],
                      body=f"Name: {name}\nEmail: {sender_email}\nPhone: {phone_number}\n\nMessage:\n{message}")

        mail.send(msg)
        flash('Message sent successfully!', 'success')
        return redirect('/')
    
    return render_template('index.html')

#for download
@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory('static/docs', filename, as_attachment=True)

#Main
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
