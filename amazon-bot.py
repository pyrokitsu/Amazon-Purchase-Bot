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
            self.driver.get('https://www.amazon.fr/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F'
                            '%2Fwww.amazon.fr%2Fref%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth'
                            '%2F2.0%2Fidentifier_select&openid.assoc_handle=frflex&openid.mode=checkid_setup&openid'
                            '.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns'
                            '=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
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
            sleep(2)
            add = self.driver.find_element_by_xpath('//*[@id="add-to-cart-button"]')
            add.click()
            sleep(2)
            buy = self.driver.find_element_by_xpath('//*[@id="attach-sidesheet-checkout-button"]')
            buy.click()
            sleep(2)
            pay = self.driver.find_element_by_xpath('//*[@id="placeYourOrder"]')
            pay.click()
        except Exception as e:
            if e:
                print("Cannot find the {add to cart} button! Refreshing now...")
                sleep(1.5)
                clear_screen()
                self.check_and_buy()
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
