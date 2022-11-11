
def pyramid():
    line = input()
    number_of_blocks = int(line)

    height = 0
    base = 1

    while number_of_blocks >= (base)**2:
        number_of_blocks -= (base**2)

        if(number_of_blocks < 0):
            height -= 1
        else:
            height += 1
        
        base += 2

    return height

if __name__ == "__main__":
    print(pyramid())