a = [2, 5, 1, 2, 3, 9, 1, 9, 3, 2]
hash_arr = [0]*13
for i in a:
  hash_arr[i] +=1

#i repeated tiimes
print("1 appears ",hash_arr[1], "times")
print("9 appears ",hash_arr[9], "times")
print("12 appears ",hash_arr[12], "times")
print("2 appears ",hash_arr[2], "times")