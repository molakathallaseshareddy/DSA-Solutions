a = [2, 5, 1, 2, 3, 9, 1, 9, 3, 2]
hash_arr = [0]*13
for i in a:
  hash_arr[i] +=1

#i repeated tiimes
print("1 appears ",hash_arr[1], "times")
print("9 appears ",hash_arr[9], "times")
print("12 appears ",hash_arr[12], "times")
print("2 appears ",hash_arr[2], "times")



# String
st = "abcdeadsdsaz"
hash_arr = [0]*26
for i in st:
  value = ord(i)-ord('a')
  hash_arr[value] +=1
print(hash_arr)
value = ord('y') - ord('a')
print(hash_arr[value])


# hash map
li = [1, 2, 5, 4, 2, 9, 12]
hash_map = {}
for i in li:
  hash_map[i] = hash_map.get(i, 0)+1
print(hash_map)
print(hash_map.get(12,0))