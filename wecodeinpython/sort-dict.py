dict_sort = {
    "JavaScript": 1,
    "Java": 2,
    "C": 3,
    "C++": 4,
    "C#": 5,
    "Objective-C": 6,
    "PHP": 7,
    "Python": 8,
    "R": 9,
    "Kotlin": 10
}

sort_value = {
    k: v for k, 
        v in sorted(
            dict_sort.items(), 
            key = lambda item: item[1]
    )
}

print(sort_value)
# this program dont working corretly