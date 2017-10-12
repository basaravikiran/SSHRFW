from SSHLibrary.library import SSHLibrary
from robot.api  import logger
from robot.libraries.BuiltIn import BuiltIn


class LogfileAnalysis(SSHLibrary):
    def __init__(self,url,login,passwd):
        super(LogfileAnalysis, self).__init__()
        print type(self)
        self.open_connection(url)
        self.login(login,passwd)

    def syslog_contains_text_message(self,log_file_path,tail,message):
        cmd='tail -'+str(tail)+' '+log_file_path
        self.start_command(cmd)
        output=self.read_command_output()
        logger.console(output)
        BuiltIn().should_contain(output,message)

    def syslog_match_regex(self,log_file_path,tail,regex):
        cmd='tail -'+str(tail)+' '+log_file_path
        self.start_command(cmd)
        output=self.read_command_output()
        logger.console(output)
        logger.console(regex)
        BuiltIn().should_match_regexp(output,regex)



    def close_ssh_connection(self):
        self.close_connection()



if __name__=='__main__':
    handler=LogfileAnalysis('192.168.56.101','root',None)
    handler.syslog_contains_text_message('/logs/syslog','50','data 641')
    handler.syslog_match_regex('/logs/syslog', '50', 'data\s[0-9][0-9][0-9]')
    handler.close_ssh_connection()
