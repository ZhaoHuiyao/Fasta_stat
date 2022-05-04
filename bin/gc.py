#!/usr/bin/python3            #python的位置
#一个计算fasta文件的GC含量的python脚本
import argparse               #导入模块
import re
import os
import sys
import time

#将在该脚本帮助文档中显示，该python脚本撰写人和邮件
__author__='zhao huiyao'
__mail__= 'zhaohuiyao@snnu.edu.cn'


pat1=re.compile('^\s+$')    #空白行
#__file__；表示gc.py脚本文件
file_name = os.path.basename(__file__)      #python脚本文件名字

def std( level, message ):
    now_time = time.strftime("%Y-%m-%d %H:%M:%S")
    string = '{0} - {1} - {2} - {3}\n'.format( now_time, file_name, level, message )    #string格式：时间-python脚本名字（这里是gc.py）-ERROR/INFO-输入文件存在
    if level == 'ERROR':
        sys.stderr.write( string )
    else :
        sys.stdout.write( string )


def file_exists( file_or_dir ) :
    target = os.path.abspath( file_or_dir )
    if not os.path.exists( target ) :
        std( 'ERROR', '{0} is not exists , program EXIT'.format( target ) )
        sys.exit(0)
    else :
        std( 'INFO', '{0} is exists'.format( target) )
        return target

#我的习惯，定义主函数main()，当然你也可以直接使用
def main():
    parser=argparse.ArgumentParser(description='GC content of fasta file',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog='author:\t{0}\nmail:\t{1}'.format(__author__,__mail__))
    parser.add_argument('-i','--input',help='input a fa file',type=argparse.FileType('r'),dest='input',required=True)
    parser.add_argument('-o','--output',help='output dirtory',dest='output',required=True)
    args=parser.parse_args()
    

    fastaname = os.path.splitext(os.path.basename(sys.argv[2]))[0];gc_out = os.path.join(sys.argv[4], fastaname + '_gc.txt')
    fastadir = os.path.abspath(sys.argv[2])
    print ('fasta file: ', fastadir)
    file_exists(fastadir)
    gc_dict = {}        #定义一个字典。序列名对应两个值：GC个数和序列长度
    for line in args.input :
        if re.match(pat1, line) : continue      #如果是空白行，则跳出循环
        line = line.rstrip()
        if line.startswith('>') :
            name = line.replace('>', '')
            gc_dict[name] = [0, 0]
        else :
            nG = line.count('g')+line.count('G')
            nC = line.count('c')+line.count('C')
            nGC = nG + nC
            length = len(line)
            gc_dict[name][0] += nGC         #输入的fasta文件可以是多行，也可以是单行
            gc_dict[name][1] += length
    total_GC, total_length = 0, 0
    for i in gc_dict :
        total_GC += gc_dict[i][0]
        total_length += gc_dict[i][1]
    ratio = total_GC/total_length
    print ('GC_content ', ratio)
    with open(gc_out, 'w') as gc:
        gc.write("GC_content\t{0}\n".format( ratio))

#调用主函数
if __name__ == '__main__':
    main()
