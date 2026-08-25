class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # will get TLE with ileterative appriach on stack poistion 
        #best to make a stack by using time 
        # also we need to keep track of which car is forward and which is back
        # beacuse only the car at back can come in line with the front car
        # dont just sort vased on time no based on position then use time to figure
        #out who will come in line with who and the ta da ans
        cars = []
        for i in range(len(speed)):
            cars.append([position[i],speed[i]])
        cars.sort()
        stack =[]
        for i in range(len(speed)-1,-1,-1):
            ti = (target-cars[i][0])/cars[i][1]
            stack.append(ti)

            if len(stack)>1 and stack[-2]>=stack[-1]:
                stack.pop()
        return len(stack)
        