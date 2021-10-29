#https://towardsdatascience.com/write-clean-python-code-using-pipes-1239a0f3abf5
#working with iterables
# here we select divisible numbers from array using filter and apply *2 to each using map
arr = [1,2,3,4,5]
result = list(map(lambda x: x*2,filter(lambda x: x % 2 == 0 ,arr)))
print("result with map and filter:", result)

#We can do the same with pipes
#install pipe on the fly (Bad practice don't do this, use requirements.txt)
try:
    import pipe
except ModuleNotFoundError :
    from pip._internal import main as pip
    pip(['install', '--user', 'pipe',])
    import pipe

#Use a pipe | to pass the result of one method to another
result = list (arr| pipe.where(lambda x: x %2 == 0) | pipe.select(lambda x: x *2))
print("result with pipe:", result)
