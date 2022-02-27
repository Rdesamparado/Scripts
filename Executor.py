import paramiko
import time

if __name__ == '__main__':
    sesh = paramiko.SSHClient()
    sesh.load_system_host_keys()
    sesh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sesh.connect('10.10.64.11',22,'rdesamparado','Tyler/34')
    channel = sesh.invoke_shell()
    time.sleep(1)
    channel.send('sudo -i\n')
    time.sleep(1)
    channel.send('Tyler/34\n')
    time.sleep(1)
    channel.send('py sshTools4.py 149235\n && testobject1.txt')
    time.sleep(2)    
    cmd = 'cat /root/fs/testobject1.txt'
    stdin, stdout, stderr = sesh.exec_command(cmd)
    output = stdout.read().decode('utf-8')
    #result=''.join(output)
    time.sleep(5)
    #for line in output:
     #  print (line.strip('\n'))
    #time.sleep(2)
    #output = channel.recv(9999).decode('utf-8')
    log = output.split()[0]
    log2 = output.split()[1]
    log3 = output.split()[6]
    print (str(log), str(log2), str(log3)) 
    print (log2)

