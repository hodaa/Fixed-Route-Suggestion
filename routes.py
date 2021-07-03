from math import sqrt
import timeit

start = timeit.default_timer()


# Locate the most similar neighbors
def get_neighbors(fixed_paths, suggested_path):

	min_dist =1000000
	for fixed_path in fixed_paths:
		dist = sqrt((int(fixed_path[1])- int(suggested_path[1]))**2 + (int(fixed_path[2]) - int(suggested_path[2]))**2)
		if dist < min_dist: 
			min_dist = dist
			neareast_path = fixed_path
	return neareast_path




def get_nearest_stations(input_file,output_file):

	fixed_paths = list()
	output_file = open(output_file, "a")

	with open(input_file) as input_file:
		fixed_paths_count = int(input_file.readline())  #the number of fixed routes in Swvl system.
		for i in range(fixed_paths_count):
			for s in range(int(input_file.readline())):
				fixed_paths.append(input_file.readline().replace(" ", ""))



		suggested_paths_count = int(input_file.readline()) #the number of stations in user’s suggested fixed route
		for i in range(suggested_paths_count):
			suggested_path = input_file.readline().replace(" ", "")
			neareast_path = get_neighbors(fixed_paths, suggested_path)
			
			fixed_paths.remove(neareast_path) #remove alrady taken station to reduse number of paths that we will loop to search in.
			output_file.write(suggested_path[0]+ ' '+ neareast_path[0][0]+ "\n")



	output_file.close()







# run the code
output = get_nearest_stations('input.txt','output.txt')
stop = timeit.default_timer()
print("Result is written to output.txt Time Taken is : ", stop - start)  



#remove taken point

