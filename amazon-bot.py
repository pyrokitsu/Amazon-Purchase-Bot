from selenium import webdriver
from time import sleep
import os


class AmazonBot:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def main(self):
        self.driver.get('https://www.amazon.fr')
        # Default = 15, change this setting depending on your connection.
        sleep(10)
        accept_cookie = self.driver.find_element_by_xpath('//*[@id="sp-cc-accept"]')
        accept_cookie.click()
        readme_disclaimer = input(
            "Amazon Purchase Bot\nby pyrokitsu\n\nIf you have any problems with the script, contact me at:\nDiscord: "
            "pyrokitsu#1237\nGitHub: https://github.com/pyrokitsu\n\nPlease READ the readme before proceeding.\n"
            "[x] abort [y] proceed\n> ")
        if readme_disclaimer == 'x':
            self.driver.close()
            os.system('Taskkill.exe /IM cmd.exe')
        elif readme_disclaimer == 'y':
            clear_screen()
            print("Please login to your Amazon account! (You have 60 seconds!)")
            # Default = 60, change this setting depending on your speed to login at your account.
            sleep(60)
        else:
            clear_screen()
            bot.main()

    def check_and_buy(self):
        try:
            # Change the link of the product that you want to buy!
            self.driver.get("LINK HERE")
            buy_now = self.driver.find_element_by_xpath('//*[@id="buy-now-button"]')
            buy_now.click()
            sleep(2)
        except Exception as e:
            if e:
                print("Cannot find the {Buy Now} button! Refreshing now...")
                sleep(1.5)
                clear_screen()
                self.check_and_buy()
        finally:
            if self.driver.find_element_by_xpath('//*[@id="placeYourOrder"]'):
                self.driver.find_element_by_xpath('//*[@id="placeYourOrder"]').click()
            elif self.driver.find_element_by_xpath('//*[@id="turbo-checkout-pyo-button"]'):    
                self.driver.find_element_by_xpath('//*[@id="turbo-checkout-pyo-button"]').click()
        sleep(120)
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
