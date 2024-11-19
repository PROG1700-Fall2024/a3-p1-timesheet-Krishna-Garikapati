#Program 1 – Timesheet
#Description:   Design and write a program that accepts the number of hours worked on 
#               each of five work days from the user, then displays different 
#               information calculated about those entries as output. 

#Student #:     w0502117
#Student Name:  krishna Priyanka, Garikapati

def WorkHours():
    Day=[1,2,3,4,5]
    hours=[]
    
    #we need input for each day. So using for loop. Also lets add all the values in hours list.
    for i in range(len(Day)):
        hour= int(input("Enter hours worked on Day #{0}:".format(Day[i])))
        hours.append(hour)


    #we need find max of all values entered in hours list so use max()
    highest=max(hours)
    # Since index +1 position indicates the day number at which value is entered. I need to find index at which my max value is in hours list and then add 1 to it.
    ind=(hours.index(highest))+1
    #print the max hours corresponding the day number worked.
    print("\nThe most hours worked was on:\n Day #{1} when you worked {0} hours.".format(highest, ind))

    #total number of hours worked can be calculated using sum function.
    TotalHours=sum(hours)
    print("\nThe total number of hours worked was: {0}".format(TotalHours))

    #Average hours worked on each day can be done by sum of hours/length of hours
    Avghours=TotalHours/(len(hours))
    print("The average number of hours worked each day was: {0:.1f}".format(Avghours))

    #Days you slacked off 
    print("\nDays you slacked off (i.e. worked less than 7 hours):")
    for j in range(len(hours)):
        if hours[j]<7:
            val=j+1
            print("Day #{0}: {1} hours".format(val,hours[j]))





def main():

    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    
    WorkHours()
    

    # YOUR CODE ENDS HERE

main()