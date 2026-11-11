#m1
# import json
# with open("matematika.json") as ptr:
#     data=json.load(ptr)
#     for fan in data:
#         if "Matematika" in fan['subjects']:
#             print(fan['name'])





#m2
# import json
# with open("test.json") as ptr:
#     data=json.load(ptr)
#     print(f"Umumiy narx: {data['narx']*data['son']}")






#m3
# import json
# with open("test.json") as ptr:
#     data=json.load(ptr)
#     print(max(data,key=data.get))





#m4
# import json
# with open("test.json") as ptr:
#     data=json.load(ptr)
#     for narx in data:
#         if 500<=narx["price"]<=1000 and narx["is_available"]:
#             print(narx["id"],narx["material"])






# #m5
# import json
# with open("test.json") as ptr:
#     data=json.load(ptr)
#     new=[]
#     for i in data:
#         if i["is_available"]==True:
#             new.append(i)
# print(sorted(new, key=lambda x:x["price"]))





#m6
# import json
# with open("test.json") as ptr:
#     data=json.load(ptr)
#     for qiymat in data:
#         if qiymat["is_available"]==False and qiymat["price"]<1000:
#             print(qiymat["material"])
            


#m7
# import json
# with open("vazifa.json") as ptr:
#     data=json.load(ptr)
#     new=[]
#     for shaxs in (data["people"]):
#         new.append(shaxs["name"])
# print(new)
    




#m8
# import json
# with open("vazifa.json") as ptr:
#     data=json.load(ptr)
#     new=[]
#     for yosh in (data["users"]):
#         new.append(yosh["age"])
# print(sum(new))





#m9
# import json
# with open("vazifa.json") as ptr:
#     data=json.load(ptr)
#     for narx in (data["products"]):
#         print(narx["price"])





#m10
# import json
# with open("vazifa.json") as ptr:
#     data=json.load(ptr)
# name=max(data["people"],key=lambda x:x["age"])
# print(name["name"])






#m11
# import json
# with open("vazifa.json") as ptr:
#     data=json.load(ptr)
#     new=[]
#     for raqam in (data["contacts"]):
#         new.append(raqam["phone"])
# print(new)




#m12
# import json
# with open("vazifa.json") as ptr:
#     data=json.load(ptr)
#     for ball in (data["students"]):
#         print(f"{ball['name']} : {sum(ball["grades"])//len(ball["grades"])}")





#m13
# import json
# with open("vazifa.json") as ptr:
#     data=json.load(ptr)
#     for rol in (data["users"]):
#         if rol["role"]=="admin":
#             print(rol["name"])





#m14
# import json
# with open("vazifa.json") as ptr:
#     data=json.load(ptr)
#     new=[]
#     for key,value in data["categories"].items():
#         new.append(key,len(value))

# print(max(new))




#m15
# import json
# with open("vazifa.json") as ptr:
#     data=json.load(ptr)
#     new=[]
#     for date in (data["people"]):
#         if "s" in date["name"].lower():
#             new.append(date["name"])
# print(new)






#m16
# import json
# with open("vazifa.json") as ptr:
#     data=json.load(ptr)
#     summa=0
#     for key,value in data["departments"].items():
#         print(f"{key}:{len(value)}")






#m16
# import json
# with open("vazifa.json") as ptr:
#     data=json.load(ptr)
#     new={}
#     for ball in data["orders"]:
#         customer=ball["customer"]
#         amount=ball["amount"]
#         if customer not in new:
#             new[customer]=amount

#         else:
#             new[customer]+=amount
# print(new)



