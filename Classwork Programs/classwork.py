def main():
    my_list = [1,2,3,4,5,6,7,8,9,10]
    total = sum(my_list)
    for each_element in range(11):
        print(each_element)
    print(total)

    total2 = 0
    for element in my_list:
        total2 += element
    print(total2)

    total3=0
    index =0
    while index < len(my_list):
        total3 += my_list[index]
        index += 1
    print(total3)

    list_exercise(my_list)

def list_exercise(para_list):
    para_list[0] = 200

main()
