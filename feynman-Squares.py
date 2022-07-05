# def count_squares(n):
#     sq=0
#     for i in range(1,n+1):
#         sq+=i*i
#     return sq
def count_squares(n):
    return int((n*(n+1)*((n<<1)+1)/6))