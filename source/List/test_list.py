list1=["Ánh","Thuận","Tiếp","Hoàn","Hoà"]
print(list1[2]) # tiep
print(list1[1:4]) # Thuan,Tiep,Hoan
your_list = [1, 'hi', 'greeting', 3.14]


our_list = ['123-string', [0, 1], ['str1', 'str-2'], [list1, your_list]]
print(our_list[1][1]) # 1;
print(our_list[len(our_list)-1][0]) #['Ánh', 'Thuận', 'Tiếp', 'Hoàn', 'Hoà']
print(our_list[len(our_list)-1][0][0])  #Ánh
print(list1[4::-2]) #['Hoà', 'Tiếp', 'Ánh']



my_list = [0, 1, 2, 4, 4, 5, 10]
my_list[2:4]={"THUẬN","ÁNH"}
print(my_list)  #[0, 1, 'ÁNH', 'THUẬN', 4, 5, 10]
my_list[-1]="HAHA"
print(my_list)#[0, 1, 'ÁNH', 'THUẬN', 4, 5, 'HAHA']
#my_list.reverse()
print(my_list) #['HAHA', 5, 4, 'THUẬN', 'ÁNH', 1, 0]
my_list.append(1111)
print(my_list)
my_list.extend(["Thuận","yêu","Ánh"])
print(my_list)

my_list_1 = [0, 1, 2, 4, 4, 5, 10]
my_list_1.sort(reverse=True)
print(my_list_1)
sorted(my_list_1,reverse=True)
print(my_list_1)
my_list2 = [1, 2, 5, 8, 9, 6, 7, 0]
# Lấy các phần tử là số chẵn trong list trên
so_chan_list = list(filter(lambda x: x % 2 == 0, my_list2))
print(so_chan_list)
new_list=list(x for x in my_list2 if x%2==0)
print(new_list)