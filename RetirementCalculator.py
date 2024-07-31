### Excercise 6: Retirement Calculator
import datetime
def main():
    current_year = datetime.datetime.now().year
    cur_age = int(input("What is your current age? "))
    ret_age = int(input("At what age would you like to retire? "))
    years_left = ret_age - cur_age
    ret_year = current_year + years_left
    if years_left < 0:
        print("The user can already retire!")
    else:
        print(f"You have {years_left} years left until you can retire.")
        print(f"It's {current_year}, so you can retire in {ret_year}")

main()