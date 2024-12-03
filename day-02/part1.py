def is_safe_report(report):
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    
    
    is_increasing = all(d > 0 for d in differences)
    is_decreasing = all(d < 0 for d in differences)
    
    
    are_differences_valid = all(1 <= abs(d) <= 3 for d in differences)
    
    
    return (is_increasing or is_decreasing) and are_differences_valid


with open("day-02\input.txt", "r") as file:
    lines = file.read().strip().split("\n")


reports = [list(map(int, line.split())) for line in lines]


safe_count = sum(is_safe_report(report) for report in reports)


print(f"Number of safe reports: {safe_count}")