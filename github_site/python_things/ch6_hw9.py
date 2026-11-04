name = input("What's your name?: ")
hobbiesig = input("Describe yourself: ")

with open(name+".html", "w") as f:
    f.writelines(f"<html>\n<head>\n</head>\n<body>\n  <center>\n  <h1>{name}</h1> \n</center>\n<hr  /> {hobbiesig}\n<hr  />\n</body>\n</html>")

with open(name+".html", "r") as f:
    print(f.read())