list = [1,2,3,4,5,6,7,8,9,10]

num = 2

start = 0
end = len(list) - 1 

while start <= end:
  mid = start + (end-start)//2
  
  if list[mid] == num:
    print("True")
    exit()
  elif list[mid] < num:
    start = mid+1
  else:
    end = mid-1

print("False")
    

