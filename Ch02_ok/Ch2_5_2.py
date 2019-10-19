import requests

r = requests.get("http://ououou.gq")
r.encoding = "utf-8"

fp = open("test.txt", "w", encoding="utf8")
fp.write(r.text)
print("寫入檔案test.txt...")
fp.close()

# 使用open()函式開啟，需再使用close()函式關閉
""" 
模式字串        當開啟檔案已存在時候        當開啟檔案不存在的時候
    r       開啟唯獨的檔案                  　產生錯誤
    w       清除檔案內容後寫入              　建立寫入檔案
    a       開啟檔案從檔尾後開始寫入          建立寫入檔案
    r+      開啟讀寫得檔案                  　產生錯誤
    w+      清除檔案內容後讀寫內容          　建立讀寫檔案
    a+      開啟檔案從檔尾後開始讀寫        　建立讀寫檔案

"""
