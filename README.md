# Автоматизированное тестирование веб-приложения
Данный фреймворк предназначен для создания автотестов, проверяющих работу авторизации на web-сайте.
В частности проверяется работа функциональности "Авторизация" на странице https://passport.yandex.ru.
## О проекте
Проект представляет собой пример организации автоматизированных тестов для веб-приложения с использованием паттерна Page Object, язык Python + pytest и библиотеки Selenium.

## Основные компоненты проекта:

- `tests/` - директория с тестами. Здесь размещаются тест-кейсы, использующие Page Object модели и параметризацию.
- `data/` - директория с тестовыми данными. Здесь хранятся файлы JSON, CSV или другие форматы данных, используемые в тестах.
- `pages/` - директория с Page Object моделями. Каждая модель представляет отдельную страницу или функциональный блок приложения.
- `locators/` - директория с локаторами элементов страницы. Здесь хранятся селекторы, которые идентифицируют элементы на странице.
- `conftest.py` - файл с фикстурами для настройки тестового окружения. Здесь можно настроить запуск браузера, создание сессий и другие настройки.
- При необходимости можно создать `pytest.ini` - файл с настройками pytest. Здесь можно настроить параметры запуска тестов, включая маркеры и логирование.
- `requirements.txt` - список зависимостей проекта. Указывает необходимые библиотеки и их версии.

## Запуск тестов

1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
2. Запустите тесты:
   ```bash
   pytest

## Как добавить новые тесты
1. Создайте новый файл с тестами в директории tests/.
2. Используйте Page Object модели для взаимодействия с элементами страницы.
3. Используйте параметризацию тестов с помощью @pytest.mark.parametrize для разных входных данных.

## Ограничения
> Для успешного выполнения задания, в фреймворке должны использоваться тестовые данные с сервиса jsonplaceholder. Однако, в предоставленном JSON файле с пользователями отсутствовали корректные учетные данные для авторизации, а также все номера телефонов были в неверном формате для данного сайта. Исходя из этого, я тестировал на тех данных которые я мне нужно было использовать в задании.
> Для проверки функционала авторизации через номер телефона, мне пришлось создать отдельный JSON файл, где я использовал свой собственный номер телефона. Это позволило убедиться, что функция авторизации через номер телефона вообще работает.

> Также на тестируемом веб-сайте также присутствует двухфакторная аутентификация и защита от ботов в виде капчи. Исходя из этого я условился моментом, что если я попадаю на страницу, где предлагается ввести код из SMS, то это считается успешным сценарием авторизации.
