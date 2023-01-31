const MongoClient = require('mongodb').MongoClient; // mongoDB호출
const express = require('express'); // 서버 통신을 위한 라이브러리 호출
const bodyParser= require('body-parser') // 데이터 처리를 위한 라이브러리
const app = express(); // 객체에 저장
const methodOverride = require('method-override')
require('dotenv').config()

app.use(bodyParser.urlencoded({extended: true})); // 바디파서 사용
app.use('/public', express.static('public')); // css와 같은 static(data변화에 따라 변하지 않는 파일)파일을 public에서 불러와 사용하겠다는 의미
app.set('view engine', 'ejs'); // ejs파일 사용
app.use(methodOverride('_method')); // put과 delete 사용

app.use('/shop', require('./routes/shop.js'));

var db;
MongoClient.connect(process.env.DB_URL, function(에러, client){
    // DB연결 성공하면 할 일
    if(에러) return console.log(에러)

	// todoapp이라는 database에 연결
    db = client.db('todoapp');

    app.listen(process.env.PORT, function(){
        console.log('listening on 8080')
    });
});



app.get('/', function(요청, 응답){
    응답.render('index.ejs')
});
app.get('/write', function(요청, 응답){
    응답.render('write.ejs')
});

app.get('/list', function(요청, 응답){
    db.collection('post').find().toArray(function(에러, 결과){
        응답.render('list.ejs', {posts: 결과}) 
				// ^ 이 위치 중요!
    });
});

app.get('/detail/:id', function(요청, 응답){
	db.collection('post').findOne({ _id : parseInt(요청.params.id) }, function(에러, 결과){
	  응답.render('detail.ejs', {data : 결과} )
	})
});

app.get('/edit/:id', function(요청, 응답){
    db.collection('post').findOne({ _id : parseInt(요청.params.id) }, function(에러, 결과){
        if(에러) return console.log(에러)
        응답.render('edit.ejs', {post : 결과} );
    })
});


app.put('/edit', function(요청, 응답){
    db.collection('post').updateOne({_id: parseInt(요청.body.id)},{$set:{title: 요청.body.title, date: 요청.body.date}}, function(에러, 결과){
        응답.redirect('/list');
    })
});


// 회원 인증 기능
const passport = require('passport');
const LocalStrategy = require('passport-local').Strategy;
const session = require('express-session');

app.use(session({secret : '비밀코드', resave : true, saveUninitialized: false}));
app.use(passport.initialize());
app.use(passport.session());


app.get('/login', function(요청, 응답){
    응답.render('login.ejs')
});

app.post('/login', passport.authenticate('local', {
    failureRedirect : '/fail'
}), function(요청, 응답){
    응답.redirect('/')
});


passport.use(new LocalStrategy({ 
    usernameField: 'id',
    passwordField: 'pw',
    session: true, 
    passReqToCallback: false, 
}, function (입력한아이디, 입력한비번, done) {
        db.collection('login').findOne({ id: 입력한아이디 }, function (에러, 결과) { 
            // 사용자 아이디 , 비번 검증하는 부분
            if (에러) return done(에러)
        
            if (!결과) return done(null, false, { message: '존재하지않는 아이디입니다.' }) // 아이디 먼저 검사
            if (입력한비번 == 결과.pw) { // 아이디가 있을 시, 비밀번호 검사
                return done(null, 결과)
            } else { 
                return done(null, false, { message: '비번틀렸어요' })
            }
        });
    }
));

passport.serializeUser(function (user, done) {
    done(null, user.id)
		// id를 이용해 세션을 저장시키는 코드 (로그인 성공시 발동)
});
  
passport.deserializeUser(function (아이디, done) {
    // 이 세션 데이터를 가진 사람을 DB에서 찾아주세요 (마이페이지 접속시 발동)
    db.collection('login').findOne({id: 아이디}, function(에러, 결과){
        done(null, 결과)
    })
});


