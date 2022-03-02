answer = "b....b"
i=0
while i < len(answer)-1:
    print(f"s = {answer} i = {i} len = {len(answer)}")
    if answer[i]+answer[i+1] == "..":
        answer = answer.replace('..','.')
    else:
        i+=1
        
print(answer)