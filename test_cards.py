from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Запускаем браузер
service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Неявные ожидания
driver.implicitly_wait(10)

try:
    # 1. Авторизация
    print("1. Авторизуемся...")
    driver.get('https://petfriends.skillfactory.ru/login')
    time.sleep(2)
    
    driver.find_element(By.ID, 'email').send_keys('vasya@mail.com')
    driver.find_element(By.ID, 'pass').send_keys('12345')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    time.sleep(3)
    
    # 2. Переходим на страницу с питомцами
    print("2. Переходим на страницу с питомцами...")
    driver.get('https://petfriends.skillfactory.ru/all_pets')
    time.sleep(2)
    
    # 3. Ищем карточки
    cards = driver.find_elements(By.CSS_SELECTOR, '.card')
    print(f"3. Найдено карточек: {len(cards)}")
    
    # 4. Проверяем первые 5
    print("4. Проверяем карточки:")
    for i in range(min(5, len(cards))):
        card = cards[i]
        
        # Используем неявные ожидания
        name = card.find_element(By.CSS_SELECTOR, '.card-title')
        desc = card.find_element(By.CSS_SELECTOR, '.card-text')
        img = card.find_element(By.CSS_SELECTOR, '.card-img-top')
        
        print(f"   {i+1}. {name.text}")
        print(f"      {desc.text}")
        print(f"      Фото: {'есть' if img.get_attribute('src') else 'нет'}")
    
    print("\n✅ Тест с неявными ожиданиями завершен!")
    
except Exception as e:
    print(f"❌ Ошибка: {e}")

finally:
    driver.quit()