from classes import *

shop_items = {
    "печеньки": 2,
    "сок": 3,
    "чипсы": 85,
    }

sklad_items = {
    "печеньки": 5,
    "сок": 30,
    "сыр": 10,
    "торт": 10,
    "яблоки": 5,
    }

sklad1 = Store(sklad_items)   # создаем и склад с наполнением
shop1 = Shop(shop_items)  # создаем магазин с наполнением

points = {"склад": sklad1,
          "магазин": shop1}  # создаем список точек доставки

def main():
    print("Добрый день!\n")

    while True:
        for point in points:  # печатаем содержимое точек доставки
            print(f"Сейчас в {point}:")
            for k, v in points[point].get_items().items():
                print(f"{k}: {v}")
            print('\n')

        user_input = input(  # предлааем пользователю ввести запрос
            "Введите запрос в формате 'Доставить 3 печеньки из склад в магазин'\n"
            "Введите 'стоп' или 'stop', если хотите закончть: \n"
        )

        if user_input.lower() in ['стоп', 'stop']:  # останавливаем програаму если введен стоп
            break

        try:
            request = Request(user_input, points)  #парсим запрос пользователя в объект
        except RequestError as error:
            print(error.message)  # выводим сообщение об ошибке, если запрос не валиден
            continue

        except NotPointForRequest as error:
            print(error.message)  # выводим сообщение об ошибке, если запрос не валиден
            continue

        try:
            points[request.from_].remove(request.product, request.amount)  # уменьшаем количество товара  по запросу
        except NotRequiredPosution as error:  # ошибка уменьшения товара, если нет указанного товара
            print(error.message)
            continue  # начинаем заново
        except NotRequiredCountAvailable as error:  # ошибка уменьшения товараесли недостаточно указанного товара
            print(error.message)
            continue  # начинаем заново

        # печатаем информацию о перемещеннии товара
        print(f"Нужное количество есть на {request.from_}")
        print(f"Курьер забрал {request.amount} {request.product} со {request.from_}")
        print(f"Курьер везет {request.amount} {request.product} со {request.from_} в {request.to}")
        try:
            points[request.to].add(request.product, request.amount)  # увеличиваем товар в
                                                                    # точке в соотвествии с запросом
        except NotSpaceRequired as error:  # ошибка, елси недостаточно места
            print(error.message)
            points[request.from_].add(request.product, request.amount)  # отменяем уменьшение на складе
            print(f"{request.amount} {request.product} возвращен в {request.from_}")
            continue

        except ToManyPositions as error:  # ошибка, если превышено количество номенклатуры
            print(error.message)
            points[request.from_].add(request.product, request.amount)  # отменяем уменьшение на складе
            print(f"{request.amount} {request.product} возвращен в {request.from_}")
            continue

        print(f"Курьер доставил {request.amount} {request.product} в {request.to}")


if __name__ == "__main__":
    main()
