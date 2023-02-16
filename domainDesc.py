import requests
from bs4 import BeautifulSoup
import numpy as np



def get_domainDesc(label):

    fn='struct_domain_Desc.txt'
    fw=open(fn,'a')

    url='http://smart.embl.de/smart/do_annotation.pl?DOMAIN='+label+'&BLAST=DUMMY'
    info=requests.get(url)
    sp=BeautifulSoup(info.text,'lxml')
    tab1 = sp.find('table',id='annoHead')
    tab2 = sp.find('table', id='domainDesc')

    '''
    for tr in tab1.findAll('tr'):
        print(tr.getText().replace(label,''))
    '''
    #print(label,end=',')


    for tr in tab2.findAll('tr'):
        for td in tr.findAll('td'):
            if "GO" in td.getText():
                fw.write(td.getText())
    fw.write('\n')
    

    '''
    st=sp.find('li',id='St')
    if st !=None:
        #print('yes')
        tr=st.findAll('tr')[0]
        print(tr.findAll('td')[0].getText())
    else:
        print('no')
    '''

if __name__ == '__main__':
    labels = np.loadtxt('struct_domains_label.dat', dtype='str')
    for i in labels:
        get_domainDesc(i)

    # get_consensus('seq_label.fasta')
    # get_fasta('seq_label_native.fasta')
    # print(len(labels))
    # fw.write(line)