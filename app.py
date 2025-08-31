import pandas as pd
import numpy as np
from datetime import datetime


df = pd.read_csv("data/Nat_Gas.csv")
df["Dates"] = pd.to_datetime(df["Dates"], format="%m/%d/%y")
df = df.set_index(df["Dates"])
series = df["Prices"]


x = series.index.view("int64")
y = series.values


x1, x2 = x[-2], x[-1]
y1, y2 = y[-2], y[-1]
slope = (y2 - y1) / (x2 - x1)

def estimate_price(date_str):
    
    t = pd.Timestamp(date_str).value
    
    if t < x[0]:
        slope0 = (y[1] - y[0]) / (x[1] - x[0])
        return float(y[0] + slope0 * (t - x[0]))
    
    if t <= x[-1]:
        return float(np.interp(t, x, y))
    

    return float(y2 + slope * (t - x2))



def count(inject,withdraw, injection_dates, withdraw_dates, storage_day_cost,max_storage ):

    inject_list = []
    withdraw_list = []
    value = 0
    amount = 0
    inject_list = [pd.Timestamp(d) for d in injection_dates]
    withdraw_list = [pd.Timestamp(d) for d in withdraw_dates]
    if not all_dates:
        return 0.0
    all_dates = sorted(set(inject_list + withdraw_list))
    prev_date = all_dates[0]
    storage_cost = 0
    for d in all_dates:
        days = (d - prev_date).days
        if days > 0:
            storage_cost = days * storage_day_cost * amount
            value = value - storage_cost
            if d in inject_list:
                headroom = max_storage - amount
                units_in = min(inject, max(0.0, headroom))
                if units_in > 0:
                    px = estimate_price(d)
                    value -= px * units_in
                    amount += units_in
        if d in withdraw_list:
            units_out = min(withdraw, amount)
            if units_out > 0:
                px = estimate_price(d)
                value += px * units_out
                amount -= units_out
        prev_date = d
    return float(value)
            
            

