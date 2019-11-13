question_url = 'https://www.wjx.cn/jq/48787292.aspx'

question_coockie = 'UM_distinctid=16e1aff3de1fd-0bece1616bde0c-b363e65-144000-16e1aff3de35e3; CNZZDATA4478442=cnzz_eid%3D1310099333-1572406869-https%253A%252F%252Fsp0.baidu.com%252F%26ntime%3D1573269174; .ASPXANONYMOUS=dtqxPW_F1QEkAAAAZmE5N2UwNWUtNGJlNi00OGY2LTgxNjYtY2ZkMjgwMjNlZjgx8mTsfvQkCcGBp6uvemtwoBzmi341; acw_tc=2f624a7315724109645253418e79e4c3b50feb8bfd8360cd64384a3720f9ae; jac48787292=12795638; Hm_lvt_21be24c80829bd7a683b2c536fcf520b=1572410966,1572516457,1572516568,1573184302; Hm_lpvt_21be24c80829bd7a683b2c536fcf520b=1573269428'

submit_url = 'https://www.wjx.cn/joinnew/processjq.ashx?submittype=1&curID=48787292&t=1573269466263&starttime=2019%2F11%2F9%2011%3A17%3A07&ktimes=327&rn=3752430363.12795638&hlv=1&jqnonce=aab16aac-b7f2-434f-b6da-7c51e1e6b753&jqsign=ffe61ffd*e0a5*343a*e1cf*0d26b6b1e024&jpm=13'

submit_times = 100

designated_area = ['广东','湖南']

designated_ratio = [
    [1,1,2,3,3,4,4,5],
    [1,1,2,1],
    [1111,3,888,5,999,4]
]

def createStr():
    count1 = 0
    iStr = 'submitdata= '
    while count1 < len(designated_ratio):
        halfLen = int(len(designated_ratio[count1])/2)
        sumRatio = 0
        count2 = halfLen
        while (count2 >= halfLen) & (count2 < 2*halfLen):
            sumRatio += designated_ratio[count1][count2]
            count2 += 1
        num = random.randint(1,sumRatio)
        count2 = 0
        ratio = 0
        while count2 < halfLen:
            ratio += designated_ratio[count1][count2 + halfLen]
            if num <= ratio:
                iStr = iStr + '}' + str(count1 + 2) + '$' + str(designated_ratio[count1][count2])
                break
            count2 += 1
        count1 += 1
    return  iStr