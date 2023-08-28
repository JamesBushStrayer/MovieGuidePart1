# James Alan Bush (SU200619706)
# CIS261002VA016-1236-001
# Lab: Movie Guide Part 1

def movie_guide():
    print("The Movie List program\n")
    print("COMMAND MENU")
    print("list - List all movies")
    print("add  - Add a movie")
    print("del  - Delete a movie")
    print("exit - Exit program\n")
    
def list(movie_list):
    for i, movie in enumerate(movie_list, start = 1):
        print(f"{i}. {movie}\n")
        
def add(movie_list):
    movie = input("Name: ")
    movie_list.append(movie)
    print(f"{movie} was added.\n")
    
def delete(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number.\n")
    else:
        movie = movie_list.pop(number - 1)
        print(f"{movie} was deleted.\n")
        
def main():
    movie_list = ["Star Wars", "Raiders of the Lost Ark", "E.T."]
    movie_guide()
    while True:
        command = input("Command: ")
        if command.lower() == "list":
            list(movie_list)
        elif command.lower() == "add":
            add(movie_list)
        elif command.lower() == "del":
            delete(movie_list)
        elif command.lower() == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.")
    
if __name__ == "__main__":
    main()