function 로그인했니(요청, 응답, next){
    if(요청.user){ 
        next()
    }else{
        응답.send('로그인이 되어있지 않습니다.')
    }
}

app.post('/add', function(요청, 응답){
    db.collection('counter').findOne({name: '게시물갯수'}, function(에러, 결과){
        var 총게시글갯수 = 결과.totalPost;
        var 저장할내용 = {_id: 총게시글갯수 + 1, title: 요청.body.title, date: 요청.body.date, writer_id: 요청.user._id, writer: 요청.user.id} ;

        db.collection('post').insertOne(저장할내용, function(에러, 결과){
            db.collection('counter').updateOne({name: '게시물갯수'}, {$inc: {totalPost: 1}}, function(에러, 결과){
                if(에러) return console.log(에러)
                응답.redirect('/list');
			})
        });
    });
});

app.delete('/delete', function(요청, 응답){
    var 삭제할데이터 = {_id: parseInt(요청.body._id), writer_id: 요청.user._id}
    
	db.collection('post').deleteOne(삭제할데이터, function(에러, 결과){
      	응답.status(200).send({message: '성공했습니다'});
  	});
});


app.get('/search', (요청, 응답) => {
    if(요청.query.value == null) return

    var 검색조건 = [
        {
          $search: {
            index: 'titleSearch',
            text: {
              query: 요청.query.value, // 실제 검색 부분
              path: ['title', 'date','_id'] // 제목날짜 둘다 찾고 싶으면 ['title', 'date']
            }
          }
        },
       { $sort : { _id : -1 } }, // 정렬, _id 순서로 정렬 (-1로 하면 반대순서로 정렬)
       { $limit : 10 }, // 제한걸기. 상위 10개만 가져와주세요
       { $project : { title : 1, date : 1, _id : 1 } } // 검색 결과를 뭘 보여줄지 선택 (1은 가져옴, 0이면 안가져옴)
    ];

    db.collection('post').aggregate(검색조건).toArray((에러, 결과)=>{
        응답.render('search.ejs', {posts: 결과, word: 요청.query.value})
    });
});


app.get('/mypage', 로그인했니, function(요청, 응답){
    응답.render('mypage.ejs', {사용자: 요청.user})
});



app.post('/register', (요청, 응답)=>{
    db.collection('login').insertOne({id: 요청.body.id, pw: 요청.body.pw}, (에러, 결과)=>{
        if(에러) return console.log(에러)
        응답.redirect('/');
    })
});




// 이미지 업로드
let multer = require('multer');//라이브러리 호출
var storage = multer.diskStorage({// 하드디스크에 저장하겠다는 뜻
// var storage = multer.memoryStorage({ // 램에 저장하겠다는 뜻 (휘발성이 있음)

    destination : function(req, file, cb){  // 이미지를 어디에 저장할지 경로 지정
        cb(null, './public/image')
    },
    filename : function(req, file, cb){  // 저장한 이미지의 파일명을 설정하는 부분
        cb(null, file.originalname )  // 원래 이름 그대로 저장하겠다는 뜻
    },
    filefilter : function(req, file, cb){
        var ext = path.extname(file.originalname);
        if(ext !== '.png' && ext !== '.jpg' && ext !== '.jpeg') {
            return callback(new Error('PNG, JPG만 업로드하세요'))
        }
        callback(null, true)
    }

});

var upload = multer({storage : storage});

app.get('/upload', function(요청, 응답){
    응답.render('upload');
});

app.post('/upload', upload.single('profile'), (요청, 응답)=>{
    응답.send('업로드 완료')
});

app.get('/image/:imageName', (요청, 응답)=>{
    응답.sendFile(__dirname + '/public/image/'+ 요청.params.imageName)
});



// 채팅 서비스

app.get('/chatroom/:id', (요청, 응답) => {
    
    응답.render('chatroom.ejs');
});
