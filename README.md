# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

- Cкачайте архив с кодом или клонируйте публичный репозиторий:
```
git clone https://github.com/IgorVinogradov1/wine-master
```
- Перейдите в папку с кодом:
```
cd ...\wine-master
```
- Создайте и активируйте виртуальное окружение
```
python -m venv venv

для Windows:
venv\Scripts\activate
для Linux/Mac:
source venv/bin/activate
```
- Установите зависимости:
```
pip install -r requirements.txt
```
- Запустите сайт командой в консоли:
```
python main.py
```
Появится сообщение: `index.html создан!`
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000) или откройте в браузере файл `index.html`

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
