var vm1 = new Vue({
  el: '#example1',
  data: {
    message: '가나다라마바사'
  },
  computed: {
    // 계산된 getter
    reversedMessage: function () {
      // `this` 는 vm 인스턴스를 가리킴.
      return this.message.split('').reverse().join('')
    },
  },
  methods: {
    changeText: function(){
      var newMessage = document.querySelector('#messageInput');
      this.message  = newMessage.value;
      newMessage.value = "";
    }
  }
});

var vm2 = new Vue({
  el: '#example2',
  data: {
    firstName: 'Harry',
    lastName: 'Porter',
    fullName: 'Harry Porter'
  },
  watch: {
    // 각각의 값이 바뀌었을 때만 실행됨
    firstName: function (val) {
      this.fullName = val + ' ' + this.lastName;
      console.log('first name이 바뀌었다!')
    },
    lastName: function (val) {
      this.fullName = this.firstName + ' ' + val;
      console.log('last name이 바뀌었다!')
    }
  },
  methods : {
    changeName: function(){
      var newFirstName = document.querySelector('#firstName1');
      var newLastName = document.querySelector('#lastName1');

      this.firstName  = newFirstName.value;
      this.lastName  = newLastName.value;
    }
  }
});

var vm3 = new Vue({
  el: '#example3',
  data: {
    firstName: 'Harry',
    lastName: 'Porter'
  },
  computed: {
    fullName: function () {
      return this.firstName + ' ' + this.lastName
    }
  },
  methods: {
    changeName: function(){
      var newFirstName = document.querySelector('#firstName2');
      var newLastName = document.querySelector('#lastName2');

      this.firstName  = newFirstName.value;
      this.lastName  = newLastName.value;
    }
  }
});



var watchExampleVM = new Vue({
  el: '#example4',
  data: {
    question: '',
    answer: '질문을 입력하면 yes or no로 대답합니다'
  },
  watch: {
    // 인풋의 내용(질문)이 변경될 때 마다 실행.
    question: function (newQuestion) {
      this.answer = '입력을 기다리는 중...'
      this.debouncedGetAnswer()
    }
  },
  created: function () {
    // _.debounce는 시간이 많이 소요되는 작업을 실행할 수 있는 빈도를 제한합니다.
    // 우리는 yesno.wtf/api 에 액세스 하는 빈도를 제한하고,
    // 사용자가 ajax요청을 하기 전에 타이핑을 완전히 마칠 때까지 기다림.
    this.debouncedGetAnswer = _.debounce(this.getAnswer, 500)
  },
  methods: {
    getAnswer: function () {
      if (this.question.indexOf('?') === -1) {
        this.answer = '질문에는 물음표가 포함되어야 합니다!'
        return
      }
      this.answer = '생각중...'
      var vm = this
      axios.get('https://yesno.wtf/api')
        .then(function (response) {
          vm.answer = _.capitalize(response.data.answer);
        })
        .catch(function (error) {
          vm.answer = '에러! API 요청에 오류가 있습니다. ' + error
        })
    }
  }
})
