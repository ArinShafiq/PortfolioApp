# Portfolio App by Shafiq

## Setup with Docker
1. Clone the github repository into your Computer using ```git clone https://github.com/ArinShafiq/PortfolioApp```
2. Open a terminal in the directory of where the cloned app is stored.
3. Run the command ```docker-compose up --build```
4. Access the web app with your browser via localhost or 127.0.0.1:5000

## Setup Natively (With Python)
1. Ensure Python is installed in your computer using a terminal by running ```python --version```
2. If not installed, you can visit: https://www.python.org/downloads/
3. Clone the github repository into your Computer using ```git clone https://github.com/ArinShafiq/PortfolioApp```
4. Open a terminal in the directory of where the cloned app is stored.
5. Run the command ```pip install -r requirements.txt```
6. Afterwards you can run ```python app.py```
7. Access the web app with your browser via localhost or 127.0.0.1:5000.

## Setup Captcha
1. Go to https://www.google.com/recaptcha/admin
2. Press the + button on the page to create new recaptcha.
3. Insert the required data such as labels, domain names and type of reCaptcha. IMPORTANT: Choose reCaptcha V2.
4. Submit the form and you will then be given sitekey and secret key.
5. Insert the sitekey in contact.html inside this component ```<div class="g-recaptcha" data-sitekey="your-site-key"></div>```
6. Insert secret key in app.py inside this variable ```RECAPTCHA_SECRET_KEY = 'your-secret-key'```
7. If its running, stop and run the app again to apply the change.

## Setup Email
1. Before this, ensure your google account has 2FA enabled.
2. Go to https://myaccount.google.com/apppasswords to setup your app password.
3. After app password is created, copy it.
4. In app.py replace the strings in ```app.config['MAIL_USERNAME']``` with your sender email account.
5. Below it, replace the strings in ```app.config['MAIL_PASSWORD']``` with the app password you have copied.
6. in ```msg = Message(subject=msg_subject,
                      sender=sender_email,
                      recipients=['your-email'],
                      body=f"Name: {name}\nEmail: {sender_email}\nPhone: {phone_number}\n\nMessage:\n{message}")```
   replace the recipients with your receiver email address.
7. Save and restart app.py

