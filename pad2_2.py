slownik = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, 
	{'make': 'Mi Max', 'model': 2, 'color': 'Gold'}, 
	{'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

print("Podaj po którym argumencie sortować dane:\n1 -- make\n2 -- model\n3 -- color")
option = int(input())
if option == 1:
    result = sorted(slownik, key=lambda x: x['make'])
if option == 2:
    result = sorted(slownik, key=lambda x: x['model'])
if option == 3:
    result = sorted(slownik, key=lambda x: x['color'])
print(result)