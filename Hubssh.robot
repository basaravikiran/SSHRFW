*** Settings ***
#Library     SSHLibrary
Library     LogfileAnalysis.py     192.168.56.102    root   None
Test Teardown   close ssh connection
*** Variables ***
${url}      192.168.56.102
${user}     root
${passwd}   ${None}

*** Test Cases ***

Connect SSH via LogfileAnalyzer
    syslog contains text messgaes   /var/log/messages   50   Input
