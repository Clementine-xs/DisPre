import requests
from bs4 import BeautifulSoup
import numpy as np
import os

global out_dir

out_dir='result_native_AA'

def get_disorder(index,label,url):
    print("Processing : "+index+'\t'+label)
    result=[]
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'html.parser')
    tables = soup.findAll('table')
    tab = tables[1]
    for tr in tab.findAll('tr'):
        for td in tr.findAll('td'):
            for span in td.findAll('span'):
                if len(span) != 0 :
                    s=span['onmouseover']
                    s=s.replace('vconf(','')
                    s=s.replace("'","")
                    s=s.replace(");","")
                    result.append(s.split(','))
    result=np.array(result)

    outfile = os.path.join(out_dir, str(index).zfill(4)+'_'+label + '_result.csv')
    np.savetxt(outfile, result, delimiter=',', fmt='%s')
    #return (result)


if __name__ == '__main__':

    if not os.path.exists(out_dir):
        os.mkdir(out_dir)

    urls=np.loadtxt('dis_urls_native_lost.txt',dtype='str',delimiter='\t')
    [ get_disorder(index,label,url) for index,label,url in urls]



