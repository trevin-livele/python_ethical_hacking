from pynput import keyboard

def get_key_name(key):
if isinstance(key,keyboard.keyCode):
  return key.char
  else
  return str(key)

def on_press(key) :
key_name = get_key_name(key)
print("key {} pressed" .format (key) )
print("key type: {}".format(key._class_._name_))

def on_release (key) :
key_name = get_key_name(key))
print ("key {} released" .format (key_name) )
if str(key) == 'key.esc':
print("Existing...")
return False

with keyboard.Listener(
 on_press = on_press,
 on_release = on_release) as listener:
 listener.join()