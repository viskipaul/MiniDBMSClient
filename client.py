import requests

def run_client():
    cmd = ""
    while cmd != 'q':
        cmd = input('> ')
        if cmd != "":
            r = requests.get('http://192.168.1.237:5000/default?command=' + cmd)
            print(r.text)

if __name__=='__main__':
    run_client()