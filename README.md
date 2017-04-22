# Readme

Программа проверяет входит ли адрес в зону доставки с указанными условиями.
#### Описание алгоритма
- pass

#### Вход
В папке с программой должны лежать три файла

- Файл с координатами зеленой зоны. В одной строчке должны находиться координаты только одной точки в формате 37.839218 в.д. 55.719345 с.ш.. Файл должен называться green_zone, без расширения.
- Файл с координатами желтой зоны. В одной строчке должны находиться координаты только одной точки в формате 37.839218 в.д. 55.719345 с.ш.. Файл должен называться yellow_zone, без расширения.
- Файл с информацией о заказах, которые нужно проверить. Файл должен называть clients_coordinate, без расширения. В файле построчно должны содержаться данные в следующем формате: C24150-9 10000 55.7312339 37.4714044 , где C24150-9 - номер заказа, 10000 - сумма заказа, 55.7312339 37.4714044 - координаты указанного формата (с.ш., в.д.) Данные должны располагаться через пробел.

#### Описание функций

`load_zone_coordinates` - загружает координаты из файлов **green_zone** и **yellow_zone**. Возвращает списки координат.
`load_orders_information` - загружает данные о заказах из файла **clients_coordinate**. Возвращает массив элементов с данными.
`include_in_polygon` - проверяет входит ли точка в заданную область. Функция принимает координаты точки и два списка координат заданной области - список координат по оси **X** и список координат по оси **Y**. Возвращает булево значение **True** или **False**.
`make_decision` - принимает решение по каждому заказу. Получает на вход информацию о заказе, и по два списка для каждой из зон доставки: список координат по оси **X** и список координат по оси **Y**.

#### Ближайшие обновлнения
- Чтение и запись в csv файл;
- Избавиться от предварительной выгрузки файлов в память, реализовать горячее построчное чтение;

#### Полезные ссылки

| Ссылка | Описание |
| ------ | ------ |
| [maps.ya.ru] | Карта с областями |
| [the-mostly.ru] | Онлайн конвертер для перевода географических координат между десятичным форматам и форматом градусы/минуты/секунды |


   [maps.ya.ru]: <https://yandex.ru/maps/213/moscow/?um=constructor%3A1dTiI3ahnaYIorbtuf6gB6D_8pR2Wvzl&ll=37.551753%2C55.743583&z=11&l=map&mode=usermaps>
   [the-mostly.ru]: <http://the-mostly.ru/konverter_geograficheskikh_koordinat.html>
