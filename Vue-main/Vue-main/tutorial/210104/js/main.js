var vm1 = new Vue({
  el: '#example1',
  data: {
    items: [
      { message: 'apple' },
      { message: 'banana' },
      { message: 'orange' }
    ]
  }
})

var vm2 = new Vue({
  el: '#example2',
  data: {
    parentMessage: '과일',
    items: [
      { message: 'apple' },
      { message: 'banana' },
      { message: 'orange' }
    ]
  }
})

var vm3 = new Vue({
  el: '#example3',
  data: {
    object: {
      title: 'How to do lists in Vue',
      author: 'Jane Doe',
      publishedAt: '2016-04-10'
    }
  }
})