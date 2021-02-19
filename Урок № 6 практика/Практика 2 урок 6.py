all_students = {"Ivanov", "Petrov", "Sydorov", "Dymov", "Lenin","Bregnev",
                "Vetrov"}
Python = {"Ivanov", "Petrov", "Sydorov"}
FrontEnd = {"Petrov", "Dymov", "Lenin"}
FullStack = {"Lenin", "Bregnev", "Ivanov"}
Java = {"Sydorov", "Vetrov", "Dymov"}
print("студенты которые учатся в двух или более группах: " +
      str((Python & FrontEnd) | (Python & FullStack) | (Python & Java) |
          (FrontEnd & FullStack) | (FrontEnd & Java) | (FullStack & Java)))
print("студенты которые не учатся на фронтенде: " + str(all_students - FrontEnd))
print("студенты которые изучают Python или Java: " + str(Python & Java))
