import subprocess
import re
from subprocess import Popen, PIPE
import os,sys,re

def get_space():
    ret = subprocess.run("df -h",shell=True, stdout=subprocess.PIPE)
    space_free=ret.stdout.decode("utf-8")
    space_free=re.findall(r"\d+\%", space_free)[0]
    space_free=int(space_free.split("%")[0])
    print("1")
    return space_free

''' 获取 ifconfig 命令的输出 '''
def getIfconfig():
    # p = Popen(['ifconfig'], stdout = PIPE)
    p = Popen(['/sbin/ifconfig'], stdout = PIPE)
    getIf_data = p.stdout.read().decode()
    print("2")
    return getIf_data


''' 获取 dmidecode 命令的输出 '''
def getDmi():
    p = Popen(['dmidecode'], stdout = PIPE)
    data = p.stdout.read().decode()
    print("3")
    # print(data)
    return data


''' 根据输入的段落数据分析出ifconfig的每个网卡ip信息 '''
def parseIfconfig(parsed_data):
    parsed_data = [i for i in parsed_data.split("\n")]
    host_ip = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', parsed_data[1])
    #  print(host_ip)
    print("4")
    return host_ip

''' 获取linux系统主机名称'''
def getHostname():
    with open('/etc/sysconfig/network') as fd:
        fd = [i.strip() for i in fd]
        fd = fd[-1]
        fd = re.findall(r"HOSTNAME=(.*)", fd)
        print("5")
    # print(fd[0])
        return fd[0]

''' 获取CPU的型号和CPU的核心数'''
def getCpu():
# meminfo 后面不能加/ 否则报错
    with open('/proc/meminfo') as fd:
        fd = [i.strip() for i in fd][0]
        fd = re.findall(r'MemTotal:(.*) kB', fd)
        fd = int(fd[0].strip())
        mem = str('%.f' % (fd / 1024.0)) + ' MB'
        print("6")
        return mem


if __name__ == '__main__':
    use_space=get_space()
    # print(use_space)
    # dic = {}
    data_ip = getIfconfig()
    parsed_data_ip = parseIfconfig(data_ip)
    Memorys = getCpu()
    hostnames = getHostname()
    print('\033[1;31m')
    print(use_space)
    print("IP  : %s,   BCAST  : %s,  MASK   :%s"%(parsed_data_ip[0], parsed_data_ip[1],parsed_data_ip[2] ))
    print("Memory : %s"%Memorys)
    print("hostname: %s"%hostnames)
    print("\033[0m")
