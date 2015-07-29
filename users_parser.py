"""
Print all the users and their login shells
"""

import pwd

# Get the users from /etc/passwd


def getusers():
    users = pwd.getpwall()
    for user in users:
        print('{0}:{1}'.format(user.pw_name, user.pw_shell))

if __name__ == '__main__':
    getusers()
