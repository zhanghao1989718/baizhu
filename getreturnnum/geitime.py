import datetime

now_time = datetime.date.today()
fromDate = now_time - datetime.timedelta(days=15)
toDate = now_time - datetime.timedelta(days=8)
from_date = str(fromDate)
to_date = str(toDate)

js_fromdate_value = 'document.getElementById("train_date").'+ 'value=' + from_date

print(js_fromdate_value)