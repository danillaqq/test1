
total_seconds1 = 6785
days1 = total_seconds1 // 86400
hours1 = (total_seconds1 % 86400) // 3600
minutes1 = (total_seconds1 % 3600) // 60
seconds1 = total_seconds1 % 60

total_seconds2 = 456789
days2 = total_seconds2 // 86400
hours2 = (total_seconds2 % 86400) // 3600
minutes2 = (total_seconds2 % 3600) // 60
seconds2 = total_seconds2 % 60

total_seconds3 = 86401
days3 = total_seconds3 // 86400
hours3 = (total_seconds3 % 86400) // 3600
minutes3 = (total_seconds3 % 3600) // 60
seconds3 = total_seconds3 % 60
# Виведення результатів
print(f"{days1} day(s), {hours1} hour(s), {minutes1} minute(s), {seconds1} second(s).")
print(f"{days2} day(s), {hours2} hour(s), {minutes2} minute(s), {seconds2} second(s).")
print(f"{days3} day(s), {hours3} hour(s), {minutes3} minute(s), {seconds3} second(s).")
