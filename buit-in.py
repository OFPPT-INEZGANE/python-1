
#! List

myList = list(("text" , "idea" , "ista")) #[]

#* (Ordered , changable , allow duplicate) 
# * List[0]
# * List[:0]
# * List.insert(index , object)
# * List.append(object)
# * firstList.extend(secondList)
#* list.remove("value")
#* list.pop(index)
#* del list[index] || del list
#* 


#? Access
print("_________________________________________")

print(myList[1])
print(myList[1:2])

if "textg" in myList:
    print("Found 200OK!")
else:
    print("No Result 400")



#? Change List Items
print("_________________________________________")

print(myList)
# myList[0] = "test"

# myList[1:] = ["list" , "fatiha"]

# insert()
# myList.insert(-3, "test")
# Append()

# myList.append("ofppt")

# secondList = ["ofppt" , "fatiha"]

# print(myList.extend(secondList))

# remove / Pop

# myList.remove("text")
# myList.pop(0)

# del myList[2]

# myList.clear()



print(myList)

#! Tuple

#! dictionary

#! Set

#! FrozenSet