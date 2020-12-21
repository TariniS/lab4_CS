import driver

def letter(row,col):
    if((col>=4)and(col<=9)and(row>=2)and(row<=3)):
        return 'Z'
    elif((col>=4)and(col<=6)and(row>=4)and(row<=5)):
        return 'Z'
    elif((col>=7)and(col<=9)and(row>=4)and(row<=5)):
        return 'X'
    elif((col>=10)and(col<=12)and(row>=4)and(row<=5)):
        return 'B'
    elif((col>=7)and(col<=12)and(row==6)):
        return 'B'
    else:
        return 'T'

if __name__ == '__main__':
    driver.comparePatterns(letter)
