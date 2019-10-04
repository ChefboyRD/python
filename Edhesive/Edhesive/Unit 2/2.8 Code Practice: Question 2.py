lat = input("Enter lats: ")
lon = input("Enter lons: ")

lat_list = [float(s) for s in lat.split(',')]
lon_list = [float(s) for s in lon.split(','	)]

print(lat_list)
print(lon_list)

print('Farthest north = ' , max(lon_list))
print('Farthest west = ', min(lat_list))
print('Farthest south = ', min(lon_list))
print('Farthest east = ', max(lon_list))
