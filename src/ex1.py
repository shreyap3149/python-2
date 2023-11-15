def ex1():
    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    sort_people(people_list, 'weight', 'desc')
    print(people_list)

    

def sort_people(people, field, direction):
    if(direction=="asc"):
        people.sort(key=lambda x: x[field])
    else:
        people.sort(key=lambda x: x[field], reverse = True)
      

def main():
    ex1()


if __name__ == '__main__':
    main()
