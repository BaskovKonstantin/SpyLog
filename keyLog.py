from pynput.keyboard import Key, Listener


def show(key):

    print(key)



# Collect all event until released
with Listener(on_press=show) as listener:
    listener.join()