var todoList = new Vue({
  el: '#wrapper',
  data: {
    todos: [
      { text: '1111',
        done : false
      },
      { text: '2222',
        done : false
      },
      { text: '3333',
        done : false
      }
    ]
  },
  methods: {
    addTodos: function () {
      var newTodo = document.querySelector('#addTodoInput');
      this.todos.push({text: newTodo.value});
      newTodo.value = "";
    },
    removeTodos: function(ele){
      // this.todos.slice({text: newTodo.value});
      console.log(ele.currentTarget.parentNode.innerText)
    },
    done: function(){
      console.log(this.done)
    }
  }
});