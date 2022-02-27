import paramiko
import time

if __name__ == '__main__':
    sesh = paramiko.SSHClient()
    sesh.load_system_host_keys()
    sesh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sesh.connect('10.10.64.11',22,'rdesamparado','Tyler/34')
    channel = sesh.invoke_shell()
    time.sleep(1)
    channel.send('python /home/chirag/fs_webtoolkit/get_all_projects.py\n')
    time.sleep(2)    
    output = channel.recv(9999).decode('utf-8')
    print (output)

