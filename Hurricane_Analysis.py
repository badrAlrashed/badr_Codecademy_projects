# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]
# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}
def update_recorded_damages(list_of_damages):
  print("ENTERED URD")
  updated_list = []
  for damage in list_of_damages:
    if damage == "Damages not recorded":
      updated_list.append(damage)
    else:
      if "M" in damage:
        damage_split = damage.split("M")
        #print("damage split is "+ str(conversion.get("M")))
        updated_list.append(float(damage_split[0])*conversion.get("M"))
      elif "B" in damage:
        damage_split = damage.split("B")
        updated_list.append(float(damage_split[0])*conversion.get("B"))
      else:
        updated_list.append(damage)
  return updated_list

# test function by updating damages
damages = update_recorded_damages(damages)
print(damages)
# 2 
# Create a Table

# Create and view the hurricanes dictionary
def create_hurricanes_dic(names,months,years,max_sustained_winds,areas_affected,damages,deaths):
  hurricanes_dic ={}
  for i in range(len(names)):
    hurricanes_dic[names[i]] = {"Name":names[i],"Month":months[i],"Year":years[i],"Max Sustained Wind":max_sustained_winds[i],"Areas Affected":areas_affected[i],"Damage": damages[i] ,"Deaths":deaths[i]}
  return hurricanes_dic

hurricanes_dic = create_hurricanes_dic(names,months,years,max_sustained_winds,areas_affected,damages,deaths)
# 3
# Organizing by Year
def orgnize_by_year(hurricane_dic):
  hurricane_by_year = {}
  years = []
  for hurricane_name,hurricane in hurricane_dic.items():
    years.append(hurricane["Year"])
    years.sort()
  for year in years:
    for hurricane in hurricane_dic.values():
      if year == hurricane["Year"]:
        hurricane_by_year[year] = hurricane
        break
  return hurricane_by_year
# create a new dictionary of hurricanes with year and key
print("______________________________________________")
hurricane_by_year = orgnize_by_year(hurricanes_dic)
print(hurricane_by_year )

# 4
# Counting Damaged Areas
# create dictionary of areas to store the number of hurricanes involved in
def area_affected_count(hurricanes_dic):
  affected_area = {}
  for hurricanes in hurricanes_dic.values():
    for area in hurricanes["Areas Affected"]:
      if area in affected_area:
        affected_area[area] =affected_area.get(area) + 1
      else:
        affected_area[area] = 1
  return affected_area

print("SORTED AFFECTED AREA ---------------------------")
print(area_affected_count(hurricanes_dic))
# 5 
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in
def most_affected_area(hurricanes_dic):
  count_area_affected = area_affected_count(hurricanes_dic)
  max_affected_area = ""
  max_count = 0
  for area,count in count_area_affected.items():
    if count > max_count:
      max_count = count
      max_affected_area = area
  return max_affected_area , max_count
print("MAX AREA AFFECTED -----------------")
print(most_affected_area(hurricanes_dic))
# 6
# Calculating the Deadliest Hurricane
def deadliest_hurrucane(hurricanes_dic):
  max_dead_hurricane = ""
  max_death_count = 0
  for name,value in hurricanes_dic.items():
    if value["Deaths"] > max_death_count:
      max_death_count = value["Deaths"]
      max_dead_hurricane = name
  return max_dead_hurricane , max_death_count
print("DEADLIEST HURRICANE -----------------")
print(deadliest_hurrucane(hurricanes_dic))
# find highest mortality hurricane and the number of deaths

# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

# categorize hurricanes in new dictionary with mortality severity as key
def create_pair(rate,list1,hurricane):
  list1.append(hurricane)
  return {rate:list1}
def create_mortality_rank(hurricanes_dic):
  mortality_rank_dic = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for hurricane in hurricanes_dic.values():
    deaths =hurricane["Deaths"]
    list1 = []
    if deaths == 0:
     #print("-----0-----")
      mortality_rank_dic.update(create_pair(0,mortality_rank_dic[0],hurricane))
    elif deaths > 0 and deaths <= 100:
      #print("-----1-----")
      mortality_rank_dic.update(create_pair(1,mortality_rank_dic[1],hurricane))
    elif deaths > 100 and deaths <= 500:
     #print("-----2-----")
      mortality_rank_dic.update(create_pair(2,mortality_rank_dic[2],hurricane))
    elif deaths > 500 and deaths <= 1000:
      #print("-----3-----")
      mortality_rank_dic.update(create_pair(3,mortality_rank_dic[3],hurricane))
    elif deaths > 1000 and deaths <= 10000:
      #print("-----4-----")
      mortality_rank_dic.update(create_pair(4,mortality_rank_dic[4],hurricane))
    elif deaths > 10000:
      #print("-----5-----")
      mortality_rank_dic.update(create_pair(5,mortality_rank_dic[5],hurricane))
    else:
      print("ERROR : DEATHS VALUE IS NOT A NUMBER OR OUT_OF_BOUND")

  return mortality_rank_dic

print("RANK MORTLITY -------------")
print(create_mortality_rank(hurricanes_dic))
# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost
def highest_damaging_hurricane(hurricanes_dic):
  highest_damaging_hurricane = ""
  highest_cost = 0
  for name,value in hurricanes_dic.items():
    if value["Damage"] != "Damages not recorded":
      if value["Damage"] > highest_cost:
        highest_cost = value["Damage"]
        highest_damaging_hurricane = name
  return highest_damaging_hurricane , highest_cost
print("HIGHEST DAMAGING HURRICANE -----------------")
print(highest_damaging_hurricane(hurricanes_dic))

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key
def create_damage_rank(hurricanes_dic):
  damage_rank_dic = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for hurricane in hurricanes_dic.values():
    damage =hurricane["Damage"]
    list1 = []
    if hurricane["Damage"] == "Damages not recorded":
      damage = 0
    if damage == 0:
     #print("-----0-----")
      damage_rank_dic.update(create_pair(0,damage_rank_dic[0],hurricane))
    elif damage > 0 and damage <= 100000000:
      #print("-----1-----")
      damage_rank_dic.update(create_pair(1,damage_rank_dic[1],hurricane))
    elif damage > 100 and damage <= 1000000000:
     #print("-----2-----")
      damage_rank_dic.update(create_pair(2,damage_rank_dic[2],hurricane))
    elif damage > 500 and damage <= 10000000000:
      #print("-----3-----")
      damage_rank_dic.update(create_pair(3,damage_rank_dic[3],hurricane))
    elif damage > 1000 and damage <= 50000000000:
      #print("-----4-----")
      damage_rank_dic.update(create_pair(4,damage_rank_dic[4],hurricane))
    elif damage > 50000000000:
      #print("-----5-----")
      damage_rank_dic.update(create_pair(5,damage_rank_dic[5],hurricane))
    else:
      print("ERROR : damage VALUE IS NOT A NUMBER OR OUT_OF_BOUND")

  return damage_rank_dic

print("RANK DAMAGES -------------")
print(create_damage_rank(hurricanes_dic))
