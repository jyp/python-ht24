
def advance(timestamp):
    (hour,minute) = timestamp
    minute = minute + 10
    if minute >= 60:
        hour = hour + 1
        minute = minute - 60
    return (hour, minute)


#############################
## Tests
print(advance((8,50)))
print(advance((8,55)))
