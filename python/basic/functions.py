def greeting(text):
    return print(text)

greeting('bye')




def fruit(fruit1, fruit2, fruit3, fruit4, fruit5):
    print('좋아하는 과일 리스트 :', end=" ")
    print(fruit1, fruit2, fruit3, fruit4, fruit5)


fruit('apple', 'banana', 'kiwi', 'blueberry', 'melon')


def fruit2(*fruits):
    print('좋아하는 과일 리스트 :', end=" ")
    for fruit in fruits:
        print(fruit, end=" ") # 언어들을 모두 한 줄에 표시


fruit2('apple', 'banana', 'kiwi', 'blueberry', 'melon')