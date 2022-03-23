num = int(input("Your number: "))
# a = []
current = 1
is_current_bigger_than_n = False
for i in range(1, num + 1):
    # a.append(i)
    # print(a)
    for j in range(1, i + 1):

        if current > num:
            is_current_bigger_than_n = True
            break

        print(str(current) + ' ', end='')
        current += 1
    if is_current_bigger_than_n:
        break

    print()

# # initializing list
# a = [1, 2, 3, 4, 5, 6, 7]
#
# # printing original list
# print("The original list is : " + str(test_list))
#
# # initializing N
# N = 3
#
# # getting incremented chunks
# # using list comprehension as shorthand
# res = [a[0: (idx + 1) * num] for idx in range(0, len(a) // num)]
#
# # printing result
# print("Constructed Chunk Matrix : " + str(res))