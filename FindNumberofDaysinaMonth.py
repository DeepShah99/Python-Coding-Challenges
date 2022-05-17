month = "Jan"
days_31 = ["Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"]
days_30 = ["Apr", "Jun", "Sep", "Nov"]
if month in days_31:
    print(month + " has 31 days")
elif month in days_30:
    print(month + " has 30 days")
else:
    print(month + " has 28 days")