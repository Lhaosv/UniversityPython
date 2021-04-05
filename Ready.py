from bs4 import BeautifulSoup   #  网页解析，获取数据
import re  #  正则表达式，进行文字匹配
import urllib.request,urllib.error  #  自定URL,获取网页数据
import xlwt  #  进行excel操作


# 影片详情链接的规则：
findlink = re.compile(r'<a href="(.*?)">')
# 影片图片的链接规则
findimg = re.compile(r'<img.*src="(.*?)"',re.S)# re.S 让换行符包含在字符中
# 影片名字的规则
findtitle = re.compile(r'<span class="title">(.*)</span>')
# 影片评分的规则
findpingfen = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 影片评论的规则
findpinglun = re.compile(r'<span>(.*)</span>')
# 影片概述的规则
findgaisu = re.compile(r'<p class="">(.*?)</p>',re.S)


def main():
    baseURL = "https://movie.douban.com/top250?start="
    # 1.爬取网页
    datalist = getDate(baseURL)  # 调用getDate（）方法
    # 2.解析数据 (一边爬取一边解析)
    # 3.保存数据
    askURL("https://movie.douban.com/top250?start=")
    savepath = "豆瓣电影top250.xls"
    saveDate(datalist, savepath)  # 调用saveDate()方法

#  1.爬取网页
def getDate(baseURL):
    datalist = []
    for i in range(0,10):  #  调用获取页面信息的函数，10次
        url = baseURL + str(i*25)
        html = askURL(url)  # 保存获取到的网页源码

        # 逐一进行解析

        soup = BeautifulSoup(html,"html.parser") #  解析器
        for item in soup.find_all('div',class_="item"):  #  查找符合要求的字符串，形成列表
            #print(item)  # 测试：查看电影item的全部信息
            data = []  # 保存一部电影的所有信息
            item = str(item)
            title = re.findall(findtitle, item)[0]
            data.append(title)  # 添加名字

            link = re.findall(findlink,item)[0]  # re库用来通过正则表达式查找指定的字符串
            data.append(link)         #  添加图片

            img = re.findall(findimg, item)[0]
            data.append(img)    #  添加链接

            gaisu = re.findall(findgaisu,item)[0]
            gaisu = re.sub('<br(\s+)?/>(\s+)?'," ",gaisu)  # 去掉<br/>
            data.append(gaisu.strip())   #  添加概述 strip() 去掉空格

            pingfen = re.findall(findpingfen,item)[0]
            data.append(pingfen)  # 添加评分

            pinglun = re.findall(findpinglun,item)[0]
            data.append(pinglun)  #  添加评论

            datalist.append(data)
            # print(title)
            # print(link)
            # print(img)
            # print(pingfen)
            # print(pinglun)





    print(datalist)
    return datalist

# 得到指定一个url的网页内容
def askURL(url):
    head ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63"}
    html = "https://movie.douban.com/top250?start="
    request = urllib.request.Request(url,headers=head)
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr((e,"reason")):
            print(e.reason)
    return html



#  3.保存数据
def saveDate(datalist,savapath):
    print("save...")
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)
    sheet = book.add_sheet("豆瓣电影TOP250",cell_overwrite_ok=True)
    col = ("电影名","电影链接","图片链接","概述","评分","评价数")
    for i in range(0,6):
        sheet.write(0,i,col[i])  #  列名
    for i in range(0,250):
        print("第%d条"%(i+1))
        data = datalist[i]  # 这里的i表示第i部电影的全部信息
        for j in range(0,6):
            sheet.write((i+1),j,data[j]) # 此处i+1是为了让第一行显示列名  因为列名是第0行
                                         #  这里的j表示一部电影里面的信息，例如 电影名，评分等
    book.save(savapath)  #  保存


if __name__ == '__main__':             # 当程序执行时
# 调用函数
    main()
print("爬取完毕！")