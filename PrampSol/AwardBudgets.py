def find_grants_cap(grantsArray, newBudget):
  n=len(grantsArray)
  grantsArray.sort()
  grants=n
  budget=float(newBudget)
  cap=newBudget/grants
  for i in range(n):
    requirement=grants*grantsArray[i]
    if requirement>=budget:
      return budget/grants
    grants-=1
    budget-=grantsArray[i]
  return newBudget

  
grantsArray =[2,100,50,120,167]
newBudget =  400  
print(find_grants_cap(grantsArray, newBudget))

"""
TC: O(N)
SC: O(1)


N grants

newBudget, n grants as per newBudget we need to relloacte the budge

cap=> grant higher than  cap

exactly cap 

cap=> grants <= cap they won't impacted

grantsArray ,newBudget

findGrantsCap =>

eg :

grantsArray = [2, 100, 50, 120, 1000], newBudget = 190


[2,50,100,120,1000]=> 190/5=>  38 

190-2=> n-=1  n=4.  newbudget= 188=>

188/4=> 47 =>  return 47

grant=n
1) grantsArray sort array
2) n=len(grantsArray) cap=> grantsArray/n
3) grantsArray[i]<=cap:
      newBudget=newBudget-arr[i] grant-=1
   else:
        newBudget//grant

return orignal_newBudget//len(grantArray)








"""