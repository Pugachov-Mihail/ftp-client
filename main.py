from ftplib import FTP

ftb = FTP('v91467wt.beget.tech')
ftb.login("v91467wt_ftps1", "_aaa_BBB_1")

for i in ftb.nlst():
    #Запись в файл всех файлов что есть в хосте
    with open('my_text.txt', 'w') as files:
        files.writelines(i)
#Загрузка из записей последний лог
with open('my_text.txt', 'r') as logo:
    logo_file = open('file.txt', 'wb')
    file = logo.read()
    ftb.retrbinary('RETR ' + str(file), logo_file.write, 1024)


