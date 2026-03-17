import os
import datetime
import pandas
import collections
from dotenv import load_dotenv
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape


def calculate_years_of_work(founding_date):
    today = datetime.date.today()
    return int(today.strftime("%Y")) - founding_date  

def decline_years(years_of_winery):
    last_num = years_of_winery % 10
    prev_num = (years_of_winery // 10) % 10
    if prev_num != 1 and last_num == 1:
        return f'{years_of_winery} год'
    elif prev_num != 1 and last_num in [2, 3, 4]:
        return f'{years_of_winery} года'
    else:
        return f'{years_of_winery} лет'

def create_price():
    user_file = os.getenv('WINE_PRICE', 'wine.xlsx')
    excel_data_wine = pandas.read_excel(
        user_file,
        sheet_name='Лист1',
        usecols=['Категория', 'Название', 'Сорт', 'Цена', 'Картинка', 'Акция'],
        na_values=[], keep_default_na=False)
    wine_catalog = excel_data_wine.to_dict(orient='records')
    prices_with_category = collections.defaultdict(list)
    for wine in wine_catalog:
        category = wine['Категория']
        prices_with_category[category].append(wine)
    sorted_wines_prices = dict(sorted(prices_with_category.items()))
    return sorted_wines_prices

def main():
    load_dotenv()
    founding_date = 1920
    years_of_winery = calculate_years_of_work(founding_date)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template(os.getenv('WINE_TEMPLATE', 'template.html'))

    rendered_page = template.render(
        years_of_work=decline_years(years_of_winery),
        wines_prices=create_price(),
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
    print("index.html создан!")

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

if __name__ == '__main__':
    main()