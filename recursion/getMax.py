#list=[4,6,9,2,5]
#find the max value from list
def get_max(list,left,right):

    if left == right:
        return list[left]

    mid = int((left+right)/2)
    max_left = get_max(list,left,mid)
    max_right = get_max(list,mid+1,right)
    return  max(max_left,max_right)

list=[4,6,9,2,5]

print(get_max(list,0,len(list)-1))