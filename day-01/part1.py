def calculate_location_distance(input_data):
    
    lines = input_data.strip().split('\n')
    left_list = []
    right_list = []
    
    for line in lines:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)
    
    
    left_list.sort()
    right_list.sort()
    
    
    total_distance = sum(abs(left - right) for left, right in zip(left_list, right_list))
    
    return total_distance


with open('day-01\input.txt', 'r') as file:
    input_data = file.read()


result = calculate_location_distance(input_data)
print(f"Total distance between lists: {result}")