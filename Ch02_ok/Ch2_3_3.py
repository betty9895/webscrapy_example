import requests 

r = requests.get("http://www.google.com")

print(r.headers['Content-Type'])
print(r.headers['Content-Length'])
print(r.headers['Date'])
print(r.headers['Server']) 

# 取得標頭名稱(須注意英文大小寫)
# Content-Type的值是MIME資料類型

""" 
常見MIME類型

超文字標記語言文字 .html        text/html 
普通文字          .txt         text/plain 
RTF文字           .rtf         application/rtf 
GIF圖形           .gif         image/gif 
JPEG圖形          .ipeg,.jpg   image/jpeg 
au聲音檔案         .au         audio/basic 
MIDI音樂檔案       mid,.midi   audio/midi,audio/x-midi 
RealAudio音樂檔案 .ra, .ram    audio/x-pn-realaudio 
MPEG檔案          .mpg,.mpeg   video/mpeg 
AVI檔案           .avi         video/x-msvideo 
GZIP檔案          .gz          application/x-gzip 
TAR檔案           .tar         application/x-tar  
"""