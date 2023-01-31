'use strict'

const Test = use('App/Models/Test')
const Database = use('Database')

class TestController extends Test {


  index ({ request, response }) {
    return "aa";
  }


}

module.exports = TestController
