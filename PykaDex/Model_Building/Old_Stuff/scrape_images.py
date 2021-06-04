import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import wget

def contains_ext(ext,one_a_tag):
    """ """
    if ext in one_a_tag:
        return True
     
def scrape(url,ext):
    """ """
    #num of imgs
    lim = 21 # need to scroll page to increase count

    print('\nScrapping from ' + url + '\n')   
    response = requests.get(url) # will return 200 if allowed access    
    soup = BeautifulSoup(response.text, "html.parser") #gets html code
#    print(soup.findAll('a'))

    for i in range(0,len(soup.findAll('img'))+1): #'a' tags are for links    

        if i == 0:
            #this is the google logo
            continue    

        if i == lim:
            break

        one_a_tag = soup.findAll('img')[i]
        link = str(one_a_tag).split('src="')[1][:-3]
        #link = one_a_tag['href']
        print(str(i)+' - '+str(one_a_tag))

        # try:
        #     wget.download(link)
        # except:
        #     print('FAIL')
        
        if contains_ext(ext,str(one_a_tag)) == True:
        
            

            filename = str(str(one_a_tag).split('>')[1].split('<')[0])+ext # selects name 
            if '/' in filename:
                filename = filename.replace('/','-')
            
            download_url = url+ link
            urllib.request.urlretrieve(download_url,'scrapped/'+filename) 
            print(i,' - ' + filename)
            #time.sleep(0.1) 
        else:
            pass
            #print(i,'fail')
        
    print ('done')


searchtext = input('what do you want images of?\n')
#url = "https://www.google.co.in/search?q="+searchtext+"&source=lnms&tbm=isch"
url="https://bulbapedia.bulbagarden.net/wiki/Pikachu_(Pok%C3%A9mon)"
scrape(url,'.png')