from bug import Bug

def main():
    bugsy = Bug(10)

    bugsy.move()   # 11
    bugsy.move()   # 12
    print(bugsy.getPosition())  # should print 12

    bugsy.turn()
    bugsy.move()   # 11
    print(bugsy.getPosition())  # should print 11

    # extra testing
    bugsy.move()   # 10
    bugsy.turn()
    bugsy.move()   # 11
    print(bugsy.getPosition())

if __name__ == "__main__":
    main()