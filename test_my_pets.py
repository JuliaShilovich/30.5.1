from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing(selenium):
   # Переходим на страницу авторизации
   selenium.get('http://petfriends.skillfactory.ru/login')

   yield

   selenium.quit()

# тест: число питомцев в таблице и в статистике одинаковое
def test_number_of_pets(selenium):

   # Вводим email
   selenium.find_element(By.ID, 'email').send_keys('lula@pochta.com')
   # Вводим пароль
   selenium.find_element(By.ID, 'pass').send_keys('123456')
   # Нажимаем на кнопку входа в аккаунт
   selenium.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

   # Неявное ожидание
   selenium.implicitly_wait(10)

   # Нажимаем на кнопку "Мои питомцы"
   selenium.find_element(By.XPATH, '//*[@href="/my_pets"]').click()

   # Неявное ожидание
   selenium.implicitly_wait(10)

   list_of_pets = WebDriverWait(selenium, 10).until(EC.presence_of_all_elements_located(
      (By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr'))
   )

   # Берем количество питомцев из статистики
   num = int(WebDriverWait(selenium, 10).until(EC.presence_of_element_located(
      (By.CLASS_NAME, 'task3'))).text.split("\n")[1].split(" ")[-1])


   # Ожидаем, что количество имен в списке равно количеству питомцев из статистики
   assert num == len(list_of_pets)



# тест: фото есть у половины моих питомцев
def test_photos_of_pets(selenium):
   # Переходим на страницу авторизации
   selenium.get('http://petfriends.skillfactory.ru/login')
   # Вводим email
   selenium.find_element(By.ID, 'email').send_keys('lula@pochta.com')
   # Вводим пароль
   selenium.find_element(By.ID, 'pass').send_keys('123456')
   # Нажимаем на кнопку входа в аккаунт
   selenium.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

   # Неявное ожидание
   selenium.implicitly_wait(10)

   # Нажимаем на кнопку "Мои питомцы"
   selenium.find_element(By.XPATH, '//*[@href="/my_pets"]').click()

   # Неявное ожидание
   selenium.implicitly_wait(10)

   # Составляем список фото
   images = WebDriverWait(selenium, 10).until(EC.presence_of_all_elements_located(
      (By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/th/img'))
   )

   # Вычисляем существующие фото
   count = 0
   for i in range(len(images)):
      if images[i].get_attribute('src') != '':
         count += 1

   # Половина питомцев
   half_photos = len(images)//2

   # Ожидаем, что питомцев с фото больше либо равно половны от общего числа питомцев
   assert half_photos <= count

# тест: у всех питомцев есть имя, порода и возраст
def test_names_ages_kinds(selenium):
   # Переходим на страницу авторизации
   selenium.get('http://petfriends.skillfactory.ru/login')
   # Вводим email
   selenium.find_element(By.ID, 'email').send_keys('lula@pochta.com')
   # Вводим пароль
   selenium.find_element(By.ID, 'pass').send_keys('123456')
   # Нажимаем на кнопку входа в аккаунт
   selenium.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

   # Неявное ожидание
   selenium.implicitly_wait(10)

   # Нажимаем на кнопку "Мои питомцы"
   selenium.find_element(By.XPATH, '//*[@href="/my_pets"]').click()

   # Неявное ожидание
   selenium.implicitly_wait(10)

   # Создаем массивы имен, пород и возрастов
   names = WebDriverWait(selenium, 10).until(EC.presence_of_all_elements_located(
      (By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[1]'))
   )

   kinds = WebDriverWait(selenium, 10).until(EC.presence_of_all_elements_located(
      (By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[2]'))
   )

   ages = WebDriverWait(selenium, 10).until(EC.presence_of_all_elements_located(
      (By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[3]'))
   )

   # Проверяем что каждый элемент этих массивов не пуст
   for i in range(len(names)):
      assert names[i].text != ''
      assert kinds[i].text != ''
      assert ages[i] != ''

# тест: у всех питомцев разные имена
def test_unique_names(selenium):
   # Переходим на страницу авторизации
   selenium.get('http://petfriends.skillfactory.ru/login')
   # Вводим email
   selenium.find_element(By.ID, 'email').send_keys('lula@pochta.com')
   # Вводим пароль
   selenium.find_element(By.ID, 'pass').send_keys('123456')
   # Нажимаем на кнопку входа в аккаунт
   selenium.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

   # Неявное ожидание
   selenium.implicitly_wait(10)

   # Нажимаем на кнопку "Мои питомцы"
   selenium.find_element(By.XPATH, '//*[@href="/my_pets"]').click()

   # Неявное ожидание
   selenium.implicitly_wait(10)

   # Массив имен
   names = WebDriverWait(selenium, 10).until(EC.presence_of_all_elements_located(
      (By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[1]'))
   )

   n = []
   for i in range(len(names)):
      n.append(names[i].text)

   uniqueList = []
   for item in n:
      itemExist = False
      for x in uniqueList:
         if x == item:
            itemExist = True
            break
      if not itemExist:
         uniqueList.append(item)

   assert uniqueList == n


