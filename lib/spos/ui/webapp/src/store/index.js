import Vue from 'vue'
import Vuex from 'vuex'
import * as valuation from './valuation'
import * as school from './school'

Vue.use(Vuex)

export default new Vuex.Store({
  modules:{
    school: school.default,
    valuation: valuation.default,
  }
})
