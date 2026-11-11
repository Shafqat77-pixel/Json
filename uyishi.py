#uyishi1
# import json


# with open("uyishi.json") as ptr:

#     data = json.load(ptr)

#     sum_price = 0
#     for user in data:
#         for item in user['items']:
#             sum_price += item['price'] * item['quantity']



#     print(f"Yakuniy narx : {sum_price}")

    # max_price = -1
    # max_customer = data[0]['customer_name']
    # for user in data:
    #     user_max = max(user['items'],key=lambda x: x['price'])
    #     if user_max['price'] > max_price:
    #         max_price = user_max['price']
    #         max_customer = user['customer_name']


    # print(f"Max user : {max_customer} : {max_price}")






#uyishi2
# import json
# with open("uyishi.json") as ptr:
#     data=json.load(ptr)
    # for name in data:
    #     if name["category"]=="Pizza":
    #         print(f"{name}")
    # for narx in data:
    #     if narx["price"]>max_price:
    #         max_price=narx["price"]
    
    # max_price=max(data,key=lambda x:x["price"])
    # min_price=min(data,key=lambda x:x["price"])
    # print(f"Eng qimmat: {max_price}\nEng arzon: {min_price}")





#uyishi3
# import json
# with open("uyishi.json") as ptr:
#     data=json.load(ptr)
#     print(data)
#     print(f"Eng qimmat reys: {max(data,key=lambda x:x["price"])}")
#     print(f"Eng arzon reys: {min(data,key=lambda x:x["price"])}")
   
#     jami=0
#     for orin in data:
#         jami+=orin["seats"]
# print(f"Jami orinlar soni: {jami}-ta")






#uyishi4
# import json
# with open("uyishi.json") as ptr:
#     data=json.load(ptr)
    # for havo in data:
    #     print(havo["temperature"])
# issiq=max(data,key=lambda x:x["temperature"])
# print(f"Eng issiq shar: {issiq["city"]}:{issiq["temperature"]}-gradus")
# orta=[]
# for i in data:
#     orta.append(i["temperature"])
# print(f"O'rtacha harorat: {sum(orta)//len(orta)}-gradus")




#uyishi5
# import json
# with open("uyishi.json") as ptr:
#     data=json.load(ptr)
#     #ptr(data)
#     # for fan in data:
#     #     if "Python" in fan["courses"]:
#     #         print(fan)
#     Math=0
#     Data_Science=0
#     c=0
#     Database=0
#     Python=0
#     Ai=0
#     Cyber=0
#     Web=0
#     Mashine=0
#     English=0
#     Fizika=0
#     for kurs in data:
#         if "Math" in kurs["courses"]:
#             Math+=1
#         if "Data Science" in kurs["courses"]:
#             Data_Science+=1
#         if "C#" in kurs["courses"]:
#                     c+=1
#         if "Database" in kurs["courses"]:
#                     Database+=1
#         if "Python" in kurs["courses"]:
#                     Python+=1
#         if "AI" in kurs["courses"]:
#                     Ai+=1
#         if "Cybersecurity" in kurs["courses"]:
#                     Cyber+=1
#         if "Web Development" in kurs["courses"]:
#                 Web+=1
#         if "Machine Learning" in kurs["courses"]:
#                 Mashine+=1
#         if "English" in kurs["courses"]:
#                 English+=1
#         if "Physics" in kurs["courses"]:
#                 Fizika+=1
# print(f"Matematika: {Math}-ta") 
# print(f"Data Science: {Data_Science}-ta") 
# print(f"C: {c}-ta")
# print(f"Database: {Database}-ta") 
# print(f"Python: {Python}-ta") 
# print(f"AI: {Ai}-ta") 
# print(f"Cyber: {Cyber}-ta") 
# print(f"Web: {Web}-ta")
# print(f"Mashine: {Mashine}-ta")
# print(f"English: {English}-ta") 
# print(f"Fizika: {Fizika}-ta") 
 
            
                    
        