#Write a function to find the sum of elements in a list.

list=[23,2,56,78,4]
print(sum(list))


#Write a function to find the maximum element in a list (do not use max()).

list=[4,6,8,9,20,56]
print(max(list))


#Write a function to count even numbers in a list.

def count_even(list):
    count=0
    for x in list:
        if x%2==0:
            count+=1
    return count
a=count_even([2,4,6,5,3,8,1])
print(a)


#Write a function to reverse a list without using slicing.

def reverse(list):
    result=[]
    for i in range(len(list)-1,-1,-1):
        result.append(list[i])
    return result
a=reverse([2,4,6,8])
print(a)
#Write a function to remove duplicates from a list.