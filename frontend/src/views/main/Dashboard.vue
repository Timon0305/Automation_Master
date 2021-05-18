<template>
  <v-container fluid>
    <b-card
    title="Card Title"
    img-src="/img/5legs-logo-blue-png-rgb.png"
    img-alt="Image"
    img-top
    tag="article"
    style="max-width: 60rem;"
    class="mb-2"
  >
    <b-card-title>"Dashboard"</b-card-title>
    <b-card-body>
      <b-card-img width="100px" src=""></b-card-img>
      <b-card-text>Wonderful Pistache</b-card-text>
      <b-button-group>
        <b-button href="/main/profile/view" variant="success">View Profile</b-button>
        <b-button href="/main/profile/edit" variant="info">Edit Profile</b-button>
        <b-button href="/main/profile/password" variant="warning">Change Password</b-button>
      </b-button-group>
    </b-card-body>
    </b-card>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import { Store } from 'vuex'
import { readUserProfile } from '@/store/main/getters'

@Component
export default class Dashboard extends Vue {
    get greetedUser() {
    const userProfile = readUserProfile(this.$store)
    if (userProfile && userProfile.full_name) {
      if (userProfile.full_name) {
        return userProfile.full_name
      } else {
        return userProfile.email
      }
    }
    }
}
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.flow-chart > svg {
  margin: 0 auto;
 }
</style>
