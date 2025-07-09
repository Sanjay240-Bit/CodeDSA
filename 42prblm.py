def trap(height):
    n = len(height)
    l_wall = 0
    r_wall = 0
    max_right = [0]*n
    max_left = [0]*n

    for i in range(n):
        j = -i - 1
        max_left[i] = l_wall 
        max_right[j] = r_wall

        l_wall = max(l_wall,height[i])
        r_wall = max(r_wall,height[j])

    summ = 0
    for i in range (n):
            
            
            

        pot = min(max_left[i],max_right[i])

        summ += max(0,pot - height[i])
    
    return summ
        

height = list(map(int,input("Enter the Height").split()))

result = trap(height)

print(f"Trapped water:{result}")
