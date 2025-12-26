<template>
  <div>

     <client-only>

     <div class="horizontal-menu">
      
      <h3>Header</>

     </div>
  
  <Nuxt />

  </client-only>

  </div>
</template>

<script>

import axios from 'axios'

export default {
  name: 'LayoutMaster',

  methods: {
   
      async logout() {
        //Send Logout Request
        await axios({
            method: 'POST',
            url: this.$store.state.entry_api + '/logout',
            headers: {
                "Content-Type": "application/json",
                "Auth-User": this.$store.state.auth_user,
                "Auth-Token": this.$store.state.auth_token
            }
        }).then((response) => {
            var jsonData = JSON.parse(JSON.stringify(response.data));

            if (jsonData['status'] == true) {
              //Show Notification
              this.$toast.success('You have been Logged Out Successfully');

              //Clear Auth Data
              this.$store.commit('clear_auth_data')
        
              //Go to Core UI
              window.location.assign(this.$store.state.core_ui)
            }else {
              //Show Error on Logout
              this.$toast.error('Failed to Logout. Please Try Again...');
            }
            
        });

      }
  }

}
</script>
