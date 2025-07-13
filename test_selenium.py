from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestForm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)  # краткое implicit‑ожидание

    def test_form_submission(self):
        driver = self.driver
        driver.get("http://localhost:8000")

        #Smoke‑проверки
        self.assertEqual(driver.title, "Тестовая форма")
        self.assertTrue(driver.find_element(By.ID, "name").is_displayed())
        self.assertTrue(driver.find_element(By.ID, "email").is_displayed())
        self.assertTrue(driver.find_element(By.XPATH, "//input[@type='submit']").is_enabled())

        #Заполнение и отправка
        driver.find_element(By.ID, "name").send_keys("Alex")
        driver.find_element(By.ID, "email").send_keys("Alex@yandex.ru")
        driver.find_element(By.XPATH, "//input[@type='submit']").click()

        #Явное ожидание результата
        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element(
                (By.ID, "result-text"),
                "Привет, Alex!"
            )
        )

        #Проверки текста
        result = driver.find_element(By.ID, "result-text").text
        self.assertIn("Привет, Alex!", result)
        self.assertIn("Alex@yandex.ru", result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
