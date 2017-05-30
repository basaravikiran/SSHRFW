import paramiko
import threading
import os.path
import subprocess
import time
import sys
import re

def Log_into_device(url,user,passwd):

    # Logging into device
    session = paramiko.SSHClient()

    # For testing purposes, this allows auto-accepting unknown host keys
    # Do not use in production! The default would be RejectPolicy
    session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the device using username and password
    session.connect(url, username=user, password=passwd)
