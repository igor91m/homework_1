# Программа Python для конвертации секунд в часы, минуты и секунды")

time = int(input(f"Введите общее время в секундах: ")) # лично мое что только написал:) остальное что ниже взял с интернета
# Обьясните пожалуйста следующую функцию def и return.
# Как преобразовали секунды понял
def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%d:%02d:%02d" % (hour, minutes, seconds) # Вообще пока не понял как понимать:)
n = time
print(convert(n))