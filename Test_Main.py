import csv
#import matplotlib.pyplot as plt
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

#print insurances dict
def print_insurances():
    for key , values in insurances.items():
        print(key +  " values are:")
        print(values)

#helping function
def create_list_from_dict_key(column):
    column_list = []
    for insurance in insurances.values():
        column_list.append(insurance[column])
    return column_list

def avarage(temp_list):
    sum = 0 
    for value in temp_list:
        sum += int(value)
    return round(float(sum / len(temp_list)),1)

## Analysis start here:

# 1- BMI to Cost:

def bmi_to_cost():
    bmi = create_list_from_dict_key("bmi")
    charges = create_list_from_dict_key("charges")
    plt.plot(bmi,charges)
    plt.xlabel("BMI")
    plt.ylabel("Insurances Charges")
    plt.title("BMI TO CHARGES GRAPH")
    plt.show()

# 2- Age to children:

def age_to_children():
    age = create_list_from_dict_key("age")
    children = create_list_from_dict_key("children")
    plt.plot(age,children)
    plt.xlabel("Age")
    plt.ylabel("Number of children")
    plt.title("AGE TO CHILDREN GRAPH")
    plt.show()

# 3-  where the majority lives:
def find_location_of_mojority():
    regions = {}
    for insurance in insurances.values():
        region = insurance["region"]
        if region in regions:
            count = regions[region] +1
        else:
            count = 1
        regions[region] = count
    max = 0
    region_max = ""
    for region,n in regions.items():
        if n > max:
            max = n 
            region_max = region
    return region_max , max

#EXTRA analysis
def avarage_age():
    return avarage(create_list_from_dict_key("age"))

def smoker_vs_nosmoker():
    smoker_list = create_list_from_dict_key("smoker")
    charges_list = create_list_from_dict_key("charges")
    sum_smoker = 0
    sum_nosmoker = 0
    smoker_num = 0
    nosmoker_num = 0

    for i in range(len(smoker_list)):
        if smoker_list[i] == "yes":
            sum_smoker += float(charges_list[i])
            smoker_num += 1
        else:
            sum_nosmoker += float(charges_list[i])
            nosmoker_num += 1

    avg_smoker = sum_smoker / smoker_num
    avg_nosmoker = sum_nosmoker / nosmoker_num

    if avg_smoker > avg_nosmoker:
        print("The cost of insurances for smoker on avarage is higher then none smoker for a ratio of " + str(round(avg_smoker/avg_nosmoker,1)))
    else:
        print("The cost of insurances for smoker on avarage is lower then none smoker for a ratio of " + str(round(avg_smoker/avg_nosmoker,1)))

def avg_age_with_children():
    age_with_children_list = []
    age_list = create_list_from_dict_key("age")
    children_list = create_list_from_dict_key("children")

    for i in range(len(age_list)):
        if int(children_list[i]) > 0:
            age_with_children_list.append(age_list[i])
    return avarage(age_with_children_list)

## TESTING ----------------------------------------------------------
#print_insurances()
print("------------------------------------")
max_region,max = find_location_of_mojority() 
print("The most populated region with a population of {max} is {max_region}".format(max = max, max_region = max_region))
#print("------------------------------------")
#print("In this graph you can see the reation between  BMIs and insurance charges") #not Tested
#bmi_to_cost()
#print("------------------------------------") #not Tested
#age_to_children()
print("------------------------------------")
print("The average age of the patients in the dataset is " + str(avarage_age()))
print("------------------------------------")
print("Looking at the different costs between smokers vs. non-smokers:")
smoker_vs_nosmoker()
print("------------------------------------")
print("The average age for someone who has at least one child in this dataset is " + str(avg_age_with_children()) )