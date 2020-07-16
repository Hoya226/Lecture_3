import func_module
import func_module_as
#func_module.module_show()

nowdate = func_module.date_now()
#now_year = nowdate.year
#now_month = nowdate.month
#now_day = nowdate.day
#print(nowdate)


# date_today = '{}년 {}월 {}일'.format(nowdate.year , nowdate.month ,nowdate.day)
#print(date_today)


#start_time = datetime.datetime.now()
#start_time.replace(month = 12, day = 25)


#X_mas = nowdate.replace(month=12, day=25)

#date_Xmas = '{}년 {}월 {}일'.format(X_mas.year , X_mas.month ,X_mas.day)
#print(now_year, '년', now_month, '월', now_day, '일')

#print(date_Xmas)


#ndate = func_module_as.date_now()

#print(ndate)


re_date = func_module_as.remain_date_input(10,20)
print(re_date)