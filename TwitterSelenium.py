import datetime
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def log(log_text):
    log_text = str(time.strftime("\n%Y.%m.%d %H:%M:%S")) + " ➾ " + log_text
    log_file = open("logs.txt", "a", encoding='utf-8')
    log_file.write(log_text + "\n")
    log_file.close()

def log_finish(logtext):
    logtext = "----------------------------- " + logtext
    log_file = open("logs.txt", "a", encoding='utf-8')
    log_file.write(logtext + "\n")
    log_file.close()

#ENTER YOUR USERNAME AND PASSWORD
usernames = ["your_username1", "your_username2"]
passwords = ["your_password1", "your_password2"]

#ENTER YOUR TWEET PATHS
tweet_path = [
    "https://twitter.com/example_tweet_path_1",
    "https://twitter.com/example_tweet_path_2",
    "https://twitter.com/example_tweet_path_3",
    "https://twitter.com/example_tweet_path_4",
]

quotes_num = 0 # change this number if you want to comment more or less
rt_num = 3 # change this number if you want to retweet more or less

quotes_yes_no = "no"  # yes or no
quotes_number = len(tweet_path) * quotes_num
retweet_number = len(tweet_path) * rt_num

quotes_goodmorning = ["Günaydınn",
          "iyi günler",
          "İyi günler! Piyasa telaşına kapılmayın ahahah",
          "teşekkürler",
          "sağolun"]

quotes_project = ["Harika bir proje",
                "Tam olarak bu ne",
                "Güzel haber",
                "Bakıyorum hemen",
                "👏👏👏",
                "👍👍",
                ]



quotes = quotes_project # quotes_goodmorning or quotes_project

like_count = 0
retweet_count = 0
comment_count = 0

personal_like_count = 0
personal_retweet_count = 0
personal_comment_count = 0

log_finish("Program Başladı  -----------------------------")
log("Kullanıcı adı ve şifreler alındı")
log("Toplam kullanıcı sayısı: " + str(len(usernames)))
log("Toplam tweet sayısı: " + str(len(tweet_path)))
rtsayi=retweet_number/len(tweet_path)
log("Her tweet için retweet sayısı: " + str(rtsayi))
quotessayi=quotes_number/len(tweet_path)
log("Yorum isteği: " + str(quotessayi))


