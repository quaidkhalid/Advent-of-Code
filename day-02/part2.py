def is_safe_report(report):
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    
    
    is_increasing = all(d > 0 for d in differences)
    is_decreasing = all(d < 0 for d in differences)
    
    
    are_differences_valid = all(1 <= abs(d) <= 3 for d in differences)
    
    
    return (is_increasing or is_decreasing) and are_differences_valid


def can_be_safe_with_removal(report):
    n = len(report)
    for i in range(n):
        # Create a new report by removing the i-th level
        modified_report = report[:i] + report[i+1:]
        # Check if the modified report is safe
        if is_safe_report(modified_report):
            return True
    return False


with open("day-02\input.txt", "r") as file:
    lines = file.read().strip().split("\n")


reports = [list(map(int, line.split())) for line in lines]


safe_count = 0
for report in reports:
    if is_safe_report(report) or can_be_safe_with_removal(report):
        safe_count += 1


print(f"Number of safe reports with Problem Dampener: {safe_count}")