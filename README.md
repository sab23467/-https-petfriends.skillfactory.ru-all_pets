# Тесты для PetFriends

## Описание
Тесты для проверки карточек питомцев на сайте https://petfriends.skillfactory.ru/all_pets

## Файлы

### 1. test_cards.py
- Использует **неявные ожидания** (driver.implicitly_wait(10))
- Проверяет карточки питомцев
- Тестирует фото, имена и возраст

### 2. test_table.py
- Использует **явные ожидания** (WebDriverWait + expected_conditions)
- Проверяет те же карточки
- Демонстрирует другой подход к ожиданиям

## Запуск тестов

```bash
pip install selenium
python test_cards.py
python test_table.py
