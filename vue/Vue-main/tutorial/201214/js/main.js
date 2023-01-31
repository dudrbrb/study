var app1 = new Vue({
  el: '#app1',
  data: {
    message: 'console창에 app1.message 를 새로 입력해주면 바뀝니당'
  }
});

var app2 = new Vue({
  el: '#app2',
  data: {
    message: '이 페이지는 ' + new Date() + ' 에 로드 되었습니다'
  }
});

var app3 = new Vue({
  el: '#app3',
  data: {
    seen: false
  }
});

var app4 = new Vue({
  el: '#app4',
  data: {
    todos: [
      { text: '새우깡' },
      { text: '감자깡' },
      { text: '고구마깡' }
    ]
  },
  methods: {
    addTodos: function () {
      var app4Input = document.querySelector('#app4Input');
      this.todos.push({text: app4Input.value});
      app4Input.value = "";
    }
  }
});

var app5 = new Vue({
  el: '#app5',
  data: {
    message: '오늘의 점심은 볶음 진짬뽕',
  },
  methods: {
    splitMessage: function () {
      this.message = this.message.split('')
    },
    reverseMessage: function () {
      this.message = this.message.reverse()
    },
    joinMessage: function () { 
      this.message = this.message.join('')
    },
    onceChange : function(){ // 최종
      this.message = this.message.split('').reverse().join('')

    }
  }
});

var app6 = new Vue({
  el: '#app6',
  data: {
    message: 'input에 입력해주세요'
  }
})

Vue.component('todo-item', {
  // 이제 todo-item 컴포넌트는 "prop" 이라고 하는
  // 사용자 정의 속성 같은 것을 입력받을 수 있습니다.
  // 이 prop은 todo라는 이름으로 정의했습니다.
  props: ['todo'],
  template: '<li>{{ todo.text }}</li>'
})
  
  var app7 = new Vue({
    el: '#app7',
    data: {
      groceryList: [
        { id: 0, text: '아롱이' },
        { id: 1, text: '누리' },
        { id: 2, text: '인자' }
      ]
    }
  })
  