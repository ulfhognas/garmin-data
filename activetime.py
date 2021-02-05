def get_sec(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + float(s)

def get_speed(s, d):
    if d > 0:
        speed = d*1000/s
        return speed
    pass

def get_time(secs):
    s = round(secs%60)
    m = int(((secs - s) / 60)%60)
    h = int(secs)//3600
    #print(h,m,s)
    sep=':'
    return sep.join([str(h).zfill(2),str(m).zfill(2),str(s).zfill(2)])
