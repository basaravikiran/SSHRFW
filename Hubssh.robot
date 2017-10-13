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
    #While verifying log file with regex place the text part to be
    #verified in regex as it is ,substitute .* for unwanted text
    #and place meta characters that apperas in log file in []
    # for example the below text verification needs []() to be enclosed in []
    #or escaped using \\

    #Verify string in syslog "data 376 - -  0#6#[main] ReqQueue.hpp(56): Requestor"
    syslog match regex          /logs/syslog   50
    ...   data [\\w][\\w][\\w] - -\\s\\s0#6#[[]main[]] ReqQueue.hpp[(]56[)]: Requestor
    syslog match regex          /logs/syslog   50
    ...    data.*[[].*[]] ReqQueue.hpp[(].*[)].*Requestor
    syslog match regex          /logs/syslog   50
    ...    data.*\\[.*\\] ReqQueue.hpp\\(.*\\).*Requestor

