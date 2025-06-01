from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def create_driver():
    service = Service("msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    return driver

def test_successful_login():
    driver = create_driver()
    try:
        driver.get("https://opensource-demo.orangehrmlive.com")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )

        driver.find_element(By.NAME, "username").clear()
        driver.find_element(By.NAME, "username").send_keys("Admin")

        driver.find_element(By.NAME, "password").clear()
        driver.find_element(By.NAME, "password").send_keys("admin123")

        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
        )

        print("✅ Успішний вхід: Тест пройдено.")
        return True
    except Exception as e:
        print(f"❌ Успішний вхід: Тест не пройдено. Помилка: {e}")
        return False
    finally:
        driver.quit()

def test_failed_login():
    driver = create_driver()
    try:
        driver.get("https://opensource-demo.orangehrmlive.com")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )

        driver.find_element(By.NAME, "username").clear()
        driver.find_element(By.NAME, "username").send_keys("Admin")

        driver.find_element(By.NAME, "password").clear()
        driver.find_element(By.NAME, "password").send_keys("wrongpassword")

        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.orangehrm-login-error'))
        )

        error_text = driver.find_element(By.CSS_SELECTOR, 'div.orangehrm-login-error').text
        if "Invalid credentials" in error_text or "Invalid" in error_text:
            print("✅ Помилковий вхід: Тест пройдено (помилка виявлена).")
            return True
        else:
            print("❌ Помилковий вхід: Тест не пройдено (неправильне повідомлення).")
            return False
    except Exception as e:
        print(f"❌ Помилковий вхід: Тест не пройдено. Помилка: {e}")
        return False
    finally:
        driver.quit()

def test_redirect_after_login():
    driver = create_driver()
    try:
        driver.get("https://opensource-demo.orangehrmlive.com")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )

        driver.find_element(By.NAME, "username").clear()
        driver.find_element(By.NAME, "username").send_keys("Admin")

        driver.find_element(By.NAME, "password").clear()
        driver.find_element(By.NAME, "password").send_keys("admin123")

        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("/web/index.php/dashboard/index")
        )

        current_url = driver.current_url
        if "/web/index.php/dashboard/index" in current_url:
            print("✅ Перехід після входу: Тест пройдено (правильна сторінка).")
            return True
        else:
            print(f"❌ Перехід після входу: Тест не пройдено (поточна URL: {current_url}).")
            return False
    except Exception as e:
        print(f"❌ Перехід після входу: Тест не пройдено. Помилка: {e}")
        return False
    finally:
        driver.quit()

if __name__ == "__main__":
    test_successful_login()
    test_failed_login()
    test_redirect_after_login()