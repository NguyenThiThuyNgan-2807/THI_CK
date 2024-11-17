# Bạn được cung cấp một số nguyên dương n . Viết một hàm để xác định xem n có phải là
# số nguyên tố hay không.
# Số nguyên tố là số nguyên dương lớn hơn 1 và chỉ có hai ước số dương là 1 và chính nó.
def question_1(n: int) -> bool:
    if n < 2:
        return False
    for i in [2,int(n**0.5)+1]:
        if n % i ==0:
            return False
    return True
print(question_1(37))

# Viết một hàm tạo ra n số nguyên ngẫu nhiên từ 1 đến 100. Sau đó, tính tổng và 
# trung bình của các số này.
def question_2(n: int):
    import random
    if n == 0:
       return False 
    ran_num= [random.randint(1,100) for _ in range (n)]
    return sum(ran_num),sum(ran_num)/len(ran_num)
print(question_2(9))
            
# Viết một hàm nhận vào một chuỗi, sau đó đếm và in ra số lượng ký tự viết hoa và
# ký tự viết thường trong chuỗi đó.
def question_3(s: str) :
    upper_count = sum(1 for i in s if i.isupper())
    lower_count = sum(1 for i in s if i.islower())
    return upper_count,lower_count
print(question_3("toi TEN LA Chloe"))

# Viết một hàm để kiểm tra xem một số nguyên được nhập vào có phải là số chẵn hay không.
# Trả về True nếu số đó là số chẵn, và False nếu là số lẻ.
def question_4(n: int) -> bool:
    if n% 2==0:
        return True
    return False
print(question_4(2))

# Viết một hàm để tìm phần tử x trong một danh sách lst . Nếu tìm thấy, 
# trả về vị trí (chỉ số)
# của phần tử đó, nếu không, trả về None .

def question_5(lst_a:list, n):
    try:
        return lst_a.index(n)
    except:
        return None
print(question_5([1,2,3,4,5], 5))

# Viết một hàm để tính giai thừa của số nguyên dương n . Giai thừa của n 
# (ký hiệu là n! ) là tích của tất cả các số từ 1 đến n .
def question_6(n: int):
    x=1
    for i in range (1,n+1):
        x*=i
    return x
print(question_6(7))

# Viết một hàm tạo ra n số thực ngẫu nhiên trong khoảng từ 0 đến 1. Sau đó, 
# tìm số lớn nhất và số nhỏ nhất trong danh sách đó.
def question_7(n: float):
    import random
    ran_num1= [random.random() for _ in range (n)]
    return ran_num1,max(ran_num1), min(ran_num1)
print(question_7(4))

# Viết một hàm để đảo ngược một chuỗi được nhập vào từ bàn phím.   
def question_8(s:str):
    return s[::-1]
print((question_8("hello")))

# Viết một hàm để kiểm tra xem một chuỗi có phải là chuỗi palindrome hay không. Một chuỗi
# được gọi là palindrome nếu, sau khi chuyển tất cả các chữ cái viết hoa thành chữ thường
# và loại bỏ tất cả các ký tự không phải chữ cái và số, nó đọc giống nhau từ trái sang phải và
# từ phải sang trái.

def question_9(s: str) -> bool:
    s=s.lower()
    s_after=''.join( i for i in s if i.isalnum())
    return s_after==s_after[::-1]
print(question_9("A man, a plan, a canal: Panama"))

# Viết một hàm nhập vào một danh sách số nguyên từ bàn phím các số nguyên này được
# phân cách bằng khoảng trắng và trả về None nếu danh sách đó trống.

def question_10():
    s=input("nhập ds: ").strip()
    if not s:
        return None
    ds_s= [int(i) for i in s.split()]
    return ds_s
print(question_10())
    
# Viết một hàm question_11(n) để trả về số Fibonacci thứ n . Dãy số Fibonacci được định
# nghĩa như sau:

# F(0) = 0
# F(1) = 1
# F(n) = F(n-1) + F(n-2) với n > 1

