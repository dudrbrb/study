'use strict'

/** @type {typeof import('@adonisjs/lucid/src/Lucid/Model')} */
const Model = use('Model')
class Test extends Model {
  static get table(){
    return 'blog_css'
  }

}

module.exports = Test
