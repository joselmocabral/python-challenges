
def string_formatter(number, string_number):
    append = ("s" if number > 1 else "")
    return str(number) + " " + string_number + append

def format_duration(seconds):
    if(not seconds):
        return "now"
    seconds_mark = (seconds % 60, "second")
    minutes_mark = ((seconds // 60) % 60, "minute")
    hour_mark = ((seconds // (60 * 60)) % 24, "hour")
    day_mark = ((seconds // (60 * 60 * 24)) % 365, "day")
    year_mark = ((seconds // (60 * 60 * 24 * 365), "year"))
    time_mark = [year_mark, day_mark, hour_mark, minutes_mark, seconds_mark]
    
    filtered_and_string = list(map(lambda x: string_formatter(x[0], x[1]), filter(lambda x: x[0] > 0, time_mark)))
    if(len(filtered_and_string) > 1):
        filtered_and_string[-1] = "and " + filtered_and_string[-1]
    if(len(filtered_and_string) > 2):
        filtered_and_string[0:-2] = map(lambda x: x + ",", filtered_and_string[0:-2])
    return " ".join(filtered_and_string)
    