time = int(input('За сколько секунд пробежишь марафон?: '))
hours = time / 3600
minutes = (time - hours * 3600) / 60
seconds = time - (hours * 3600 + minutes * 60)
print(f"время в формате чч:мм:сс   {hours} : {minutes} : {seconds}")