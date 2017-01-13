page_num = 1;
k1= 'http://shanghai.anjuke.com/sale/hongkou/p'
k2= '-rd1/?kw=%E5%9C%B0%E6%9A%96&from_url=kw_final'
while(page_num < 7):
    k = k1 + str(page_num) + k2
    print(k)
    print("/n")
    print("---------")
    print("/n")
    page_num = page_num + 1

