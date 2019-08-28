# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 21:39:38 2019

@author: DELL
"""

#!/usr/bin/env python

#从fasta提取满足需求的数百条序列（根据序列名提取文件）
#读取文件，fasta文件可以直接用biopython读取，另一个文件可作为一个列表进行读取

import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser()
parser.add_argument('--input', '-i', help='input your fasta file')
parser.add_argument('--query', '-q', help='input your query file')
parser.add_argument('--output', '-o', help = 'output file')
args = parser.parse_args()

#first version
fas_file = SeqIO.index(args.input,'fasta')
out_handler = open(args.output, 'w')
with open(args.query,'r') as query: 
    #There is a newline character(\n) in every line, \
    #so it must be striped when map to the fasta file
    for name in query:
        name = name.strip()
        if name in fas_file.keys():
            seq = str(fas_file[name].seq)
            out_handler.write('>' + name + '\t' + seq + '\n')
        else:
            print ("%s is not in this file" % name)

out_handler.close()
query.close()       

#simplified version 1, a negative example for write output file
fas_file = SeqIO.index(args.input,'fasta')
query = open(args.query,'r')
for name in query:
    open(args.output, 'w').write('>' + name.strip() + '\n' +str(fas_file[name.strip()].seq) + '\n')
    #not open file in cycle, this will increase the burden of computer
    #for example, 100 cycles will open the output file 100 times
query.close()
    
#simplified version 2
fas_file = SeqIO.index(args.input,'fasta')
out_handler = open(args.output, 'w')
query = open(args.query, 'r')
for name in query:
    name = name.strip()
    out_handler.write('>' + name + '\n' + str(fas_file[name].seq) + '\n')
out_handler.close()
query.close()