import driver

def letter(row,col):
    if(col<=(row-1)):
        return 'T'
    else:
        return 'W'

if __name__ == '__main__':
    driver.comparePatterns(letter)
