# 만약에 유저가 입력한 글자가 2면 아이템
if number == 2:
    print("아이템을 쓴다.")
# 만약에 유저가 입력한 글자가 3이면 싸운다.
if number == 3:
    print("싸운다.")

print a = [10, 20, 30, 40, 50]
    print(list(a))
    
list = [0]
print(list)
list.append(1)
print(list)

dictVariable = {
        "name" : "철수",
        "age" : 20,
        "from": "korea"
    }   # 딕셔너리(Dictionary) 생성 및 초기화(Key, Value)

    print(dictVariable) # 딕셔너리 내용 확인
    print(dictVariable.keys())  # 딕셔너리 키 확인
    print(dictVariable["name"])
    print("name" in dictVariable)
    dictVariable["name"] = "영희"
    dictVariable["phone"] = "Galaxy"
    print(dictVariable)
    print(dictVariable["name"]) 
