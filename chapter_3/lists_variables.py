#we can use values in a list directly with f-strings by noting their index position

names = ["Nick", "Coco", "Taco", "Belle"]

message = f"{names[0]} lives with {names[1]} and their two cats {names[2]} and {names[3]}"

print(message)