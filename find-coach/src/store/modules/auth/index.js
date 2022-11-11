// import mutations from './mutations.js'
// import getters from './getters.js'
// import actions from './actions.js'
import axios from 'axios';

export default {
    state:{
        user: null,
        posts: null
    },
    getters:{
        isAuthenticated: (state) => !!state.user,
        StatePosts: (state) => state.posts,
        StateUser: (state) => state.user
    },
    
    actions:{
        async Register({dispatch}, form){
            await axios.post('auth/users/', form)
            let userForm = new FormData();
            userForm.append('email', form.email)
            userForm.append('password', form.password)

            await dispatch('LogIn', userForm)
        },

        async LogIn({commit}, user){
            await axios.post('api/token/', user);
            await commit('setUser', user.get('email'))
        },
        async CreatePost({dispatch}, post){
            await axios.post('post', post)
            await dispatch('GetPosts')
        },
        async GetPosts({commit}){
            let response = await axios.get('auth/posts')
            commit('setPosts', response.data)
        }
           ,
        async LogOut({commit}){
            let user = null
            commit('logout', user)
        }
    },
    mutations:{
        setUser(state, email){
            state.user = email
        },
        setPosts(state, posts){
            state.posts = posts
        },
        logout(state){
            state.user = null;
            state.posts = null;
        }

    },
    
}