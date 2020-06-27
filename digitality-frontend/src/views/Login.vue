<template>
  <div class="login">
    <h1 class="logo">Digitality</h1>
    <h3 style="color: #00a2ff;"> Prijava </h3>
    
      <div class="container">
        <div class="row">
          <div class="col-sm"></div>
              <div class="col-sm">

                <form v-on:submit.prevent="login">
                  <div class="email"> 
                      <i class="fa fa-envelope" id="iconEmail" aria-hidden="true"></i>
                      <input type="email" v-model="email" class="form-control placeholderEmail" aria-describedby="emailHelp" placeholder=" e-mail..." required />
                  </div>

                  <div class="password">
                      <i class="fas fa-key"></i>
                      <input type="password" v-model="password" class="form-control"  id="hidden_password" placeholder="lozinka..." required />
                      <i class="fas fa-eye" id="password_eye" v-on:click="show_password()"></i>

                  </div>
                  <h6 v-if="login_fail" style="color:red; font-size:12px">Neuspjela prijava, provjerite unesene podatke.</h6>
                  <small class="logReg">
                    <span>
                      Nemate korisnički račun?
                      <router-link to = "signup" style="padding-left:3px;"> 
                      Registracija 
                      </router-link>
                      !
                    </span>
                  </small>

                  <button type="submit" class="btn btn-primary">Prijava</button>
                </form>

              </div>
            <div class="col-sm"></div>
          </div>
      </div>
  </div>
</template>

<script>
import store from '@/store.js';
import { Auth } from "@/services";

export default {
  data(){
      return{
        email: "",
        password: "",
        store,

        login_fail: false,
        error_message: null
      }
    },
  methods: {
      async login() {
        let success = await Auth.login(this.email, this.password);

        if (success == true) {
          this.$router.push({ name: 'Home'});
        }
        else{
          this.login_fail = true;
        }
      },
      
      show_password() {
        let x = document.getElementById("hidden_password");
        
        if (x.type === "password"){
          x.type = "text";
          document.getElementsByClassName("fas fa-eye")[0].className = "fas fa-eye-slash";
        } 
        else{
          x.type = "password";
          document.getElementsByClassName("fas fa-eye-slash")[0].className = "fas fa-eye";
        } 
        
      }
    },
    
}
//popraviti: tri stupca na mobitelu i kompu drugaciji prikaz, dodati forgot password, popraviti za neke ekrane small tag se ne ponasa kako treba, staviti ikonu za brisanje maila?
</script>

<style scoped>

.logo{
  margin-bottom:5%;
  font-family: BillabongW00-Regular;
  font-size:80px;
  letter-spacing: 0;
  color: #000000;
  opacity: 1;
}

.btn{
  margin-top:25px;
  background-color: #00a2ff;
  text-align: center;
  font: Regular 40px/49px Montserrat;
  letter-spacing: 0;
  color: #FFFFFF;
  opacity: 1;
}

form{
  margin-top:50px;
}

input {
  border-color:white;
  font-size: 17.5px;
  width:250px;
  display: inline-block;

}

@keyframes lightBulb {
  
  50% {border-bottom-color: #00a2ff;}
}

.logReg{
  margin-top:5px;
  border: 1px solid white;
  animation: lightBulb 5s infinite;
  padding: 3px;
  text-align: left;
  color:#888888;
}


.login{
  position: relative;
  animation: drop 1s;
  animation-fill-mode: forwards;
  margin-top: 0% !important;
}

@keyframes drop {
  from {top: 0px;}
  to {top: 100px;}
}


::placeholder {
  color:#888888;
  margin-left: -20px;
}

i{
  
  position: relative;
  font-size: 20px;
  color:#888888;
  display: inline-block;
}

small{
  position:relative;
  margin-left: 12.5%;
  margin-right: 12.5%;
  display: flex;
  justify-content: center;
}


.email, .password{
        width: 300px;
        display: inline-block;
        margin: 10px;
        border-bottom:1px #00a2ff solid;
    }

#iconEmail{
  margin-left: -25px;
}

span{
  text-align: center;
}



</style>