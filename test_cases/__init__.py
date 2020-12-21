#_*_encoding=utf-8_*_
#作者     :bozhong
#创建时间 :2020/4/814:22
#文件     :
#IDE      :PyCharm



class Solution:
    def reverse(self, x: int) -> int:
        if x <0:
            num=abs(x)
            res_str=str(num)[::-1]
            res_int=int('-'+res_str)
        else:
            res_str = str(x)[::-1]
            res_int = int(res_str)

        if (-pow(2,31) < res_int < pow(2,31)-1):
            return res_int
        return 0
if __name__ == '__main__':
    num = -1234500
    print(Solution().reverse(num))



print(2**31)