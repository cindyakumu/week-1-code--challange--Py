def sort_by_age(people):
    return sorted(people, key=lambda person: person[1])
 
 #example
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35), ("Diana", 20)]
sorted_people = sort_by_age(people)
print(sorted_people)

#output
#[('Diana', 20), ('Bob', 25), ('Alice', 30), ('Charlie', 35)]