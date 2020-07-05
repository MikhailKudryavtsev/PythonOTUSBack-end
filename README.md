**Parsing logs**

Для парсинга логов берется файл логов (`access.log`), который должен находиться в одной директории с `parsing_logs.py`.

Из лога выбирается:

    Первые 10 POST запросов;
    Первые 20 GET запросов;
    10 уникальных IP адресов;
    Запросы, которые выполнились с ошибкой 404;
    Запросы, которые выполнились с ошибкой 500;
    Все долгие запросы (более 500мс)

Полученная информация записывается json - файл (`access_log.json`).

**Socket**

Сервер получает `http запрос` через браузер и возвращает json, который содержит `request headers`.

**os sys subprocess**

 Скрипт `my_sys_info.py` выводит информацию:
 
 - Cемейство ОС;
 - Версия ядра;
 - Версия ОС;
 - Текущуя директория и список в файлов в ней;
 - Указанная директория и список в файлов в ней;
 - Список всех процессов;
 - Информация о процессе `bash`.