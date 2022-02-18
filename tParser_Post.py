# ---------------------------------------------------------------
# This program shows how to search the first ten results from
# google website
# Written by Yingli Zhao, February 2022
# ---------------------------------------------------------------
import json
import traceback
import requests
from bs4 import BeautifulSoup


#   Anzeige im Googlesearch wird hier ausgeschlossen
def searchresults(keyword):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'}
#   search key is bosch, search from the first result to 10, num set to 13 instead of 10 due to some Werbung
    url = 'https://google.com/search'
    kv = {'q': keyword, 'start': '0', 'num': '20'}
#   simulate the user-agent to deactive the consent (Nutzungsbedingen)
    try:
        re = requests.get(url, params=kv, headers=headers)
        re.encoding = re.apparent_encoding
#        print(re.status_code)   # will be changed to try by checking status code
        if re.status_code != 200:
            raise Exception('Statuscode of google is:' + str(re.status_code))
        else:
            content = BeautifulSoup(re.content, 'html.parser')
#            elements = content.find_all("div", {"class": "tF2Cxc"})
            elements = content.find_all("div", {"class": "yuRUbf"})
            result = {}
#            print(len(elements))
            if len(elements) <= 10:
                for i in range(len(elements)):
                    title = elements[i].find("h3", {"class": "LC20lb MBeuO DKV0Md"}).text
                    link = elements[i].find("a", href=True)['href']
                    key = 'Searchresult[' + str(i) + ']'
                    result[key] = [title, link]
            else:
                for i in range(10):
                    title = elements[i].find("h3", {"class": "LC20lb MBeuO DKV0Md"}).text
                    link = elements[i].find("a", href=True)['href']
                    key = 'Searchresult[' + str(i) + ']'
                    result[key] = [title, link]


#                print('weiter....')
#                elements_add = content.find_all("div", {"class": "g tF2Cxc"})
#                print(len(elements_add))
#                for j in range(10-len(elements)):
#                    title = elements_add[j].find("h3", {"class": "LC20lb MBeuO DKV0Md"}).text
#                    link = elements_add[j].find("a", href=True)['href']
#                    key = 'Searchresult[' + str(j+len(elements)) + ']'
#                    result[key] = [title, link]
        filename = "result_getMethode_2.json"
        with open(filename, "w") as outfile:
            json.dump(result, outfile)
        return filename

    except Exception as e:
        traceback.print_exc()
        return None


#if __name__ == "__main__":
#    searchresults('bosch')
