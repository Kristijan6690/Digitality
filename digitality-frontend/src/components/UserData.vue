<template>
    <div class="userData" >
        <div class="personIcon"><i class="far fa-user"></i></div>
        <div class="mailOsobe">{{info}}</div> 
        <button @click="removeUserAccess" class="opcijaPopis">ukloni</button>  
    </div>
</template>

<script>
import store from "@/store.js";
import { Auth } from "@/services";
import { app } from "@/services";

export default {
  data() {
    return {
      user: Auth.getUser()
    };
  },
  props: ["info"],

  methods:{
    async removeUserAccess(){
      let result = await app.delete_shared_archive(this.info)
      if(!result) return 

      let email_list = this.user.email_list;
      this.user.email_list = email_list.filter(email => email != this.info)
      
      localStorage.setItem("user", JSON.stringify(this.user))
      location.reload();
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

.userData{
  display: flex;
}

.personIcon{
  display:inline-block;
}

.mailOsobe {
  display:inline-block; 
  width:200px;   
  text-align: center; 
  overflow: hidden;
  text-overflow: ellipsis;
  height: 30px;
}

.opcijaPopis{
  display:inline-block; 
  color:#FF0000; 
  width: 75px;
  text-align: center;
  border:none;
  background-color: white;
}

</style>
