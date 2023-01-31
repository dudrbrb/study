var router = require('express').Router(); 
// express라는 라이브러리 중 Router()함수 router변수에 담겠다.


function 로그인했니(요청, 응답, next) {
    if (요청.user){next()}
    else {응답.send('로그인이 되어있지 않습니다.')}
}


// 전역 미들웨어 (각 라우트에 안적어도 이 파일 내의 라우트에 전체 적용)
router.use(로그인했니);
// 지정 주소에만 미들웨어 적용
// router.use('/shirts', 로그인했니);


// app 대신 위에서 선언한 router 사용
router.get('/shirts', function(요청, 응답){
   응답.send('셔츠 파는 페이지입니다.');
});

router.get('/pants', function(요청, 응답){
   응답.send('바지 파는 페이지입니다.');
}); 

module.exports = router;
// 이 js 파일 안 변수(최상단에서 설정한 변수 router)를 다른 파일에서 불러서 쓰고싶을 때 사용
// 배출문법 : module.exports = 변수명;
// 첨부 문법 : require('/shop.js')