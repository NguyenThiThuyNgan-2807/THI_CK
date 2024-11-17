#1
def question_1(n: int) -> bool:
    if n<2:
        return False
    for i in range (2,n):
        if n%i == 0:
            return False
    return True
print(question_1(4))


#2
import random
def question_2(n: int) -> (int, float):
    n_1 = [random.randint(1,100) for _ in range (n)]
    x = sum(n_1)
    y = sum(n_1)/len(n_1)
    return x,y
print(question_2(2))


#3
def question_3(s: str) -> (int, int):
    return len([i for i in s if i.isupper()]), len([i for i in s if i.islower()])
print(question_3("Hello World"))


#4
def question_4(n: int) -> bool:
    if n%2 == 0:
        return True
    else:
        return False
print(question_4(10))


#5
def question_5(lst: list, x: int) -> int or None:
    if x in lst:
        return lst.index(x)
    return None
print(question_5([10,20,30,40],25))


#6
def question_6(n: int) -> int:
    x=1
    for i in range(1,n+1):
        x *= i
    return x
print(question_6(5))


#7
def question_7(n: int) -> (float, float):
    a = [random.uniform(0,1) for _ in range(n)]
    return min(a), max(a)
print(question_7(5))


#8
def question_8() -> str:
    s = "Hello World"
    return s[::-1]
print(question_8())

#9
def question_9(s: str) -> bool:
    s=' '.join(i.lower() for i in s if i.isalnum())
    s1 = s[::-1]
    return s == s1
print(question_9("A man, a plan, a canal: Panama"))


#10
def question_10() -> None:
    ds = input("Nhap ds: ")
    if not ds:
        return None
    else:
        return ds
print(question_10())


#11
def question_11(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return question_11(n-1) + question_11(n-2)
print(question_11(10))


#12
import random
def question_12() -> bool:
    n = random.randint(1,1000)
    if n<2:
        return n,False
    for i in range (2,n):
        if n%i == 0:
            return n,False
    return n,True
print(question_12())

#13
def question_13(s: str) -> int:
    return len(s.split())
print(question_13("Hello world"))

#14
def question_14(s: str) -> bool:
    return s.isdigit()
print(question_14("123a45"))
    
#15
def question_15(value) -> bool:
    if value == None:
        return True
    return False
print(question_15(None))

#16
def question_16(arg) -> float:
    if not arg:
        return None
    return sum(arg)/len(arg)
print(question_16([1,2,3,4,5]))

#17
def question_17(n: int) -> list:
    ds = [random.randint(1,100) for _ in range(n)]
    ds.sort(reverse = True)
    return ds
print(question_17(5))

#18
def question_18(s: str) -> str:
    s1 = s.strip().split()
    s2 = ' '.join(s1)
    return s2
print(question_18("     Hello     world!     "))

#19
def question_19(x: int, n: int) -> bool:
    return x>n
print(question_19(x = 15, n = 10))

#20
from typing import Optional
def question_20() -> Optional[str]:
    n = input("Mời nhập: ")
    if not n:
        return None
    return n
print(question_20())

#21
def question_21(nums: list[int], target: int) -> Optional[tuple[int, int]]:
    s = set() 
    for i in nums:
        s = target - i
        if s in nums:
            return s, i
    return None
print(question_21([2,7,11,15],9))

#22
def question_22(nums: list[int]) -> None:
    s=0 
    for i in nums:
        if i != 0:
            nums[s]=i
            s+=1 
    for z in range (s,len(nums)):
        nums[z]=0
    return nums
print(question_22([0, 1, 0, 3, 12]))

#23
def question_23(nums: list[int]) -> bool:
    for i in range (len(nums)):
        for z in nums[i+1:]:
            if nums[i] == z:
                return True
    return False
print(question_23([1,2,3,1]))
print(question_23([1,2,3,4]))

#24
def question_24(nums: list[int]) -> int:
    s = None
    count = 0 
    for i in nums:
        if count == 0:
            s = i
        count += 1 if i == s else -1 
    return s
print(question_24([3,2,3]))

#25
def question_25(nums: list[int]) -> list[int]:
    binh_phuong = [i**2 for i in nums]
    binh_phuong.sort()
    return binh_phuong
print(question_25([-4, -1, 0, 3, 10]))

#26
def question_26(s: str):
    ds = {}
    for i in s:
        ds[i] = ds.get(i,0) + 1 
    a = 0 
    for z in ds.values():
        a += z//2*2 
    if a < len(s):
        a += 1 
    return a
print(question_26('abccccdd'))

#27
#s = tien_to_chung = tiền tố chung
def question_27(strs: list[str]) -> str:
    if not strs:
        return ""
    s = strs[0]
    for string in strs[1:]:
        while not string.startswith(s):
            s = s[:-1]
            if not s:
                return ""
    return s
print(question_27(["flower", "flow", "flight"]))

#28
from typing import Dict
def question_28(s: str) -> Dict[str, int]:
    ds = {}
    for i in s:
        ds[i] = ds.get(i,0) + 1 
    return ds
print(question_28("hello"))

#29
def question_29(nums: list[int]) -> float:
    nums.sort()
    n=len(nums)
    mid=n//2
    if n%2==1:
        return nums[mid]
    else:
        return (nums[mid]+nums[mid-1])/2
print(question_29([1,3,4,2,5]))

#30
def question_30(paragraph: str):
    para = {}
    tach = paragraph.split()
    for tu in tach:
        para[tu] = para.get(tu,0) + 1 
    return para
print(question_30("apple orange apple banana orange"))
   
#31
def question_31(paragraph: str, n: int):
    tach = paragraph.split()
    tu_20=[]
    for tu in set(tach):
        if tach.count(tu)*100/len(tach) > 20:
            tu_20.append(tu)
    return tu_20[:n]
print(question_31("apple orange apple banana orange",2))

#32
from typing import Optional, List, Dict, Tuple
def question_32(nums: List[int]) -> Tuple[List[int], List[int]]:
    chan = []
    le = []
    for i in nums:
        if i%2 == 1:
            le.append(i)
            le.sort()
        else:
            chan.append(i)
            chan.sort(reverse=True)
    return chan, le
print(question_32([4, 1, 3, 2, 7, 8, 5]))

#33
def question_33(nums: list[int]) -> tuple[int, int]:
    nums.sort()
    return nums[-2],nums[4]
print(question_33([3, 1, 4, 5, 9, 2, 6, 8, 7]))

#34
def question_34(s: str) -> int:
    max_str = ""
    current = ""
    for i in s:
        if i in current:
            current = current.slipt(i,1)[1]
        current += i
        max_str = max(max_str, current, key=len)
    return max_str
print(question_34("abcabcbb"))

#38
def question_38(n: int) -> int:
    if n<=2:
        return n
    return question_38(n-1) + question_38(n-2)
print(question_38(2))



  

                   






































    