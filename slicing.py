my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(my_list)
print(my_list[0])
print(my_list[5])
print(my_list[-1])
print(my_list[-10])
print(my_list[0:5])
print(my_list[0:6])
print(my_list[3:8])
print(my_list[-7:-2])
print(my_list[1:-2])
print(my_list[1:])
print(my_list[5:])
print(my_list[:-1])
print(my_list[:])
print(my_list[2:-1])
print(my_list[2:-1:2])
print(my_list[2:-1:1])
print(my_list[2:-1:-1])
print(my_list[-1:2:-1])
print(my_list[-2:1:-1])
print(my_list[::-1])

sample_url = 'http://coreyms.com'
print(sample_url)

#Reverse the url
print(sample_url[0::-1])

#Get the top level domain
print(sample_url[-4:])

#Print the ur; without http://
print(sample_url[7:])

#Print the url without the http:// or the top level domain
print(sample_url[7:-4])


k = [3,4,5,6,7,8,9]
print(k[::2])
print(k[:4:2])
print(k[1::2])
