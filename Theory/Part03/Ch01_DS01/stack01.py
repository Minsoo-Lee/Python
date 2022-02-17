from inspect import stack


stack_data = []

# push
stack_data.append(10)
stack_data.append(20)
stack_data.append(30)
stack_data.append(40)
stack_data.append(50)
print(stack_data)

# pop
print(stack_data.pop())
print(stack_data.pop())
print(stack_data)