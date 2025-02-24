no_boys = int(input("Enter the number of boys: "))
no_girls = int(input("Enter the number of girls: "))

boys_heights = []
girls_heights = []

# Input heights for boys
print("Enter the height of the boys:")
for i in range(no_boys):
    height1 = int(input(f"Enter the height of boy {i + 1}: "))
    boys_heights.append(height1)

# Input heights for girls
print("Enter the height of the girls:")
for i in range(no_girls):
    height1 = int(input(f"Enter the height of girl {i + 1}: "))
    girls_heights.append(height1)

# Check if boys and girls are equal in number, else it's not possible
if no_boys != no_girls:
    print("Not possible to arrange")
else:
    # Combine and sort the heights
    boys_heights.sort()
    girls_heights.sort()

    # We will attempt to alternate between boys and girls
    arranged_heights = []
    for i in range(no_boys):
        arranged_heights.append(boys_heights[i])
        arranged_heights.append(girls_heights[i])

    print("Possible alternating arrangement of heights:", arranged_heights)