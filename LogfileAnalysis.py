from SSHLibrary.library import SSHLibrary
from robot.api  import logger


class LogfileAnalysis(SSHLibrary):
    def __init__(self,url,login,passwd):
        super(LogfileAnalysis, self).__init__()
        self.open_connection(url)
        self.login(login,passwd)
    def syslog_contains_text_messgaes(self,log_file_path,tail,messages):
        cmd='tail -'+str(tail)+' '+log_file_path
        self.start_command(cmd)
        output=self.read_command_output()
        logger.console(output)
    def close_ssh_connection(self):
        self.close_connection()



if __name__=='__main__':
    handler=LogfileAnalysis('192.168.56.102','root',None)
    handler.syslog_contains_text_messgaes('/var/log/messages','50','Input')
    handler.close_ssh_connection()
