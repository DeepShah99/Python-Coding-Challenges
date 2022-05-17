product_info = {
	"description": "shoe",
	"price": 4.56,
	"colors": ["green", "blue", "red"],
}

my_list = []
for key,value in product_info.items():
    my_list.append([key,value])  

print(my_list)

