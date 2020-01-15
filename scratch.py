def combo(a):
    index = enumerate(a)
    new_list = [p1+p2+p3 for p1,p2,p3 in (a[index-1],a[index],a[index+1])]
    print(new_list)


