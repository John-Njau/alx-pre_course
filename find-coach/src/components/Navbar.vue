<template>
<main>
  <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/posts">Posts</router-link> |
    <span v-if="isLoggedIn">
      <a @click="logout">Logout</a>
    </span>
    <span v-else>
      <router-link to="/register">Register</router-link> |
      <router-link to="/login">Login</router-link>
    </span>
  </div>
</main>
</template>

<script>
export default {
  name: 'Navbar',
  computed:{
    isLoggedIn: function(){
      return this.$store.getters.isAuthenticated
    }
  },
  methods: {
    async logout(){
      await this.$store.dispatch('LogOut')
      this.$router.push('/login')
    }
  },
  
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
#nav {
  padding: 24px;

  a {
    font-weight: bold;
    color: #0d7eee;

    &.router-link-exact-active {
      color: #6b4d1f;
    }
  }
}

a:hover {
  cursor: pointer;
}

</style>
