def sshCmd(server,port,user,pswd,cmd):
	import paramiko
	paramiko.util.log_to_file("sshParamiko.log")  
	ssh = paramiko.SSHClient()
	ssh.connect(server,,port=port, username=user, password=pswd)
	ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd)
	print stdout.read()  
	s.close()

def main():
	host="10.27.2.33"
	port=22
	username="ansys"
	paswd="run208&209"
	execmd="/opta/abaqus611/Command/abaqus job=2017-02-22 cpu=20 scratch=./"	
	sshCmd(host,port,username,paswd,execcmd)
if __name__=="__main__":
	main()
