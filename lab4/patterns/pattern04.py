import driver

def letter(row,col):
    if((col>=3)and(col<=6)and(row>=2)and(row<=4)):
        return 'M'
    else:
        return 'S'

if __name__ == '__main__':
    driver.comparePatterns(letter)
