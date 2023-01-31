var vm1 = new Vue({
  el: '#example1',
  data: {
      show: false,
  }
});

var vm2 = new Vue({
  el: '#example2',
  data: {
      show: true,
  }
});

var vm3 = new Vue({
  el: '#example3',
  data: {
      type: 'D',
  }
});

var vm4 = new Vue({
  el: '#example4',
  data: {
    loginType: 'email',
    showText: false
  },
  methods: {
    changeType: function () {
      return this.loginType = this.loginType === 'username' ? 'email' : 'username'
    },
    openText: function(){
      return this.showText = this.showText === true ? false : true

    }
  }
});

var vm5 = new Vue({
  el: '#example5',
  data: {
    loginType: 'email',
  },
  methods: {
    changeType: function () {
      return this.loginType = this.loginType === 'username' ? 'email' : 'username'
    }
  }
});

var vm6 = new Vue({
  el: '#example6',
  data: {
    show: true,
  }
});