def main():
    people_list = [
        {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
        {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
    ]
    new_people_list = calc_bmi(people_list)
    print(new_people_list)

def calc_bmi(people):

    bmi_list = list(map(lambda p: round(p['weight_kg']/p['height_meters'] ** 2, 1),people))
 
    for person, bmi in zip(people, bmi_list):
        person["bmi"] = bmi
        
    return people


    
if __name__ == '__main__':
    main()
