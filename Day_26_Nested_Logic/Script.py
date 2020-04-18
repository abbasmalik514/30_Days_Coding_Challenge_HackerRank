def get_fine(return_date, due_date):

    late_years=return_date[2]-due_date[2]
    if (late_years==0):
        late_months = return_date[1]-due_date[1]
        if(late_months==0):
            late_days =  return_date[0]-due_date[0]
            if late_days<1:
                return 0
            else:
                return 15*late_days
        elif 0<late_months:
            return 500*late_months
        else:
            return 0
    elif 0<late_years:
        return 10000
    else:
        return 0

if __name__=='__main__':
    return_date = list( map(int, input().split()))
    due_date = list(map(int,input().split()))
    print(get_fine(return_date, due_date))
