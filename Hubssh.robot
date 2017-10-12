*** Settings ***
Library     SSHLibrary
Library     LogfileAnalysis     192.168.56.101    root   None
Test Teardown   close ssh connection
#Library     UserSSHLibrary.py
*** Variables ***
${url}      192.168.56.101
${user}     root
${passwd}   ${None}

*** Test Cases ***

#Connect SSH via LogfileAnalyzer
#    syslog contains text messgaes   /var/log/messages   50   Input

Test Call
    #syslog contains text message   /logs/syslog   50    Input
    syslog match regex          /logs/syslog   50
    ...   data 641 - -\\s\\s0#6#[[]main[]] ReqQueue.hpp[(]56[)]: Requestor
