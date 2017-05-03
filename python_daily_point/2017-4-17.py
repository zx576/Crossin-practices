# from selenium import webdriver
#
# driver = webdriver.PhantomJS()
#
#
# driver.get('http://www.baidu.com')
#
# print(driver.current_url)


title,url,keywords,content = 0,0,0,0


sql = '''
        SELECT URL,CONTENT FROM RESOURCE \
        WHERE TITLE LIKE '%{0}%' \
        OR WHERE URL LIKE '%{1}%' \
        OR WHERE KEYWORDS LIKE '%{2}%' \
        OR WHERE CONTENT  LIKE  '%{3}%'
      '''.format(title,url,keywords,content)

# sql = r'''
#         SELECT URL,CONTENT FROM RESOURCE \
#         WHERE TITLE LIKE '%{0}'
#       '''.format(title)


print(sql)
