from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
load_dotenv()


import os
MYAPP_USER = os.getenv('MYAPP_USER')
MYAPP_PASS = os.getenv('MYAPP_PASS')
DRIVER_PATH = os.getenv('DRIVER_PATH')
USER_ID = os.getenv('USER_ID')
PASSWORD = os.getenv('PASSWORD')


class LikeAutomation:
    def __init__(self):
        self.search_word = input('検索ワードは？("お返し"の場合はスキ返しをする。 or "exit"で終了)： ')
        print('\n')
        self.like_count = 100
        while not 0 < self.like_count <= 20:
            self.like_count = input('何回いいねする？(20以下の半角数字で入力 or "exit"で終了)： ')
            if self.like_count == 'exit':
                break
            try:
                self.like_count = int(self.like_count)
            except:
                print('半角数字を入力してください。\n')
                self.like_count = 100
                continue
            if not 0 < self.like_count <= 20:
                print('正しい値を入力してください。\n')

        self.login_to_note()

    def login_to_note(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://note.com')

        login_btn = self.driver.find_element(
            By.XPATH, '/html/body/div/div/div/div[1]/header/span/div/nav/div[2]/a'
        )
        login_btn.click()

        time.sleep(5)

        id_input = self.driver.find_element(By.ID, 'email')
        id_input.send_keys(USER_ID)

        password_input = self.driver.find_element(By.ID, 'password')
        password_input.send_keys(PASSWORD + Keys.ENTER)
        time.sleep(10)

    def search_and_like(self):
        search_box = self.driver.find_element(
            By.XPATH,
            '/html/body/div/div/div/div[1]/header/span/div/nav/div[1]/div/div[1]/div/form/input',
        )
        search_box.send_keys(self.search_word + Keys.ENTER)
        time.sleep(10)
        post_list = self.driver.find_elements(By.CLASS_NAME, 'm-largeNoteWrapper__card')
        push_like_count = 0
        for post in post_list:
            try:
                like_target = post.find_element(By.CLASS_NAME, 'a-icon--heart')
                like_target.click()
                push_like_count += 1
                print(f'「{post.text}」\n"スキを押しました。"\n')
            except:
                print('すでに"スキ"済み。\n')

            if push_like_count == self.like_count:
                break

    def return_like(self):
        pass

    def quit_driver(self):
        self.driver.quit()


if __name__ == '__main__':
    client = LikeAutomation()
    if client.search_word == 'お返し':
        client.return_like()
    else:
        client.search_and_like()
    time.sleep(5)
    client.quit_driver()
