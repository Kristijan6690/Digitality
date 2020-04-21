<template>
  <div class="login">
    <h1 class="logo">Digitality</h1>
    <h3 style="color: #00a2ff;">Prijava</h3>
    <div class="container">
      <div class="row">
        <div class="col-sm"></div>
        <div class="col-sm">
          <form v-on:submit.prevent="login">
            <div class="email">
              <i class="fa fa-envelope" id="iconEmail" aria-hidden="true"></i>
              <input
                type="email"
                v-model="email"
                class="form-control placeholderEmail"
                aria-describedby="emailHelp"
                placeholder=" e-mail..."
              />
            </div>

            <div class="password">
              <i class="fas fa-key"></i>
              <input
                type="password"
                v-model="password"
                class="form-control"
                id="hidden_password"
                placeholder="lozinka..."
              />
              <i class="fas fa-eye" id="password_eye" v-on:click="show_password()"></i>
            </div>
            <small class="logReg">
              <div class="border">
                Nemate korisnički račun?
                <router-link to="signup" style="padding-left:3px;">Registracija</router-link>!
              </div>
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
import axios from "axios";
import store from "@/store.js";
export default {
  data() {
    return {
      email: "",
      password: "",
      store
    };
  },
  methods: {
    async login() {
      let response = await axios.post("http://127.0.0.1:5000/login", {
        email: this.email,
        password: this.password
      });
      let vrijednost = await response.data;
      if(vrijednost) {
        this.store.userData = vrijednost;
        console.log(this.store.userData)
        //this.$router.push({ name: 'Home'})
      }
      else{
        console.log("Invalid username or password")
      }
    },
    show_password() {
      let x = document.getElementById("hidden_password");

      if (x.type === "password") {
        x.type = "text";
        document.getElementsByClassName("fas fa-eye")[0].className =
          "fas fa-eye-slash";
      } else {
        x.type = "password";
        document.getElementsByClassName("fas fa-eye-slash")[0].className =
          "fas fa-eye";
      }
    }
  }
};
</script>

<style scoped>
.logo {
  margin-bottom: 5%;
  font-family: BillabongW00-Regular;
  font-size: 80px;
  letter-spacing: 0;
  color: #000000;
  opacity: 1;
}

.btn {
  margin-top: 25px;
  background-color: #00a2ff;
  text-align: center;
  font: Regular 40px/49px Montserrat;
  letter-spacing: 0;
  color: #ffffff;
  opacity: 1;
}

form {
  margin-top: 50px;
}

input {
  border-color: white;
  font-size: 17.5px;
  width: 250px;
  display: inline-block;
}

@keyframes mymove {
  50% {
    border-bottom-color: #00a2ff;
  }
}

.logReg {
  margin-top: 5px;
  padding: 3px;
  text-align: center;
  color: #888888;
}

.border {
  animation: mymove 5s infinite;
}

.login {
  position: relative;
  animation: mymove2 2s;
  animation-fill-mode: forwards;
  margin-top: -5%;
}

@keyframes mymove2 {
  from {
    top: 0px;
  }
  to {
    top: 100px;
  }
}

::placeholder {
  color: #888888;
  margin-left: -20px;
}

i {
  position: relative;
  font-size: 20px;
  color: #888888;
  display: inline-block;
}

small {
  position: relative;
  margin-left: 12.5%;
  margin-right: 12.5%;
  display: flex;
  justify-content: center;
}

.email,
.password {
  width: 300px;
  display: inline-block;
  margin: 10px;
  border-bottom: 1px #00a2ff solid;
}

#iconEmail {
  margin-left: -25px;
}

.form-control > .placeholderEmail {
  padding-left: 30px;
  background-color: red;
  color: red;
}
</style>