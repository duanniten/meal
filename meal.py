def main():
    time = input("What time is it? ").strip()
    


def convert(time:str):
    timeParts = time.split(sep=":")
    hour  = float(timeParts[0])
    minutes = float(timeParts[1]) / 60
    return hour + minutes

if __name__ == "__main__":
    main()