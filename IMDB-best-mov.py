
import imdb
print("______________________________________________")
list_mov = imdb.IMDb()
search = list_mov.get_top250_movies()

for namess in range(50):#number 50 is best 50 filem u can see .... u can change to exp 40 or 10 or 200 :)
    
	print(search[namess]['title'])
