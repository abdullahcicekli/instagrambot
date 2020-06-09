# from instagramkullanici import username,password
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import keyboard
import random
import os
import os.path
from termcolor import colored

class Instagram:
    def menü(self):
        print (colored('MENÜ ', 'red').center(60,"*"))
        
        while True:
            print(colored("1-","yellow")+" Takipçileri Çek\n"+colored("2-","yellow")+" Takip Ettiklerini Çek\n"+colored("3-","yellow")+ " Takip Etmeyenleri Takipten Çık\n"+colored("4-","yellow")+ " Otomatik Takip Yap\n"+colored("5-","yellow")+ " Otomatik Yorum Yap\n"+colored("6-","yellow")+ " Çıkış\n")
            secim =input("Seçiniz : ")

            if secim == "6":
                break
            else:
                if secim =="1":
                    while True:
                        print(colored("Kimin Takipçileri Çekilecek ?\n","green"))
                        print(colored("1-","green")+" Kendi Takipçilerim\n"+colored("2-","green")+" Başkasının Takipçileri\n")
                        sec = input("Seçiniz : ")
                        if sec=="1":
                            time.sleep(2)
                            kullanici = self.username
                            instagram.getFollowers(kullanici)
                            break
                        elif sec=="2":
                            kullanici = input("Kullanıcı Adı Giriniz : ")
                            instagram.getFollowers(kullanici)
                            break
                        else:
                            print(colored("\nHatalı Seçim Yaptınız 1 veya 2 olarak seçim yapınız.","red"))
                            
                    
                    
                elif secim =="2":
                    while True:
                        print(colored("Kimin Takip Ettikleri Çekilecek ?\n","green"))
                        print(colored("1-","green")+" Kendi Takip Ettiklerim\n"+colored("2-","green")+" Başkasının Takip Ettikleri\n")
                        sec = input("Seçiniz : ")
                        if sec=="1":
                            time.sleep(2)
                            kullanici = self.username
                            instagram.getFollow(kullanici)
                            break
                        elif sec=="2":
                            kullanici = input("Kullanıcı Adı Giriniz : ")
                            instagram.getFollow(kullanici)
                            break
                        else:
                            print(colored("\nHatalı Seçim Yaptınız 1 veya 2 olarak seçim yapınız.","red"))

                elif secim =="3":
                    print(colored("Takipten Çıkma Nasıl Yapılacak ?\n","green"))
                    print(colored("(Unfollow sayısı fazla ise otomatik işlemi seçiniz)","yellow").center(60,"*"))
                    print(colored("NOT :","yellow")+colored("Otomatik işlem işlem arasındaki süreleri random olarak\nbelirleyerek 1 dk ortalama 2 unfollow yapar.\nBu sayede instagram'ın olası kısıtlamasından kaçınılmış olur.\n","white"))
                    print(colored("1-","green")+" Seçimi Bana Bırak\n"+colored("2-","green")+" Tüm Takip Etmeyenleri Otomatik Çık\n"+colored("3-","green")+ " Programdan Çık\n")
                    
                    while True:
                        try:
                            while True:
                                sec = int(input("Seçiniz : "))
                                
                                if sec == 3:
                                    break
                                elif sec==1 or sec==2:
                                    instagram.unfollow(username,sec)
                                    time.sleep(random.randint(15,30))
                                    break
                                else:
                                    print("\nLütfen 1-2-3 Olarak Seçiniz.")
                            break
                        except ValueError:
                            print(colored("Lütfen 1-2-3 Olarak Seçiniz.\n","red"))

                elif secim == "4":
                    print(colored("Bu işlem için kullanıcı listesi gerekir.","yellow"))
                    dosya=input("Dosya Yolunu Giriniz :")
                    edilecekler=[]
                    if os.path.isfile(dosya):
                        with open(dosya,"r",encoding="utf-8") as file:
                            for i in file:
                                edilecekler.append(i.split("\n")[0])
                                
                        for satır in edilecekler:
                            instagram.followUser(satır)
                    else:
                        print("Dosya Bulunamıyor")
                elif secim =="5" :
                    print(colored("Bu İşlem İçin Yorum Yapılacak Link ve Kullanıcı Listesi Gereklidir."),"green")
                    print(colored("UYARI","red").center(60,"*"))
                    print("*".center(60,"*"))
                    print(colored("Yorum Botu Çalışırken Bilgisayara Dokunmayın.","white"))
                    print(colored("\nYorum Botu Ne Amaçla Kullanılacak ?\n","green"))
                    print(colored("1-","yellow")+" REKLAM\n"+colored("2-","yellow")+" ÇEKİLİŞ")
                    while True:
                        sectir = input("Seçiniz : ")
                        if sectir == "2":
                            link = input("Link : ")
                            dosya = input("Etiletlencek Kullanıcı Dosyasını Giriniz :")
                            if os.path.isfile(dosya):
                                sayac=0
                                with open(dosya,"r",encoding="utf-8") as file:
                                    for i in file:
                                        s = i.split()
                                        listToStr = ' '.join(map(str, s)) 
                                        sayac+=1
                                        instagram.yorumekle(link,"@"+listToStr) 
                                        r=random.randint(20,45)
                                        print(f"{sayac}-{listToStr} isimli kullanıcı etiketlendi. Diğer kullanıcı {r} saniye sonra etiketlenecek.\nLütfen Hata Almamak İçin Etiketlenmeler Bitene Kadar Bilgisayarınıza Dokunmayın")
                                        time.sleep(r)
                            else:
                                print("Dosya Bulunamıyor")
                            break
                        elif sectir =="1":
                            print(colored("NOT: ","red")+colored("Bu işlem için hashtag ve yorum bilgisi gereklidir.","red"))
                            print(colored("Hangi hastag'deki görsellere yorum yapılacak ?: ","green"))
                            hashtag = input("--> ")
                            print(colored("Yorum olarak ne yazılacak ?: ","green"))
                            mesaj = input("--> ")
                            print(colored("Kaç Resme Yorum Yapılsın ?: ","green"))
                            sayi = int(input("--> "))
                            instagram.hashtag(hashtag,mesaj,sayi)
                            
                        else:
                            print("Hatalı Giriş Yaptınız.")
                            break

                            

                else:
                    print(colored("Yanlış Seçim\n","red"))


    def __init__(self,username,password):
        self.browser=webdriver.Chrome()
        self.username=username
        self.password=password
        self.followers = []
        self.follow=[]
        self.takipetmeyenler = []

    def hashtag(self,hashtag,mesaj,sayi):
        
        for i in range(int(sayi/3)):
            for j in range(3):
                self.browser.get("https://www.instagram.com/explore/tags/"+hashtag)
                if sayi > 24:
                    for tekerlek in range(i*3):
                        action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                        action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                time.sleep(2)
                self.browser.find_elements_by_xpath("//*[@id='react-root']/section/main")
                link = self.browser.find_element_by_xpath(f"//*[@id='react-root']/section/main/article/div[2]/div/div[{i+1}]/div[{j+1}]/a").get_attribute("href")
                self.browser.get(link)
                self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[1]/article/div[2]/section[3]/div/form/textarea").click()
                keyboard.write(mesaj)
                time.sleep(1)
                self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[1]/article/div[2]/section[3]/div/form/button").click()
                time.sleep(4)

    def yorumekle(self,linkk,username):
        try:
            self.browser.get(linkk)
            time.sleep(1)
            # begen=self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[1]/article/div[2]/section[1]/span[1]/button").click()
            self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[1]/article/div[2]/section[3]/div/form/textarea").click()
            # for i in username:
            #     keyboard.press(i)
            #     keyboard.release(i)
            #     time.sleep(0.25)
            keyboard.write(username)
            time.sleep(1)
            self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[1]/article/div[2]/section[3]/div/form/button").click()
        except selenium.common.exceptions.ElementClickInterceptedException:
            print(colored("Beklenmeyen Bir Hata Oluştu. Linki Tekrar Kontrol Edin ve İşlem Sırasında Bilgisayarınız ile oynamayın.","red"))
    
    def girisyap(self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(3)
        emailInput=self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
        passwordInput=self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")

        emailInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[4]").click()
        time.sleep(3)
############################################################################## TAKİPÇİLER #############################
        
    def getFollowers(self,username):
        try:
            self.browser.get(f"https://www.instagram.com/{username}")
            time.sleep(2)
            self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
            time.sleep(2)
            dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
            followersCount = len(dialog.find_elements_by_css_selector("li"))
            action = webdriver.ActionChains(self.browser)
            #takipci = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/span").text
            # # sayi= float(takipci)
            time.sleep(1)
            sayac=1
            while True:
                self.browser.find_element_by_xpath("/html/body/div[4]/div/div[2]").click()
                if sayac==1:
                    action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                    action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                else:
                    action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                sayac +=1    
                time.sleep(2)
                newResult = len (dialog.find_elements_by_css_selector("li"))

                if  followersCount != newResult:
                    followersCount=newResult
                    print(colored(f"Takipçiler Alınıyor Lütfen Bekleyiniz\nÇekilen Takipçi : {newResult}\n","blue"))
                else :
                    break

            followers = dialog.find_elements_by_css_selector("li")

            for user in followers:
                link = user.find_element_by_css_selector("a").get_attribute("href")
                # print(link) #Ekrandan Yazdırmak İçin
                self.followers.append(link.split("/")[3])
            

            with open(f"{username} takipciler.txt","w",encoding="utf-8") as file:
                for kullanici in self.followers:
                    file.write(kullanici+"\n")

            del self.followers[0:len(self.followers)]
        except:
            print("Beklenmedik Bir Hata Oluştu. Tekrar Deneyiniz")
####################################################################################  UNFOLLOW  #######################
    def unfollow(self,username,sayi):
        sayactakip=0
        takipciler=[]
        if os.path.isfile(f"{username} edilentakip.txt") and os.path.isfile(f"{username} takipciler.txt"): 
            with open(f"{self.username} takipciler.txt","r",encoding="utf-8") as file:
                for i in file:
                    takipciler.append(i.split("\n")[0])
            
            takipedilenler=[]
            with open(f"{self.username} edilentakip.txt","r",encoding="utf-8") as file:
                for i in file:
                    takipedilenler.append(i.split("\n")[0])
            saydır=0
            for eleman in takipedilenler:
                if not eleman in takipciler:
                    self.takipetmeyenler.append(eleman)
                    print(self.takipetmeyenler[saydır])
                    saydır+=1    
            print("\n"+colored(f"{saydır}","yellow")+ "adet takip etmeyen kullanıcı tespit edildi")  
            
            for eleman in takipedilenler:
                if eleman in takipciler:
                    # print(f"{eleman} takipte") #Takip edenleri sıralamak için burayı aktif yap.
                    pass
                    
                else:
                    if sayi == 1:
                        print("\n"+colored(f"{eleman}","red") +colored(" takip etmiyor. Takipten Çıkılsın mı ?\n" ,"green")+colored("1-","yellow")+ " Evet\n"+ colored("2-","yellow")+ " Hayır\n"+ colored("3-","yellow")+ " Üst Menüye Dön\n")
                        
                        while True:    
                            try:
                                while True:
                                    soru=int(input("Seçiniz : "))
                                    if soru==1 or soru==2 or soru==3:
                                        break  
                                    else:
                                        print("\nLütfen 1-2-3 Olarak Seçiniz.")
                                break
                            except ValueError:
                                print("\nLütfen 1-2-3 Olarak Seçiniz.")
                                   
                        try:
                            if soru==1:
                                self.browser.get(f"https://www.instagram.com/{eleman}")
                                time.sleep(1)
                                self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[2]/span/span[1]/button/div/span").click()
                                time.sleep(1)
                                self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[1]").click()
                                with open(f"{self.username} edilentakip.txt","r",encoding="utf-8") as file:
                                    satirlar = file.readlines()
                                with open(f"{self.username} edilentakip.txt","w",encoding="utf-8") as file:
                                    for line in satirlar:
                                        if line != eleman+"\n":
                                            file.write(line)
                                print(f"{eleman} isimli kullanıcı takipten çıkarıldı.")
                            # except selenium.common.exceptions.NoSuchElementException:
                            #     self.browser.get(f"https://www.instagram.com/{eleman}")
                            #     time.sleep(random.randint(10,20))
                            #     self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/button").click()
                            #     time.sleep(random.randint(1,5))
                            #     self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[1]").click()
                            #     with open(f"{self.username} edilentakip.txt","r",encoding="utf-8") as file:
                            #         satirlar = file.readlines()
                            #     with open(f"{self.username} edilentakip.txt","w",encoding="utf-8") as file:
                            #         for line in satirlar:
                            #             if line != eleman+"\n":
                            #                 file.write(line)
                            #     print(f"{eleman} isimli kullanıcı takipten çıkarıldı.")
                            elif soru==2:
                                pass
                            else:
                                return instagram.menü()
                        
                        except selenium.common.exceptions.NoSuchElementException:
                            print(colored(f"{eleman}","green")+" takipten çıkartılamadı.\n"+colored("Beklenmeyen Bir Hata Oluştu Lütfen Bir Süre Sonra Tekrar Deneyin.","red") )  
                    
                    elif sayi ==2:
                        try:
                            self.browser.get(f"https://www.instagram.com/{eleman}")
                            time.sleep(random.randint(10,20))
                            self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[2]/span/span[1]/button/div/span").click()
                            time.sleep(random.randint(1,5))
                            self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[1]").click()
                            with open(f"{self.username} edilentakip.txt","r",encoding="utf-8") as file:
                                satirlar = file.readlines()
                            with open(f"{self.username} edilentakip.txt","w",encoding="utf-8") as file:
                                for line in satirlar:
                                    if line != eleman+"\n":
                                        file.write(line)
                            print(f"{eleman} isimli kullanıcı takipten çıkarıldı.")
                        # except selenium.common.exceptions.NoSuchElementException:
                        #     self.browser.get(f"https://www.instagram.com/{eleman}")
                        #     time.sleep(random.randint(10,20))
                        #     self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/button").click()
                        #     time.sleep(random.randint(1,5))
                        #     self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[1]").click()
                        #     with open(f"{self.username} edilentakip.txt","r",encoding="utf-8") as file:
                        #         satirlar = file.readlines()
                        #     with open(f"{self.username} edilentakip.txt","w",encoding="utf-8") as file:
                        #         for line in satirlar:
                        #             if line != eleman+"\n":
                        #                 file.write(line)
                        #     print(f"{eleman} isimli kullanıcı takipten çıkarıldı.")
                        
                        except selenium.common.exceptions.NoSuchElementException:
                            print(colored(f"{eleman}","green")+" takipten çıkartılamadı.\n"+colored("Beklenmeyen Bir Hata Oluştu Lütfen Bir Süre Sonra Tekrar Deneyin.","red") )                                  
                    
                    else:
                        pass
        else:
            print(colored("Takipçilerinizi ve Takip Ettiklerinizi Çektikten Sonra Bu Özelliği Kullanabilirsiniz.\nLütfen önce 1 ve 2. Seçenekleri Çalıştırın.","yellow"))
            return instagram.menü()
      #############################################################################3 TAKİP EDİLENLER #################33 

    def getFollow (self,username):
        try:
            self.browser.get(f"https://www.instagram.com/{username}")
            time.sleep(2)
            self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a").click()
            time.sleep(2)
            dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
            followCount = len(dialog.find_elements_by_css_selector("li"))
            action = webdriver.ActionChains(self.browser)
            #takipci = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/span").text
            # # sayi= float(takipci)
            time.sleep(1)
            sayac=1
            
            while True:
                self.browser.find_element_by_xpath("/html/body/div[4]/div/div[2]/ul").click()
                if sayac==1:
                    action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                    action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                else:
                    action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                    action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                sayac +=1    
                time.sleep(4)
                newResult = len (dialog.find_elements_by_css_selector("li"))

                if  followCount != newResult:
                    followCount=newResult
                    print(colored(f"Takipler Alınıyor Lütfen Bekleyiniz\nÇekilen Takip : {newResult}\n","blue"))
                else :
                    break

            follow = dialog.find_elements_by_css_selector("li")

            for user in follow:
                link = user.find_element_by_css_selector("a").get_attribute("href")
                # print(link.split("/")[3]) #Ekrandan Yazdırmak İçin
                self.follow.append(link.split("/")[3])
            

            with open(f"{username} edilentakip.txt","w",encoding="utf-8") as file:
                for kullanici in self.follow:
                    file.write(kullanici+"\n")

            del self.follow[0:len(self.follow)]
        except:
            print("Hata Oluştu Sonra Tekrar Deneyiniz.")

        ########################################################################## TAKİP ETME #####################

    def followUser(self, username):
        self.browser.get("https://www.instagram.com/"+ username)
        time.sleep(2)

        followButton = self.browser.find_element_by_tag_name("button")
        if followButton.text != "Following" or followButton.text != "Takiptesin" or followButton.text != "Mesaj Gönder" or followButton.text != "Message":
            followButton.click()
            time.sleep(2)
        else:
            print("Zaten takiptesin")


#################################################################################### ANA KOD BLOĞU ###################

print (colored('İnstagram Bot ', 'red').center(60,"*"))
print (colored("Bot'u başlatmak için bilgileri giriniz. ", 'yellow'))
username = input("Kullanıcı Adı : ")
password = input("Parola : ")
instagram=Instagram(username,password)
instagram.girisyap()
instagram.menü()