def main():
    time = input("What time is it? ").strip()
    time = convert(time)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <=13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinne time")
    
        

def convert(time:str):
    timeParts = time.split(sep=":")
    hour  = float(timeParts[0])
    minutes = float(timeParts[1]) / 60
    return hour + minutes

if __name__ == "__main__":
    main()