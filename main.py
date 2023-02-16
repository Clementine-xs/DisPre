# This is a sample Python script.
import numpy as np
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from bs4 import BeautifulSoup
import re


def get_links_from(address):

    urls = []
    labels= []
    list_view = address
    wb_data = requests.get(list_view)
    soup = BeautifulSoup(wb_data.text,'html.parser')
    tables=soup.findAll('table')
    tab=tables[0]
    for tr in tab.findAll('tr'):
        for td in tr.findAll('td'):
            if len(td)!=0:
                urls.append(td.find('a')['href'])
                labels.append(td.getText())
    return(labels,urls)

def get_sequence(label):

    fn='seq_label_native_lost.fasta'
    fw=open(fn,'a')

    DATA={
        "NAME":label,
        #"SHOW_ALIGNMENT":"Family alignment in",
        #"FORMAT":"CHROMA"
        "DO_CONSENSUS":"Alignment consensus sequence",
        "FORMAT":"FASTA"
    }

    url='http://smart.embl.de/smart/show_info.pl'
    info=requests.post(url,DATA)
    sp=BeautifulSoup(info.text,'lxml')
    #seqs=sp.findAll('b')
    seqs=sp.findAll('pre')
    if seqs!=[]:
        fw.write('>'+label+'\n')
        for seq in seqs:
            fw.write(seq.getText())


def get_consensus(fn):
    file=open(fn)
    fw=open('consensus.fasta','w')
    for line in file:
        if line.startswith(">"):
            fw.write(line)
        elif "Consensus" in line:
            if len(line)>100:
                line=line.rstrip('\n')
                line=line.strip('Consensus/60%')
                line=line.strip()
                fw.write(line)

            else:
                line = line.strip('Consensus/60%')
                line = line.strip()
                fw.write(line+'\n\n')

def get_fasta(fn):
    file=open(fn)
    fw=open('native_seq.fasta','w')
    for line in file:
        if line.startswith(">"):
            fw.write('\n\n'+line)
        elif "CONSENSUS" not in line and ">" not in line:
            if len(line)>1:
                #line = line.strip().split(r'[ ]+',1)
                line=re.split(r"[ ]+",line.strip())
                s=line[1].replace('-','')
                s=s.replace('_','')
                s=s.replace('.','')
                s=s.strip()
                fw.write(s)


if __name__ == '__main__':
    #address = 'http://smart.embl.de/browse.shtml'
    #labels,urls=get_links_from(address)
    labels=np.loadtxt('lost_labels_native.dat',dtype='str')
    for i in labels:
        print(i)
        get_sequence(i)

    #get_consensus('seq_label.fasta')
    #get_fasta('seq_label_native.fasta')
    #print(len(labels))

    '''
    file=open('consensus.fasta')
    fw=open('consensus_strip_2.fasta','a')
    for line in file:
        if not line.startswith(">"):
            line=line.replace(" ","")
            line=line.replace(".","") #删除标注为任意残基的位点

            for n in range(line.count('-')):
                repl=random.sample(['D','E'],1)[0]
                line=line.replace("-",repl,n+1)

            for n in range(line.count('*')):
                repl=random.sample(['S','T'],1)[0]
                line=line.replace("*",repl,n+1)

            for n in range(line.count('l')):
                repl=random.sample(['I', 'L', 'V'],1)[0]
                line=line.replace("l",repl,n+1)

            for n in range(line.count('+')):
                repl=random.sample(['H', 'K', 'R'],1)[0]
                line=line.replace("+",repl,n+1)

            for n in range(line.count('t')):
                repl=random.sample(['A', 'G', 'S'],1)[0]
                line=line.replace("t",repl,n+1)

            for n in range(line.count('a')):
                repl=random.sample(['F', 'H', 'W', 'Y'],1)[0]
                line=line.replace("a",repl,n+1)

            for n in range(line.count('c')):
                repl=random.sample(['D', 'E', 'H', 'K', 'R'],1)[0]
                line=line.replace("c",repl,n+1)

            for n in range(line.count('s')):
                repl=random.sample(['A', 'C', 'D', 'G','N','P','S','T','V'],1)[0]
                line=line.replace("s",repl,n+1)

            for n in range(line.count('p')):
                repl=random.sample(['C', 'D', 'E', 'H', 'K','N','Q','R','S','T'],1)[0]
                line=line.replace("p",repl,n+1)

            for n in range(line.count('b')):
                repl=random.sample(['E','F','H','I','K','L','M','Q','R','W','Y'],1)[0]
                line=line.replace("b",repl,n+1)

            for n in range(line.count('h')):
                repl=random.sample(['A', 'C', 'F', 'G', 'H', 'I', 'L', 'M', 'T','V','W', 'Y'],1)[0]
                line=line.replace("h",repl,n+1)

        
        
            line=line.replace("-", random.sample(['D','E'],1)[0] )
            line=line.replace("*", random.sample(['S','T'],1)[0] )
            line = line.replace("l", random.sample(['I', 'L', 'V'], 1)[0])
            line = line.replace("+", random.sample(['H', 'K', 'R'], 1)[0])
            line = line.replace("t", random.sample(['A', 'G', 'S'], 1)[0])
            line = line.replace("a", random.sample(['F', 'H', 'W', 'Y'], 1)[0])
            line = line.replace("c", random.sample(['D', 'E', 'H', 'K', 'R'], 1)[0])
            line = line.replace("s", random.sample(['A', 'C', 'D', 'G','N','P','S','T','V'], 1)[0])
            line = line.replace("p", random.sample(['C', 'D', 'E', 'H', 'K','N','Q','R','S','T'], 1)[0])
            line = line.replace("b", random.sample(['E','F','H','I','K','L','M','Q','R','W','Y'],1)[0])
            line = line.replace("h", random.sample(['A', 'C', 'F', 'G', 'H', 'I', 'L', 'M', 'T','V','W', 'Y'], 1)[0])
        '''
        #fw.write(line)