def question_11(n:int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return question_11(n - 1) + question_11(n - 2)
print(question_11(10))
        
# Viết một hàm để tạo ra một số nguyên ngẫu nhiên từ 1 đến 1000. Sau đó, kiểm tra xem số
# đó có phải là số nguyên tố hay không.
# Số nguyên tố là số nguyên dương lớn hơn 1 và chỉ có hai ước số dương là 1 và chính nó.
def question_12() -> bool:
    import random
    s=random.randint(1, 1000)
    for i in [2,int(s**0.5)+1]:
        if s%i==0:
            return False,s
    return True,s
print(question_12())

# Viết một hàm để đếm số từ trong một chuỗi. Một từ được định nghĩa là một chuỗi các ký tự
# không phải khoảng trắng.
def question_13(s: str) -> int:
    sau=s.split()
    return len(sau)
print(question_13("Hello world, how are you?"))

# Viết một hàm để kiểm tra xem một chuỗi có phải là chữ số hay không. Chuỗi được coi là
# chữ số nếu tất cả các ký tự trong chuỗi là số và không có ký tự nào khác.

def question_14(s: str) -> bool:
    return s.isdigit()
print(question_14("132c68"))

# Viết một hàm để kiểm tra xem một biến có giá trị None hay không.

def question_15(value) -> bool:
    if value==None:
        return True
    return False
print(question_15(None))

# Viết một hàm để tính trung bình cộng, nhận vào số lượng tham số bất kỳ và trả về giá trị
# trung bình cộng của chúng.
def question_16(*args) -> float:
    if not args:
        return None
    return sum(args)/len(args)
print(question_16())

# Viết một hàm để tạo ra một danh sách gồm n số nguyên ngẫu nhiên từ 1 đến 100. Sau đó,
# sắp xếp danh sách theo thứ tự giảm dần.
def question_17(n: int):
    import random
    x=[random.randint(1,100) for _ in range (n)]
    x.sort(reverse=True)
    return x
print(question_17(4))

# Viết một hàm để loại bỏ tất cả khoảng trắng thừa trong một chuỗi, bao gồm:

# Loại bỏ khoảng trắng ở đầu và cuối chuỗi.
# Loại bỏ các khoảng trắng dư thừa giữa các từ (chỉ giữ lại một khoảng trắng giữa các
# từ).

def question_18(s: str) :
    s1= s.strip().split()
    x=' '.join(s1)
    return x
print(question_18(" Hello             world!                   "))

# Viết một hàm để kiểm tra xem một số nguyên nhập vào có lớn hơn một số nguyên cho
# trước n hay không.
def question_19(x: int, n: int) -> bool:
    return x>n
print(question_19(6, 2))

# Viết một hàm yêu cầu người dùng nhập một giá trị từ bàn phím. Nếu người dùng không
# nhập bất kỳ giá trị nào từ bàn phím (chỉ nhấn Enter), hàm sẽ trả về None .    
def question_20() :
    x =input("nhập data: " )
    if not x:
        return None
    return x
print(question_20())

# Viết một hàm nhận vào một danh sách số nguyên ngẫu nhiên và một số nguyên dương.
# Hàm sẽ tìm trong danh sách hai số có tổng bằng với số nguyên dương kia và trả về cặp số
# đó.
def question_21(nums: list[int], target: int):
    so=0 
    for i in nums:
        so=target-i
        if so in nums:
            return so,i
    return None
print(question_21([1,23,3,5,6], 19))

# Viết một hàm nhận vào một mảng các số nguyên nums . Di chuyển tất cả các số 0 trong
# mảng về cuối mảng trong khi vẫn giữ nguyên thứ tự của các phần tử không phải số 0.    
def question_22(nums: list[int]) ->None :
    vi_tri=0 
    for i in nums:
        if i != 0:
            nums[vi_tri]=i
            vi_tri+=1 
    for z in range (vi_tri,len(nums)):
        nums[z]=0
    return nums
print(question_22([1,3,0,3,0,3,9,0]))

# Viết một hàm nhận vào một mảng các số nguyên nums . Trả về True nếu có bất kỳ giá trị
# nào xuất hiện ít nhất hai lần trong mảng, và trả về False nếu tất cả các phần tử trong mảng
# đều khác nhau.
def question_23(nums: list[int]) -> bool:
    for i in range (len(nums)):
        for z in nums[i+1:]:
            if nums[i]==z:
                return True
    return False
print(question_23([1,2,3,4,5]))

# Viết một hàm nhận vào một mảng số nguyên nums có kích thước n . Trả về phần tử chiếm
# đa số trong mảng. Phần tử chiếm đa số là phần tử xuất hiện nhiều hơn [n / 2] lần. Bạn có
# thể giả định rằng phần tử chiếm đa số luôn tồn tại trong mảng.
def question_24(nums: list[int]) -> int:
    candidate = None
    count = 0
    for num in nums:
       if count == 0:
           candidate = num
       count += 1 if num == candidate else -1
    return candidate
print(question_24([2,2,2,1,1,1,2]))

# Cho một mảng các số nguyên nums đã được sắp xếp theo thứ tự không giảm. Viết một hàm
# để trả về một mảng chứa bình phương của mỗi số trong nums và mảng này cũng phải được
# sắp xếp theo thứ tự không giảm.
def question_25(nums: list[int]) -> list[int]:
     binh_phương=[i**2 for i in nums]  
     binh_phương.sort()
     return binh_phương
print(question_25([-1,0,2,3]))

# Cho một chuỗi s chỉ gồm các chữ cái viết thường và viết hoa. Viết một hàm để trả về độ dài
# của chuỗi palindrome dài nhất có thể được tạo ra từ các chữ cái đó. Các chữ cái có phân
# biệt chữ hoa và chữ thường (ví dụ: "Aa" không được coi là một palindrome). Palindrome là
# chuỗi đọc giống nhau từ trái sang phải và ngược lại.
def question_26(s: str):
    ds_dem={}
    for char in s:
        ds_dem[char]=ds_dem.get(char,0)+1 
    length=0 
    for val in ds_dem.values():
        length+=val//2*2 
    if length<len(s):
        length=length+1 
    return length
print(question_26('abcccccđd'))

# Viết một hàm để tìm chuỗi tiền tố chung dài nhất trong một mảng các chuỗi. Nếu không có
# tiền tố chung, trả về một chuỗi rỗng "" .
def question_27(strs: list[str]) -> str:
    if not strs:
        return ""
    tien_to_c=strs[0]
    for i in strs[1:]:
        while not i.startswith(tien_to_c):
            tien_to_c=tien_to_c[:-1]
            if not tien_to_c:
                    return ""
    return tien_to_c
print(question_27(["flower", "flow", "flight"]))

# Viết một hàm để đếm số lần xuất hiện của từng phần tử (ký tự) trong một chuỗi. Trả về kết
# quả dưới dạng một từ điển, trong đó các khóa là các ký tự và giá trị là số lần xuất hiện của
# ký tự đó.
def question_28(s: str) :
    tu_dien={}
    for char in s:
        tu_dien[char]=tu_dien.get(char,0)+1 
    return tu_dien
print(question_28("hello"))

# Số trung vị của một danh sách các số nguyên là giá trị ở vị trí giữa khi danh sách được sắp
# xếp theo thứ tự tăng dần. Nếu danh sách có số lượng phần tử là lẻ, số trung vị là giá trị
# giữa. Nếu danh sách có số lượng phần tử là chẵn, số trung vị là trung bình cộng của hai giá
# trị ở giữa
def question_29(nums: list[int]) -> float:
    nums.sort()
    n=len(nums)
    mid=n//2
    if n%2==1:
        return nums[mid]
    else:
        return (nums[mid]+nums[mid-1])/2
print(question_29([1,3,4,2]))

# Cho một đoạn văn là một chuỗi ký tự, viết chương trình đếm số lượng mỗi từ xuất hiện
# trong đoạn văn đó.
def question_30(paragraph: str):
    para = {}
    tach= paragraph.split()
    for tu in tach:
        para[tu]=para.get(tu,0)+1 
    return para
print(question_30("apple orange apple banana orange"))

# Cho một đoạn văn là một chuỗi ký tự, viết chương trình tìm ra các từ có tỷ lệ xuất hiện lớn
# hơn 20% trong đoạn văn.    
def question_31(paragraph: str, n: int):
    tach=paragraph.split()
    total=len(tach)
    tu_20=[]
    for tu in set(tach):
        if tach.count(tu)*100/total>20:
            tu_20.append(tu)
    return tu_20[:n]
print(question_31("apple orange apple banana orange",2))

# Cho một danh sách các số nguyên nums , phân chia danh sách thành hai danh sách:

# 1. Danh sách các số chẵn, được sắp xếp theo thứ tự giảm dần (từ lớn đến nhỏ).
# 2. Danh sách các số lẻ, được sắp xếp theo thứ tự tăng dần (từ nhỏ đến lớn).
    
def question_32(nums: list[int]) -> tuple[list[int], list[int]]:
    so_chan=[]
    so_le=[]
    for i in nums:
        if i%2==1:
            so_le.append(i)
            so_le.sort()
        else:
            so_chan.append(i)
            so_chan.sort(reverse=True)
    return so_chan,so_le
print(question_32([4, 1, 3, 2, 7, 8, 5]))

# Cho một danh sách nums chứa các số nguyên. Viết một hàm để tìm phần tử lớn thứ 2 và
# phần tử nhỏ thứ 5 trong danh sách.
def question_33(nums: list[int]) -> tuple[int, int]:
    nums.sort()
    return nums[4],nums[-2]
print(question_33([3, 1, 4, 5, 9, 2, 6, 8, 7]))

# Viết một hàm để tìm chuỗi con dài nhất trong chuỗi đầu vào mà không chứa bất kỳ ký tự
# nào bị lặp lại.
def question_34(s: str) -> str:
    max_str=""
    current=""
    for i in s:
        if i in current:
            current=current.split(i,1)[1]
        current+=i
        max_str=max(max_str, current, key=len)
    return len(max_str)   
print(question_34("bbbb"))

# Cho một chuỗi đầu vào, tìm chuỗi con lặp lại dài nhất trong chuỗi. Chuỗi con lặp lại là một
# chuỗi xuất hiện ít nhất hai lần và không được chồng chéo nhau.v
def question_35(s: str) -> str:
    longest=""
    n=len(s)
    for i in range(n):
        for z in range(i+1,n+1):
            chuoi_phu=s[i:z]
            if s.count(chuoi_phu)>1:
                if len(chuoi_phu)>len(longest):
                    longest=chuoi_phu
    return longest
print(question_35("aabcdeaabcd"))
    
# Cho một mảng nums gồm các số nguyên khác nhau. Viết một hàm để trả về tất cả các hoán
# vị có thể của mảng đó. Bạn có thể trả về kết quả theo bất kỳ thứ tự nào.
def question_36(nums: list[int]) -> list[list[int]]:
    if len (nums)==0:
        return [[]]
    result=[]
    for i in range(len(nums)):
        current=nums[i]
        other=nums[:i]+nums[i+1:]
        for p in question_36(other):
            result.append([current]+p)
    return result
print(question_36([1,2,3]))

# Cho một chuỗi s chỉ chứa các ký tự '(', ')', '{', '}', '[' và ']'. Viết một hàm để xác định xem
# chuỗi đầu vào có hợp lệ hay không.
def question_37(s: str) -> bool:
    chuoi= []
    tuong_ung={'(':')','[':']','{':'}'}
    for char in s:
        if char in tuong_ung:
            chuoi.append(tuong_ung[char])
        elif not chuoi or chuoi.pop() != char:
            return False
    return not chuoi
print(question_37("()[]{}"))

# Giả sử bạn đang đứng trước cầu thang có n bậc thang. Mỗi lần bạn có thể bước lên 1 bậc
# hoặc 2 bậc. Viết một hàm để tính số cách bạn có thể leo hết bậc thang.
def question_38(n: int) -> int:
   if n<=2:
       return n
   return question_38(n-1)+question_38(n-2)
print(question_38(5))   

# Cho một dãy số nằm trong danh sách, đại diện cho giá của một mặt hàng thay đổi qua từng
# ngày. Viết một hàm để tìm ra lợi nhuận lớn nhất có thể đạt được bằng cách thực hiện một
# lần mua và một lần bán, với điều kiện là phải mua mới được bán.
def question_39(prices: list[int]) -> int:
    if not prices:
        return 0
    lnln=prices[0]
    lnln_c=0
    for i in prices:
       lnln=min(lnln,i)
       profit=i-lnln
       lnln_c=max(lnln_c,profit)
    return lnln_c
print(question_39([6, 7, 8, 9, 20, 5]))

       





































