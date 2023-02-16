
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from Bio import  SeqIO
import os


def get_url(url,seq):
    options = webdriver.ChromeOptions()
    #options.add_argument(
    #    'user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"')
    options.add_argument('--headless')
    options.add_argument('--blink-settings=imagesEnabled=false')

    browser = webdriver.Chrome('C:/Program Files/Google/Chrome/Application/chromedriver.exe')
    browser.get(url)
    time.sleep(1)
    browser.find_element(By.NAME,'sequence').send_keys(seq)
    browser.find_element(By.NAME,'prdos_submit').submit()
    time.sleep(1)
    browser.switch_to.window(browser.window_handles[0])
    time.sleep(1)
    browser.find_element(By.XPATH,'//input[@type="submit"]').submit()

    time.sleep(10)
    try:
        currentPageUrl=browser.current_url
        return (currentPageUrl)
    except TimeoutException:
        browser.execute_script('window.stop()')
        print(seq)
    browser.quit()



if __name__ == '__main__':
    #fasta_list=sorted(os.listdir('./Consensus_fastas'))
    fasta_list = sorted(os.listdir('./Native_lost'))
    fw=open('dis_urls_native_lost.txt','a')
    address='https://prdos.hgc.jp/cgi-bin/top.cgi'
    for file in fasta_list:
        fa=SeqIO.read('./Native_lost/'+file,'fasta')
        url=get_url(address,fa.seq)
        fw.write(fa.name+"\t"+url+"\n")
    fw.close()