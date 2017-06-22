def main(n):
    
    n = int(input())
    if n%2 == 0:
        
        if n in range(2,5) and n > 20:
                print ("Not Wierd")
    else:
        
        print('Wierd')


if __name__ == '__main__':
   main()
