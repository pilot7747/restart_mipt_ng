import sys
import platform
import subprocess
import time

def ping(host):
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '1', host]
    return subprocess.call(command) == 0


def check_mipt_ng():
    result = subprocess.run(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport', '-I'], stdout=subprocess.PIPE)
    return 'mipt-ng' in result.stdout.decode('utf-8')

def turn_off():
    result = subprocess.run(['networksetup', '-setairportpower', 'Wi-Fi', 'off'], stdout=subprocess.PIPE)

def turn_on():
    result = subprocess.run(['networksetup', '-setairportpower', 'Wi-Fi', 'on'], stdout=subprocess.PIPE)

if __name__ == '__main__':
    while True:
        if check_mipt_ng():
            if not ping('8.8.8.8'):
                turn_off()
                time.sleep(2)
                turn_on()
        time.sleep(5)
