import driver

def letter(row,col):
    if((row==col)or((col+row==6))):
        return 'X'
    else:
        return 'O'

if __name__ == '__main__':
    driver.comparePatterns(letter)
