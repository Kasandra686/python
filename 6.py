first_day_km = int(input("Сколько км пробежал спортсмен в первый день: "))
max_result_km = int(input("Какой результат спортсмен должен достигнуть км: "))
day = 1
while first_day_km < max_result_km:
    day += 1
    first_day_km = first_day_km / 10 + first_day_km
print(f" на {day} день спо2ртсмен пробежит {first_day_km:.2f} км")
