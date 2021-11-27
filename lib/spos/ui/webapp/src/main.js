import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import { makeServer } from "./mock/server"
import axios from 'axios'
import VueAxios from 'vue-axios'
import VueI18n from 'vue-i18n';
import {messages} from './trans/translation'

Vue.use(VueI18n);


const i18n = new VueI18n({
  locale: 'de',
  messages
});

Vue.use(VueAxios, axios)

Vue.config.productionTip = false

if (process.env.NODE_ENV === "xdevelopment") {
  console.log("test")
  makeServer()
}

//import Vuex from 'vuex'

import store from './store'

Vue.config.productionTip = false

new Vue({
  vuetify,
  store,
  i18n,
  render: h => h(App)
}).$mount('#app')
