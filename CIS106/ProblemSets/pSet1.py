
def problem_1(str):
    set = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for char in str:
        if char in set:
            count = count + 1
    return count

def problem_2(s):
    bobString = 'bob'
    countBob = 0
    for index in range((len(s) - 2)):
        print(s[index:index + 3])
        if s[index:index + 3] == bobString:
            countBob = countBob + 1
    print("Number of times 'bob' occurs is: " + str(countBob))

def problem_3(s):
    begin = 0
    bigBegin = begin
    end = 1
    bigEnd = end
    while end < len(s):
        if s[end] >= s[end-1]:
            end += 1
            if(end-begin > bigEnd-bigBegin):
                bigEnd = end
                bigBegin = begin
        else:
            begin = end
            end += 1
    print("Longest substring in alphabetical order is: " + s[bigBegin:bigEnd])



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    problem_3('azcbobobegghakl')
    problem_3("abcbcd")
    problem_3("byaaizbednimxquewzgkj")
    problem_3("jlzsvfcflcdjnv")
    problem_3("abcdefghijklmnopqrstuvwxyz")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
