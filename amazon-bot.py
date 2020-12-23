from selenium import webdriver
from time import sleep
import os


class AmazonBot:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def main(self):
        readme_disclaimer = input(
            "Amazon Purchase Bot\nby pyrokitsu\n\nIf you have any problems with the script, contact me at:\nDiscord: "
            "pyrokitsu#1237\nGitHub: https://github.com/pyrokitsu\n\nPlease READ the readme before proceeding.\n"
            "[x] abort [y] proceed\n> ")
        if readme_disclaimer == 'x':
            self.driver.close()
            os.system('Taskkill.exe /IM cmd.exe')
        elif readme_disclaimer == 'y':
            clear_screen()
            self.driver.get('https://www.amazon.fr')
            # Default = 15, change this setting depending on your connection.
            sleep(15)
            accept_cookie = self.driver.find_element_by_xpath('//*[@id="sp-cc-accept"]')
            accept_cookie.click()
            print("\n\nPlease login to your Amazon account! (You have 60 seconds!)")
            # Default = 60, change this setting depending on your speed to login at your account.
            sleep(60)
        else:
            clear_screen()
            bot.main()

    def check_and_buy(self):
        try:
            # Change the link of the product that you want to buy!
            self.driver.get("AMAZON LINK HERE")
            buy_now = self.driver.find_element_by_xpath('//*[@id="add-to-cart-button"]')
            buy_now.click()
            sleep(2)
            buy_now_announce = self.driver.find_element_by_xpath('//*[@id="siNoCoverage-announce"]')
            buy_now_announce.click()
            sleep(2)
        except Exception as e:
            if e:
                print("Cannot find the {Add to Cart} button! Refreshing now...")
                sleep(1.5)
                clear_screen()
                self.check_and_buy()
        finally:
            buy_now2 = self.driver.find_element_by_xpath('//*[@id="hlb-ptc-btn-native"]')
            buy_now2.click()
            sleep(2)
            buy_now3 = self.driver.find_element_by_xpath(
                '/html/body/div[5]/div/div[2]/form/div/div/div/div[2]/div/div[1]/div/div[1]/div/span/span/input')
            buy_now3.click()
            sleep(60)
            self.driver.close()


sys_windows = os.name == "nt"


def clear_screen():
    if not sys_windows:
        os.system("clear")
    else:
        os.system("cls")


bot = AmazonBot()
bot.main()
bot.check_and_buy()
