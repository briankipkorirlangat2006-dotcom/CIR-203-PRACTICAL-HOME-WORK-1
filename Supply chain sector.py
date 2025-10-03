
routes = ["Nairobi", "Mombasa", "Nakuru", "Naivasha", "Nyeri",
          "Kisumu", "Eldoret", "Malindi", "Garissa", "Meru"]

print("Original Routes:", routes)
routes.append("Thika")
if "Malindi" in routes:
    routes.remove("Malindi")
print("\nAfter Adding & Removing:", routes)
routes.sort()
routes.reverse()
print("Sorted and Reversed:", routes)
count_n = sum(1 for r in routes if r.startswith("N"))
print("Routes starting with 'N':", count_n)
long_routes = [r for r in routes if len(r) > 10]
print("Routes longer than 10 characters:", long_routes)