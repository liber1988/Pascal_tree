num_raw=input("Enter num of raws:")
if num_raw==0:
    print("You made a mistake try again:")

else:
    num_raw=int(num_raw)
    num_matrix=[[0]*(2*num_raw-1) for _ in range(num_raw)]
    num_matrix[0][num_raw-1]=1

    for j in range(1,num_raw):

        for i in range(2*num_raw-1):
            if i==0 :
                num_matrix[j][i]=num_matrix[j-1][i+1]
            elif i==2*num_raw-2:
                num_matrix[j][i]=num_matrix[j-1][i-1]
            else:
                num_matrix[j][i]=num_matrix[j-1][i-1]+num_matrix[j-1][i+1]
    t=0
    for i in num_matrix:
        i=[j for j in i if j!=0]

        print(" "*(num_raw-t),i)
        if t<=num_raw:
            t+=1


