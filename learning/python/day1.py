#day1
name = input("what is your name? ")
study_hours = input("how many hours you will study? ")
skill = input("what skill you want to improve? ")

print("\nHello ", name, "\n") 
print("Today you'll study ", study_hours, "hours\n")
print("Every hour you invest moves you closer to becoming an AI Engineer.\n")
print("Let's build something amazing.\n")

if study_hours == "8":
    print("\n Excellent dedication!")
elif study_hours >= "5" and study_hours <= "7":
    print("\n Great consistency!")
else:
    print("\n Every hours counts! Keep going!")