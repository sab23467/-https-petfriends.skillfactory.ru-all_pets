from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

# Запускаем браузер
service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

try:
    # Объект для явных ожиданий
    wait = WebDriverWait(driver, 10)
    
    # 1. Авторизация
    print("1. Авторизуемся...")
    driver.get('https://petfriends.skillfactory.ru/login')
    time.sleep(2)
    
    driver.find_element(By.ID, 'email').send_keys('vasya@mail.com')
    driver.find_element(By.ID, 'pass').send_keys('12345')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    time.sleep(3)
    
    # 2. Переходим на страницу с питомцами
    print("2. Переходим на страницу...")
    driver.get('https://petfriends.skillfactory.ru/all_pets')
    
    # 3. Ждем заголовок (явное ожидание)
    print("3. Ждем заголовок...")
    title = wait.until(
        EC.presence_of_element_located((By.TAG_NAME, 'h1'))
    )
    print(f"   Заголовок: {title.text}")
    
    # 4. Ждем карточки (явное ожидание)
    print("4. Ждем карточки...")
    cards = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.card'))
    )
    print(f"   Найдено карточек: {len(cards)}")
    
    # 5. Проверяем первые 3
    print("5. Проверяем карточки:")
    for i in range(min(3, len(cards))):
        card = cards[i]
        name = card.find_element(By.CSS_SELECTOR, '.card-title').text
        print(f"   {i+1}. {name}")
    
    print("\n✅ Тест с явными ожиданиями завершен!")
    
except Exception as e:
    print(f"❌ Ошибка: {e}")

finally:
    driver.quit()