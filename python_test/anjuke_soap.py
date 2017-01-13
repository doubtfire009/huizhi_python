from bs4 import BeautifulSoup

default_encoding = 'utf-8'
page_num_max = 6
page_num = 1

text_url1 = 'f:/data/anjukehk'
text_url2 = '.txt'
while(page_num <= page_num_max):
    text_url = text_url1 + str(page_num) + text_url2
    f = open(text_url, "r", encoding='utf-8')
    content = f.read()
    soup = BeautifulSoup(content)
    spans_list = soup.select('span[class="comm-address"]')


f = open("f:/data/anjukehk.txt","r",encoding='utf-8')
content = f.read()
# print(content)
soup = BeautifulSoup(content)
spans_list = soup.select('span[class="comm-address"]')
print(spans_list)
# print(len(spans_list))
# print(spans_list[0].string)
# print(spans_list[0].string.splitlines()[2])

# for span in spans_list:
#     print(span.string)
#     print("-------")

f.close()