all_calculations = []

newest_first = list(reversed(all_calculations))

print("=== Oldest to Newest First ===")
for item in all_calculations:
    print(item)

print()

print("=== Most Recent First ===")
for item in newest_first:
    print(item)