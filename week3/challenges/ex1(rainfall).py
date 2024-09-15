def input_numbers():
    numbersList = []
    while True:
        number = input("Input a number > ")
        if number == "" and numbersList !=[]:
            print("Numbers added to the list.")
            print()
            break
        else:
            try:
                numbersList.append(float(number))
            except ValueError:
                print("Invalid input.")
                print()
    return numbersList

def average(numbers):
    try:
        if len(numbers) == 0:
            print("Your list is empty.")
    except:
        print("This is not a list.")
    else:
        sum = 0
        for i in numbers:
            sum += i
        average = sum/len(numbers)
        return average

def average_segment(numbers, start, end):
    try:
        if len(numbers) == 0:
            print("Your list is empty.")
    except:
        print("This is not a list.")
    else:
        return average(numbers[start:end])

def average_weekly(numbers):
    numbers.reverse()
    start = 0
    end = 7
    weekAverages = []
    for week in range((len(numbers)//7)):
        weekAverage = average_segment(numbers, start, end)
        weekAverages.append(round(weekAverage, 2))
        start += 7
        end += 7
    return weekAverages
def average_monthly(numbers):
    numbers.reverse()
    start = 0
    end = 30
    monthAverages = []
    for month in range((len(numbers)//30)):
        monthAverage = average_segment(numbers, start, end)
        monthAverages.append(monthAverage)
        start += 30
        end += 30
    return monthAverages

def output_report(average, weekly_averages, monthly_averages):
    print(f"The average rainfall is {round(average, 2)}")
    print()

    if monthly_averages == []:
        print("There is no data for a full month to provide an average.")
        if weekly_averages == []:
            print("There is no data for a full week to provide an average.")
    for i in range(len(monthly_averages)):
        print(f"The average for Month {i+1} is {round(monthly_averages[i], 2)}")
    print()
    for i in range(len(weekly_averages)):
        print(f"The average for Week {i+1} is {round(weekly_averages[i], 2)}")


rainfall = input_numbers()


rainfallAverage = average(rainfall)
rainfallWeeklyAverages = average_weekly(rainfall)
rainfallMonthlyAverages = average_monthly(rainfall)
output_report(rainfallAverage, rainfallWeeklyAverages, rainfallMonthlyAverages)
