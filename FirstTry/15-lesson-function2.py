

def create_record(name, tel, address):
    '''create record'''
    record = {
        'name': name,
        'phone': tel,
        'address': address,
    }
    return record

user1 = create_record('Vasya', '+8800283839', 'Moskva')
user2 = create_record('pEtyA'.title(), '+8889898978', 'Orsk')

print(str(user1) +'\n'+ str(user2).strip('{'+'}').replace("'",""))

def give_award(medal, *persons):
    """give medals to persons"""
    for person in persons:
        print("Comrad " + person.title() + ' nagrajdaetsa medakiyu ' + medal)

give_award("Za berlin","vasya","Petua")