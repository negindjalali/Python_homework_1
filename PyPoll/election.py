import pathlib
import csv
csvpath = pathlib.Path('/Users/negindjalali/Desktop/USC/Curriculum/usc-la-virt-data-pt-06-2021-u-c/unit_03_python/homework/PyPoll/Resources/election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    print(csvreader)
   
    Candidates=[]
    cities =[]
    khan=[]
    Correy = []
    Li = []
    Otooley = []
    total= []


    csv_header = next(csvreader)
    #print(csv_header)
    
    for row in csvreader:
        total.append(row[0])
        cities.append(row[1])
        Candidates.append(row[2])

    total_votes = len(total)
    #print(total_votes)

    for i in Candidates:
        if i == "Khan":
            khan.append(Candidates)
            khan_votes = len(khan)
        elif i == "Correy":
            Correy.append(Candidates)
            Correy_votes = len(Correy)
        elif i == "Li":
            Li.append(Candidates)
            Li_votes = len(Li)
        elif i == "O'Tooley":
            Otooley.append(Candidates)
            Otooley_votes = len(Otooley)
#print(khan_votes)
#print(Correy_votes)
#print(Li_votes)
#print(Otooley_votes)
khan_percentage =  (khan_votes/ len(total)*100)
#print(khan_percentage)
Li_percentage = Li_votes/ len(total)*100
Correy_percentage = Correy_votes/ len(total)*100
Otooly_percentage = Otooley_votes/ len(total)*100 

print("Election Results")
print("=========")
print(f"Total number of votes is {total_votes}")
print("=========")
print(f" The total number of the votes for each candidate is as follows:")
print(f" Khan: {khan_percentage} with the total of {khan_votes} votes")
print(f"Correy: {Correy_percentage} with the total of {Correy_votes} votes")
print(f"Li: {Li_percentage} with the total of {Li_votes} votes ")
print(f"O'tooly: {Otooly_percentage} with the total of {Otooley_votes} votes")
print("-----------------")
print("the winner is Khan")
print("-----------------")


    

