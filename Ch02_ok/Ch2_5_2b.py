with open("test.txt", "r", encoding="utf8") as fp:
    str = fp.read()
    print("檔案內容:")
    print(str)


# 若怕忘記呼叫close()函式，可使用　with / as 程式區塊來讀取




