import Vue from 'vue'
import Vuex from 'vuex'
import authModule from './modules/auth/index.js'
import createPersistedState from "vuex-persistedstate";


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    auth: authModule
  },
  plugins: [createPersistedState()]
})
