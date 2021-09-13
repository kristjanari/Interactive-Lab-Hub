
import time

class bcolors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

MESSAGE_WAIT = 2

def valid():
    print(f"{bcolors.OKGREEN}Eth: GPU1: ETH share found! \nEth: Share actual difficulty: 14.1 GH (!)\nEth: Share accepted in 7 ms{bcolors.ENDC}")
    time.sleep(MESSAGE_WAIT)

def invalid():
    print(f"{bcolors.FAIL}Eth: GPU1: ETH share invalid! \nEth: Share actual difficulty: 15.1 GH (!)\nEth: Share rejected in 5 ms{bcolors.ENDC}")
    time.sleep(MESSAGE_WAIT)

def stale():
    print(f"{bcolors.WARNING}Eth: GPU1: ETH share stale! \nEth: Share actual difficulty: 10.6 GH (!){bcolors.ENDC}")
    time.sleep(MESSAGE_WAIT)

def normal():
    print("Eth: New job #7a6b44n from ssl://eth-us-east.flexpool.io:5555; diff: 4000 MH")
    time.sleep(MESSAGE_WAIT)

def restart():
    print("RESTARTING.....")
    time.sleep(1)
    print('\n.')
    time.sleep(1)
    print('\n.')
    time.sleep(1)
    print('\n.')
    time.sleep(1)
    print('\n.')
    time.sleep(1)
    print('\n.')
    time.sleep(MESSAGE_WAIT)

if __name__ == '__main__':
    normal()
    normal()
    normal()
    normal()
    valid()
    normal()
    normal()
    normal()
    valid()
    normal()
    valid()
    normal()
    normal()
    valid()
    normal()
    valid()
    normal()
    normal()
    invalid()
    normal()
    normal()
    valid()
    normal()
    normal()
    normal()
    valid()
    normal()
    invalid()
    normal()
    normal()
    normal()
    invalid()
    normal()
    invalid()
    normal()
    normal()
    invalid()
    normal()
    invalid()
    normal()
    normal()
    normal()
    invalid()
    normal()
    invalid()
    restart()
    normal()
    normal()
    valid()
    normal()
    normal()
    normal()
    valid()
    normal()
    valid()
    normal()
    valid()
    normal()
    normal()
    valid()
