import json


def check_oct_point(user_input: str):# בודק מיקום נקודות וכמותם
    if user_input[0] == '.':
        return False
    elif user_input[-1] == '.':
        print('')
        return False
    counter = 0
    for item in user_input:
        if item == '.':
            counter += 1
    if counter == 3:
        return True
    print('Not enough octets')
    return False

def check_oct_number(user_input: str):#בןדק תקינות המספרים עצמם ושאין סימנים אחרים
    user_input = user_input.split('.')
    for number in user_input:
        try:
            if int(number) > 255:
                print('Number too big')
                return False
            elif int(number) < 0:
                print('You cannot enter a number less than 0.')
                return False
        except:
            print('Invalid input.')    
    return True    

def check_mask(mask: str):# בודק תקינות המאסק
    user_input = mask.split('.')
    for index in range(0, len(user_input) - 1):
        if user_input[index] < user_input[index + 1]:
            print('Incorrect mask')
            return  False
    return True    
        
def get_ip():# מקבל ip address
    while True:
        user_input = input('Enter ip address')
        if check_oct_number(user_input) and check_oct_point(user_input):
            return user_input
            
        

def get_mask():#מקבל מאסק
    while True:
        user_input = input('Enter mask')
        if check_oct_number(user_input) and check_oct_point(user_input) and check_mask(user_input):
            return user_input
        
def decimal_to_binary(number: int):
        binary = ""
        for _ in range(8):
            binary += str(number % 2)
            number = number // 2
        return binary[::-1]
    

def decimal_list_to_binary(number: str):
    binary = ''
    number = number.split('.')
    for item in number:
        item = int(item)
        binary += str(decimal_to_binary(item))
    return binary

def to_list_ip(ip: str):
    list_ip = []
    ip = ip.split('.')
    for item in ip:
        list_ip.append(int(item))
    return list_ip      

def to_CIDR(sub: str):
    biary_list = decimal_list_to_binary(sub)
    counter = 0
    for binary in biary_list:
        for num in binary:
            if num == '1':
                counter += 1
            else:
                break    
    return counter           




def make_ip_to_network(cidr: int, ip: list):#הופך את הקלט לnetwork ומחשב את כמות הhosts האפשריים
    bit = cidr % 8
    num = 8 - bit
    bit = 2 ** num

    if cidr // 8 == 3:
        new_val = (ip[3] // bit) * bit
        network = ip.copy()
        network[3] = new_val
        ip[3] = new_val
        brodcast1 = ip[3] + bit - 1
        brodcast = ip
        brodcast[3] = brodcast1
        print(f'The network is {list_to_str(network)}\nthe number of host is: {bit - 2}\nthe class is: C')
        return {'Network':list_to_str(network),
                'brodcast': list_to_str(brodcast),
                'possible_host': bit - 2,
                'Class':'C'}
    elif cidr // 8 == 2:
        possible_host = bit * 255
        new_val = (ip[2] // bit) * bit
        network = ip.copy()
        network[3] = 0
        network[2] = new_val
        brodcast1 = ip[2] + bit 
        brodcast = ip
        brodcast[2] = brodcast1
        print(f'The network is {list_to_str(network)}\nthe number of host is: {possible_host}\nthe class is: B')
        return {'Network':list_to_str(network),
                'brodcast': list_to_str(brodcast),
                'possible_host': possible_host - 2,
                'Class': 'B'}
    elif cidr // 8 == 1:
        possible_host = bit * 255 * 255
        new_val = (ip[1] // bit) * bit
        network = ip.copy()
        network[3] = 0
        network[2] = 0
        network[1] = new_val
        brodcast1 = ip[1] + bit 
        brodcast = ip
        brodcast[1] = brodcast1
        print(f'The network is {list_to_str(network)}\nthe number of host is: {possible_host}\nthe class is: A')
        return {'Network':list_to_str(network),
                'brodcast': list_to_str(brodcast),
                'possible_host': possible_host - 2,
                'Class': 'A'}

def list_to_str(ip: list):
    result = "" 
    for index in range(len(ip) -1):
        result += str(ip[index]) + '.'
    result += str(ip[-1])    
    return result    
        

def check_classless_or_classful(cidr: int):
    if cidr % 8 == 0:
        return 'classful'
    return 'classless'

file_path = 'C:\\Users\\Yosef\\vsc_project\\network_week_8\\subnet_info_10.50.200.7_209265933.txt'
def seve_data(data):
        with open(file_path,'a',encoding="utf-8") as f:
            f.write(data)
            

make_ip_to_network(26, [192, 168, 10, 130])