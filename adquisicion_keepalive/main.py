import sys
from Controller import *

def main():
    if(sys.argv[1] == 'RED_KEEPALIVE'):
        observer = KeepaliveObserver(sys.argv[1])
    print('corriendo')
    observer.channel.start_consuming()

if __name__ == "__main__":
    main()