cars =["kia", "lexus", "bugatti", "royce"]
msg = f"i love to own {cars[-1].upper()}"
msg1 = f"i love to own {cars[1].upper()}"
msg2 = f"i love to own {cars[0].upper()}"
msg3 = f"i love to own {cars[2].upper()}"

cars[3] = "nissan"
cars.append("honda")
cars.insert(1, "infinite")
cars.append("acura")
del cars[4]
cars.remove("kia")
cars.insert(1, "tata")
cars.pop()
cars.append("acura")
popped_cars = cars.pop()
print(cars)
cars.append("acura")
cars.pop(3)
print(f"\n{msg}\n{msg1}\n{msg2}\n{msg3}")
