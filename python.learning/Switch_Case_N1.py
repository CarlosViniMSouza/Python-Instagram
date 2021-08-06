color = "green"

def color_code(code):

    match code:
        case "purple":
            print("Kotlin")
        
        case "yellow":
            print("JavaScript")
        
        case "blue":
            print("Java")

        case "white":
            print("Python")

        case "green":
            print("C#")

        case _:
            print("PHP")

color_code(color)

# Output: C#