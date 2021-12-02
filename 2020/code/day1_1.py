import csv

def match_list_sum(list_obj, target_val):
    for i in range(0, len(list_obj)):
        for j in range(i, len(list_obj)):
            if list_obj[i] + list_obj[j] == target_val:
                return i,j
            else:
                continue
    raise ValueError('No matching indices found')

def main():
    list_obj = []
    with open('../inputs/day1_1_input.txt') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            list_obj.append(int(row[0]))

    i,j = match_list_sum(list_obj, 2020)

    print(list_obj[i] * list_obj[j])

    return

if __name__ == "__main__":
    main()