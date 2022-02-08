my_height = 178
my_weight = 65
strides_count = 1000
activity_time = 60

stride = my_height / 4 + 0.37
s = strides_count / activity_time
v = s / activity_time
consumption_energy = 0.035 * my_weight + (v**2 // my_height) * 0.029 * my_weight
distance = (v * activity_time) / 1000
if (distance > 4):
    print("Вы прошли больше 4 км. Так держать!")
elif (distance > 2):
    print("Вы прошли больше 2 км. Неплохо!")
elif (distance < 2):
    print("Вы прошли меньше 2 км. Уже устали?")

print("Пройденная дистанция: " + str(s) + " Количество сожженных калорий: " + str(consumption_energy) + " Количество пройденных км: " + str(distance))