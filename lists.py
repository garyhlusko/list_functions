import csv


def list_split(list_name,split):
	for i in xrange(0,len(l), n):
		yield l[i:i+n]
		
def list_transpose(list_name):
	zip(*A)

def sum_row(line):
	summ = 0
	for item in line:
		try:
			item = float(item)
			summ = summ +item
		except:
			pass
		
	return summ
	
def list_write(list_sort,column):
	headers = list_sort[0]
	list_sort.remove(list_sort[0])
	sort_list = []
	set_list = []
	for line in list_sort:
		sort_list.append([line[column],line])
		set_list.append(line[column])
	set_list = set(set_list)
	for item in set_list:
		path = "C:\Users/valued/Documents/sort_folder/sorted_list_"+str(item)+".csv"
		with open(path,"wb+") as csvfile:
			scribe = csv.writer(csvfile, delimiter =',')
			scribe.writerow(headers)
			for line in list_sort:
				if line[column] == item:
					scribe.writerow(line)
				else:
					pass