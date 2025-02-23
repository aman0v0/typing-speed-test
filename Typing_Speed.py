from time import time

def tperror(prompt, inwords):
    words = prompt.split()
    errors = 0
    
    for i in range(len(inwords)):
        if i in (0, len(inwords) - 1):
            if inwords[i] == words[i]:
                continue
            else:
                errors += 1
        else:
            if inwords[i] == words[i]:
                if (inwords[i + 1] == words[i + 1]) and (inwords[i - 1] == words[i - 1]):
                    continue
                else:
                    errors += 1
            else:
                errors += 1
    return errors
    
def speed(inwords, elapsed_time):
    twords = len(inwords)
    wpm = (twords / elapsed_time) * 60  # Convert to words per minute
    return round(wpm, 2)

def elapsedtime(stime, etime):
    return round(etime - stime, 2)

if __name__ == "__main__":
    prompt = ("Programming is a skill that requires patience, practice, and perseverance.")

    print("Type this:\n", prompt, "\n")

    input("Press Enter when you are ready to check your speed!")

    stime = time()
    inprompt = input()
    etime = time()

    elapsed_time = elapsedtime(stime, etime)
    inwords = inprompt.split()

    typing_speed = speed(inwords, elapsed_time)
    errors = tperror(prompt, inwords)

    print("\nResults:")
    print(f"Total time elapsed: {elapsed_time} seconds")
    print(f"Your Average Typing Speed: {typing_speed} words per minute (wpm)")
    print(f"Total Errors: {errors}")
