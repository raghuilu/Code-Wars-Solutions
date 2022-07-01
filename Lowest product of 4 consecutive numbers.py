def f_p(a):
    p=1
    for i in range(len(a)):
        p*=ord(a[i])
    return p
def lowest_product(input):
    if(len(input)>=4):
        c_pro=f_p(input[:4])
        m_pro=c_pro
        for i in range(4,len(input)):
            c_pro=(c_pro*(ord(input[i])-ord('0'))//((ord(input[i-4]))-ord('0')))
            m_pro=min(m_pro,c_pro)
        return c_pro
    return "Number is too small"