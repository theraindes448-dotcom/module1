TARIFF = 25
def calculate_payment(consumption, tariff):
    payment = consumption * tariff
    return payment
def get_category(consumption):
    if consumption <= 100:
        category = "Низкий"
    elif consumption <= 200:
        category = "Средний"
    else:
        category = "Высокий"

    return category

def get_previous_reading():
   
    while True:
        try:
            previous = float(input("Введите предыдущие показания счетчика: "))

            if previous < 0:
                print("Ошибка! Показания не могут быть отрицательными.")
            else:
                return previous

        except ValueError:
            print("Ошибка! Введите число.")

def get_current_reading(previous):
    while True:
        try:
            current = float(input("Введите текущие показания счетчика: "))

            if current < previous or current - previous > 1000:
                print("Ошибка! Расход должен быть от 0 до 1000 кВт·ч.")
            else:
                return current

        except ValueError:
            print("Ошибка! Введите число.")


def print_report(previous, current, consumption, payment, category):
    print()
    print(f"{'ОТЧЕТ ПО ЭЛЕКТРОЭНЕРГИИ':^60}")
    print("-" * 60)

    print(f"{'Предыдущие показания:':<35}{previous:>15.2f} кВт·ч")
    print(f"{'Текущие показания:':<35}{current:>15.2f} кВт·ч")
    print(f"{'Расход электроэнергии:':<35}{consumption:>15.2f} кВт·ч")
    print(f"{'Тариф:':<35}{TARIFF:>15.2f} тг/кВт·ч")
    print(f"{'Сумма оплаты:':<35}{payment:>15.2f} тг")
    print(f"{'Категория потребления:':<35}{category:>15}")

    print("-" * 60)

def print_table():
    print()
    print(f"{'ТАБЛИЦА СТОИМОСТИ ЭЛЕКТРОЭНЕРГИИ':^60}")
    print("-" * 60)

    print(f"{'Расход (кВт·ч)':<20}{'Тариф (тг)':>15}{'Оплата (тг)':>25}")
    print("-" * 60)

    for number in range(1, 6):
        consumption = number * 100
        payment = calculate_payment(consumption, TARIFF)

        print(f"{consumption:<20.2f}{TARIFF:>15.2f}{payment:>25.2f}")

    print("-" * 60)

def main():
    repeat = "да"

    while repeat == "да":
        print()
        print(f"{'РАСЧЕТ ОПЛАТЫ ЭЛЕКТРОЭНЕРГИИ':^60}")
        print("-" * 60)
        previous = get_previous_reading()
        current = get_current_reading(previous)
        consumption = current - previous
        payment = calculate_payment(consumption, TARIFF)
        category = get_category(consumption)

        print_report(previous, current, consumption, payment, category)
        print_table()

        while True:
            repeat = input(
                "\nВыполнить новый расчет? (да/нет): "
            ).strip().lower()

            if repeat == "да" or repeat == "нет":
                break
            else:
                print("Ошибка! Введите 'да' или 'нет'.")

    print("\nРабота программы завершена")

main()