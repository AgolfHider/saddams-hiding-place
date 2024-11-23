# import urllib.request as rq
#
# opener = rq.build_opener()
# response = opener.open('https://httpbin.org/get')
#
# print(response.read())


#
# response = requests.get('https://httpbin.org/get')
# print(response.text)
#
# response = requests.post(
#     'https://httpbin.org/post',
#     data='Test data',
#     headers={'MyHeader': 'Test Title'}
# )
# print(response.text)
import requests
result_list = []
response = requests.get('https://coinmarketcap.com/currencies/hamster-kombat/')
page_text = response.text
parse_page_text = page_text.split('<span>')
for parse_elem_1 in parse_page_text:
    if parse_elem_1.startswith('$'):
        for parse_elem_2 in parse_elem_1.split('</span>'):
            if (parse_elem_2.startswith('$') and parse_elem_2[1].isdigit() ):
               result_list.append(parse_elem_2)

print(f'HMSTR Rate: {result_list[4]}')


from bs4 import BeautifulSoup

response = requests.get('https://coinmarketcap.com/')
