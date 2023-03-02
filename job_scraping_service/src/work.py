import requests
import codecs

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }

url = 'https://www.glassdoor.com/Job/prague-python-jobs-SRCH_IL.0,6_IC2296178_KO7,13.htm?context=Jobs&clickSource=searchBox'
# url = 'https://www.startupjobs.cz/nabidky/vyvoj/back-end/python?lokalita=ChIJi3lwCZyTC0cRkEAWZg-vAAQ'
# url = 'https://cz.indeed.com/jobs?q=Python&l=Prague&vjk=8dd59498c89f1f40'
# url = 'https://www.profesia.cz/en/work/prague/?search_anywhere=Python'

resp = requests.get(url, headers=headers)

h = codecs.open('work.html', 'w', 'utf-8')
h.write(str(resp.text))
h.close()