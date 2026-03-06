all_calculations = ['10.0 deg F is -12 deg C', '20.0 deg F is -7 deg C',
                    '30 deg F is -1 deg C', '40 deg F is 4 deg C',
                    '50.0 deg F is -10 deg C', '60.0 deg F is -16 deg C']

newest_first = list(reversed(all_calculations))

print("=== Oldest to Newest First ===")
for item in all_calculations:
    print(item)

print()

print("=== Most Recent First ===")
for item in newest_first:
    print(item)