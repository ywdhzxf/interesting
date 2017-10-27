#coding:utf8
from selenium import webdriver
import time
from lxml import etree

#加载内核
browser = webdriver.PhantomJS()
browser.get('http://neihanshequ.com/')
time.sleep(3)

for i in range(6):
    time.sleep(1)
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    browser.find_element_by_xpath('//div[@id="loadMore"]').click()

# browser.save_screenshot('ce.png')

res = browser.page_source
res = etree.HTML(res)
duanzi = res.xpath('//li[@class="group-item"]')
for res in duanzi:
    # print res
    #删选发件人和内容
    name = res.xpath('.//div[@class="name-time-wrapper left"]/span[@class="name"]/text()')
    content = res.xpath('.//div[@class="upload-txt {%if not the_data.content){%>no-mb{%endif%} {%if not the_data.large_image and not the_data.mp4_url%}no-mb{%endif%}"]/text()')

    print ''.join(name)
    print ''.join(content).strip()
    print '*'*100
