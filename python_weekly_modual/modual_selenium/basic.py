from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
# driver.close()


ele_input_id = driver.find_element_by_id('kw')
# ele_input_name = driver.find_element_by_name('wd')
# ele_input_cls = driver.find_element_by_class_name('s_ipt')
ele_btn = driver.find_element_by_id('su')



# ele_input_name.send_keys('name')
# ele_input_cls.send_keys('cls')

ele_input_id.send_keys('Crossin的编程教室')
ele_btn.click()


# cookie_r = driver.get_cookies()
# # print(cookie_str)
# cookies_list = []
# for i in cookie_r:
#     cookie = i['name'] + '=' + i['value']
#     cookies_list.append(cookie)
#
# cookies_str = ';'.join(cookies_list)
#
# print(cookies_str)


# driver.get

js_code = 'return document.cookie'

cookies = driver.execute_script(js_code)

print(cookies)
