l1 = ["Dairy Milk", "5 Star", "Eclairs", "Kurkure", "Popcorn"]

# i = 0
# for item in l1:
#     if i%2 is not 1:
#         print(f"Jarvis buy {item}")
#     i += 1




for index, item in enumerate(l1):                         #enumerate function takes index as argument
    if index%2 is 0:
        print(f"Jarvis buy {item}")