for i in range(len(usernames)):
    try:
        log("Yeni kullanıcıya geçiliyor: " + usernames[i])
        # Twitter'a tarayıcı ile giriş yapma ve işlemleri gerçekleştirme kodları
        # open Twitter in Browser
        driver = webdriver.Chrome()
        driver.get("https://twitter.com/i/flow/login")

        time.sleep(5)

        # enter username
        wait = WebDriverWait(driver, 5)
        username = wait.until(EC.element_to_be_clickable((By.XPATH, "//input")))
        username.send_keys(usernames[i])
        time.sleep(2)
        log("Username entered: " + usernames[i])

        # click on the "next" button
        all_buttons = driver.find_elements(By.XPATH, "//div[@role='button']")
        all_buttons[-2].click()
        time.sleep(5)

        # enter password & login
        password = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='password']")))
        password.send_keys(passwords[i])
        time.sleep(2)
        log("Password entered: " + passwords[i])

        # click on the "login" button
        all_buttons = driver.find_elements(By.XPATH, "//div[@role='button']")
        all_buttons[-1].click()
        time.sleep(4)

        for a in range(len(tweet_path)):
            try:
                driver.get(tweet_path[a])
                log(" • New Tweet link entered: " + tweet_path[a] + "   ♥")

                # Wait for the tweet to load (adjust sleep time accordingly)
                time.sleep(4)

                # Find and click the "like" button within the tweet
                like_button = driver.find_element(By.XPATH, "//div[@data-testid='like']")
                like_button.click()
                print(f"User {i + 1} Liked!")
                like_count += 1
                personal_like_count += 1
                log("Tweet liked from: " + usernames[i] + "   ♥")
                time.sleep(2)

                if retweet_count < retweet_number:
                    # Find and click the "retweet" button within the tweet
                    retweet_button = driver.find_element(By.XPATH, "//div[@data-testid='retweet']")
                    retweet_button.click()
                    time.sleep(3)
                    retweet_confirm_button = driver.find_element(By.XPATH, "//div[@data-testid='retweetConfirm']")
                    retweet_confirm_button.click()
                    time.sleep(1)
                    print(f"User {i + 1} Retweeted!")
                    retweet_count += 1
                    personal_retweet_count += 1
                    log("Tweet retweeted from: " + usernames[i] + "   ✔")
                    time.sleep(2)

                if comment_count < quotes_number and quotes_yes_no == "yes":
                    # Replying to tweet
                    reply_input = driver.find_element(By.XPATH, '//div[@data-testid="tweetTextarea_0"]')
                    reply_input.send_keys(quotes[i])
                    reply_input.send_keys(Keys.CONTROL, Keys.ENTER)
                    time.sleep(3)  # Wait for reply
                    print(f"User {i + 1} Commented!")
                    comment_count += 1
                    personal_comment_count += 1
                    log("Tweet commented from: " + usernames[i] + "   ✔" + "   Comment: " + quotes[i])
                    time.sleep(3)

                print("-----------")
                print(
                    f"Kullanıcı {i + 1} Beğendi: {personal_like_count}, Retweetledi: {personal_retweet_count}, Yorum Yaptı: {personal_comment_count}")
                time.sleep(1)
                print("Yeni tweete geçiliyor...")

            except Exception as ex:
                error_message = str(ex)
                if "element click intercepted" in error_message:
                    print(f"Hata, Kullanıcı {i + 1} için: Belirli bir hatayla karşılaşıldı.")
                    log("User " + str(i + 1) + " (" + usernames[i] + ") " + "için: Belirli bir hatayla karşılaşıldı.")
                else:
                    print(f"Hata, Kullanıcı {i + 1} için: {error_message}")
                    log("User " + str(i + 1) + " (" + usernames[i] + ") " + "için: Belirli bir hatayla karşılaşıldı.")
            finally:
                # Bir istisna oluşsa da olmasa da tarayıcının kapatılmasını sağlamak için
                print()


    except Exception as e:
        error_message = str(e)
        if "element click intercepted" in error_message:
            print(f"Hata, Kullanıcı {i+1} için: Belirli bir hatayla karşılaşıldı.")
            log("User " + str(i + 1) + " (" + usernames[i] + ") " + "için: Belirli bir hatayla karşılaşıldı.")
        else:
            print(f"Hata, Kullanıcı {i+1} için: {error_message}")
            log("User " + str(i + 1) + " (" + usernames[i] + ") " + "için: Belirli bir hatayla karşılaşıldı.")

    finally:
        log("User " + str(i + 1) + " (" + usernames[i] + ") " + " liked: " + str(
            personal_like_count) + ", retweeted: " + str(
            personal_retweet_count) + ", commented: " + str(personal_comment_count))
        personal_comment_count = 0
        personal_like_count = 0
        personal_retweet_count = 0
        log("User " + str(i + 1) + " (" + usernames[i] + ") " + " işlemi bitti.")
        # Bir istisna oluşsa da olmasa da tarayıcının kapatılmasını sağlamak için
        print("Yeni kullanıcıya geçiliyor...")
        if 'driver' in locals():
            driver.quit()


print("-----------")
print(f"Toplamda {len(usernames)} kullanıcı, {like_count} beğeni, {retweet_count} retweet ve {comment_count} yorum yaptı.")
log("Toplamda " + str(len(usernames)) + " kullanıcı, " + str(like_count) + " beğeni, " + str(retweet_count) + " retweet ve " + str(comment_count) + " yorum yaptı.")
print("-----------")
log("Ortalama beğeni sayısı: " + str(round(like_count / len(tweet_path), 2)))
log("Ortalama retweet sayısı: " + str(round(retweet_count / len(tweet_path), 2)))
log("Ortalama yorum sayısı: " + str(round(comment_count / len(tweet_path), 2)))
tahmini_islem_yapan_kullanici_sayisi = len(tweet_path) - round(like_count / len(tweet_path), 2)
log("Tahmini işlem yapmayan kullacı sayısı: " + str(tahmini_islem_yapan_kullanici_sayisi))
print("-----------")
log_finish("Program Bitti ----------------------------- \n\n")