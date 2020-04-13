from selenium import webdriver
import time

user = "REDACTED"
passw = 'REDACTED'

def main():
    driver = webdriver.Chrome()
    driver.get("https://secnumacademie.gouv.fr/")
    driver.find_elements_by_id("btn_access_insc")[0].click()
    driver.find_elements_by_id("login")[0].send_keys(user)
    driver.find_elements_by_id("password")[0].send_keys(passw)
    xpath = '/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/a[1]'
    driver.find_elements_by_xpath(xpath)[0].click()
    # selecting the first module
    while True:
        if input("continue ? [Y/n]") == "n":
            exit(0)
        driver.switch_to.default_content()
        driver.switch_to.frame("DEFAUT")
        driver.switch_to.frame("contents")
        iframe_id = driver.find_elements_by_id("content")[0].find_elements_by_tag_name("iframe")[0].get_attribute("id")
        driver.switch_to.frame(iframe_id)
        driver.execute_script("for(var i = 0; i < 15; i++) {document.querySelector('#Stage_menu_inferieur_bouton_suivant_hit').click()}")

if __name__ == '__main__':
    main()