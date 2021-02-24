import csv
#create a dict of the csv file
insurances ={}
columns = []
line_one = True

with open("insurance.csv",newline="") as csv_file:
    reader = csv.reader(csv_file)
    j = 1
    for row in reader:
        internal_dict= {}
        i = 0
        if line_one:
            for column in row:
                columns.append(column)
            line_one = False
        else:
            for value in row:
                internal_dict[columns[i]] = value
                i +=1
            insurances["insurance-"+str(j)] =  internal_dict
            j +=1

def print_insurances():
    for key , values in insurances.items():
        print(key +  " values are:")
        print(values)

# Analysis start here:

# 1- BMI to Cost:

def bmi_to_cost():
    pass
# 2- Age to children:

def age_to_children():
    pass
# 3-  where the majority lives:
def find_location_of_mojority():
    pass

print_insurances()