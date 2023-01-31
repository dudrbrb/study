import theater_module as mv# theater_module 을 가져다가 사용
mv.price(3) # 3명이 영화 보러 갔을 때 가격
mv.price_morning(4) # 4명이 조조 영화 보러 갔을 때
mv.price_soldier(5) # 5명이 군인이 영화 보러 갔을 때




from theater_module import * # theater_module 내에서 모든 것을 가져다가 사용

price(3) # theater_module. 필요 없음
price_morning(4)
price_soldier(5)




from theater_module import price_soldier as price # price_soldier 를 새로운 별명인 price 로 사용
price(5) # price_soldier() 를 호출
