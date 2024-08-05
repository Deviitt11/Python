words = ["tree", "button", "cat", "window", "defenestrate"]

# Use a list comprehension to filter out words longer than four letters

# Display the filtered list

filtered = [x for x in words if len(x) > 4]

print(filtered)