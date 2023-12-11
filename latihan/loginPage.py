from selenium.webdriver.common.by import By

class TestLogin:
    def __init__(self, driver):
        self.name = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.button = (By.ID, "login-button")
        self.sukses=(By.XPATH,"//span[@class='title']")
        self.gagal=(By.XPATH,"//h3[@data-test='error']")
        self.driver = driver  # Menggunakan objek driver dari fixture

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, usernamenya, passwordnya):
        self.driver.find_element(*self.name).send_keys(usernamenya)
        self.driver.find_element(*self.password).send_keys(passwordnya)
        self.driver.find_element(*self.button).click()

    def login_password(self,passwordnya):
        self.driver.find_element(*self.password).send_keys(passwordnya)
        self.driver.find_element(*self.button).click()
    def get_sukses(self):
        return self.driver.find_element(*self.sukses)
    def get_gagal(self):
        return self.driver.find_element(*self.gagal)
    def screenshots(self,namaphoto):
        return self.driver.save_screenshot(f"{namaphoto}.png")
#digunakan supaya bisa memakai quit secara flexibel
    def quit(self):
        if self.driver:
            self.driver.quit()
