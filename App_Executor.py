import paramiko
import time
import sys

if __name__ == '__main__':
    len_argv = len(sys.argv)
    sesh = paramiko.SSHClient()
    sesh.load_system_host_keys()
    sesh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sesh.connect('10.10.64.11',22,'rdesamparado','Tyler/34')
    channel = sesh.invoke_shell()

    
    if len_argv == 2:
        cmd = sys.argv[1]
        print (cmd)
        time.sleep(1)
        action = ('python /home/chirag/fs_webtoolkit/{}\n'.format(cmd))
        print (action)
        channel.send(str(action))
        time.sleep(2)
        output = channel.recv(99999).decode('utf-8')
        print (output)
    elif len_argv ==3:
        cmd = sys.argv[1]
        cmd2 = sys.argv[2]
        action2 = ('python /home/chirag/fs_webtoolkit/{} {}\n'.format(cmd,cmd2))
        print (action2)
        channel.send(str(action2))
        time.sleep(2)
        output = channel.recv(99999).decode('utf-8')
        print (output)
    else:
        print ('not valid')

