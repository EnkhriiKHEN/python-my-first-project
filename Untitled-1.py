import math

ans = "2"

while ans not in "4":
    n = int(input("ta hediiin dotor too sanasn be: "))

    print("bi tanii sanasan too hamgiin ihdee {} oroldlogo hiiged olj chadna.".format(int(math.log(n,2)+1)))

    low_n , high_n = 1, n
    i =1
    print("chance {} : tanii sanasn too {} mun u".format(i, (low_n + high_n) // 2))

    ans = input("1.zov hariult \n2. ih tooo \n3. baga too. \n4 garah.\n")

    while ans not in "14":

        if ans not in "1234":
            ans =input("1.zov hariult \n2. ih tooo \n3. baga too. \n4 garah.\n")
            continue
        i += 1
        if ans == "2":

            low_n = (low_n + high_n)//2
        elif ans == "3":
            high_n = (low_n+high_n)//2


        print("chance {} : tanii sanasn too {} mun u".format(i, (low_n + high_n) // 2))


        ans = input("1.zov hariult \n2. ih tooo \n3. baga too. \n4 garah.\n")
    if ans == "1":
        ans=input ("togloomoos garh bol  (4) tovchig darna uu\n urgeljluuleh bol random tovch drana uu")