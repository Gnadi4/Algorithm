import sys

input = sys.stdin.readline

def main(s):
    while True:
        st = []
        tmp = ''
        # true : 열림
        rcnt_st = False
        for i in s:
            if i == '<' and rcnt_st == False:
                rcnt_st = True
                tmp += i
            elif rcnt_st:
                tmp += i
                if i == '>':
                    st.append(tmp)
                    tmp = ''
                    rcnt_st = False
                elif i == '<':
                    return 'illegal'
        ans = []
        while st:
            s_tmp = st.pop(0)
            if s_tmp[-2] != '/':
                if s_tmp[1] == '/':
                    if len(ans) == 0:
                        return 'illegal'
                    # 닫는 태그가 속성 값을 지니고 있는 경우
                    for i in s_tmp:
                        if i == ' ':
                            return 'illegal'
                    if ans[-1][1:len(s_tmp)-2] == s_tmp[2:-1]:
                        ans.pop()
                    else:
                        return 'illegal'
                else:
                    ans.append(s_tmp)
        if len(ans) == 0:
            return 'legal'
        else:
            return 'illegal'

if __name__ == "__main__":
    while True:
        s = input().rstrip()
        if s == '#':
            break
        print(main(s))