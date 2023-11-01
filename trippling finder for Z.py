def trip_find(arr, Z):
    min_diff = float('inf')
    closest_pair = None
    Amin=min(arr)
   
    X=arr.index(Amin)
    print (Amin)
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if X not in [i,j]:
                q=abs(Z-arr[i] - arr[j]-Amin)
                if q < min_diff:
                    min_diff = q
                    I,J=i,j
                    
                    closest_pair = [arr[i], arr[j]]
                    
    print ("I,J",I,J)
    min_diff = float('inf')
    closest_pair1=sum(closest_pair)
    print (closest_pair1)
    for k in range(len(arr)):
        if k not in (I,J):
            q=abs(Z- closest_pair1 - arr[k])
            if q < min_diff:
                min_diff = q
                K = arr[k]
                KA=k
            print (arr[k])
            print ("q",closest_pair1 + arr[k])
    closest_pair.append(K)
    return closest_pair
    
# Example usage
arr = [2,3,4,5,8,9]
Z = 12
closest_pair = trip_find(arr, Z)
print("Closest Pair:", closest_pair)
