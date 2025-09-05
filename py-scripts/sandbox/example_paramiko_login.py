#!/usr/bin/env python3
"""
This is an example of how to promote a paramiko connection to a login shell environment.
Notice that the distinct difference is client.invoke_shell().
"""

import time
import paramiko
hostname = "lf0355-at7-7080.jbr.candelatech.com"


def main():
    print(f"Will connect to AT7 {hostname}")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    shell = None
    try:
        print(f"connecting to {hostname}...")
        client.connect(hostname=hostname,
                       port=22,
                       username="lanforge",
                       password="lanforge",
                       allow_agent=False,
                       look_for_keys=False)
        time.sleep(2)
        print("creating login shell...")
        shell = client.invoke_shell()
        time.sleep(1)
        shell.send("\nclear\npwd\n")
        time.sleep(0.2)
        sh_out = shell.recv(4096).decode('utf-8')
        print(f"\npwd returns: {sh_out}")

        shell.send("printenv\n")
        time.sleep(0.2)
        sh_out = shell.recv(4096).decode('utf-8')
        print(f"\nprintenv returns: {sh_out}")

        print("** If you see the VIRTUAL_ENV environment variable above, you are good!")
        shell.send("date\n")
        time.sleep(0.2)
        sh_out = shell.recv(4096).decode('utf-8')
        print(f"\ndate returns: {sh_out}")

    finally:
        if shell is not None:
            shell.close()
        if client:
            client.close()

if __name__ == '__main__':
    main()
