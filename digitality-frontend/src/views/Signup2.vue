<template>
  <div class="signup">
    <h1 class="logo">Digitality</h1>
    <h3 style="color: #00a2ff;"> Registracija</h3>
    <div class="container">
        <form>
  <div class="row d-flex justify-content-center">
    
    <div class="col col-sm-3 nameSurname">
      <i class="fas fa-user"></i>
      <input type="email" class="form-control placeholderEmail" aria-describedby="emailHelp" placeholder=" ime i prezime..."  />
    </div>
    
    <div class="col col-sm-3 email">
       <i class="fa fa-envelope" id="iconEmail" aria-hidden="true"></i>
       <input type="email" class="form-control placeholderEmail" aria-describedby="emailHelp" placeholder=" e-mail..."  />
    </div>
    
  </div>
  <div class="row d-flex justify-content-center">
    <div class="col col-sm-3 password">
       <i class="fas fa-key"></i>
       <input type="password" class="form-control"   placeholder="lozinka..."  />
    </div>
   
    <div class="col col-sm-3 password">
      <i class="fas fa-lock"></i>
      <input type="password" class="form-control"   placeholder="ponovi lozinku..."  />
    </div>
    
  </div>
  </form>
  <div class="row  d-flex justify-content-center">
    <small class="logReg ">
            Imate korisnički račun?
            <router-link to = "login" style="padding-left:3px;"> 
              Prijavite se 
            </router-link>
            !
    </small>
  </div>
    <button type="submit" class="btn btn-primary">Registracija</button>
</div>
  </div>
</template>

<script>
export default {
  
}
</script>

<style scoped>

.container{
    margin-top:100px;
    padding-left:30px;
    padding-right:30px;
}

.col{
    padding:0px;
    margin-left:0px;
    

}

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

@keyframes mymove {
  
  50% {border-bottom-color: #00a2ff;}
}

.logReg{
  margin-top:5px;
  border: 1px solid coral;
  animation: mymove 5s infinite;
  border-color:white;
  padding: 3px;
  text-align: left;
}

.signup{
  position: relative;
  animation: mymove2 1s;
  animation-fill-mode: forwards;
  margin-top: -15%;
}

@keyframes mymove2 {
  from {top: 0px;}
  to {top: 100px;}
}



::placeholder {
  color:#888888;
  margin-left: -1px;
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


.email, .password, .nameSurname{
        width: 300px;
        display: inline-block;
        margin: 10px;
        padding-left: 0px;
        border-bottom:1px #00a2ff solid;
    }

.form-control > .placeholderEmail {
  padding-left: 30px;
  background-color:red;
  color:red;
}

div > .col{
  display: flex;
  align-items: center;
  justify-content: center;
  
}

.col-sm-3{
  padding-left: 5px;
}

@media (min-width: 576px){
.col-sm-3 {
    -webkit-box-flex: 0;
    -ms-flex: 0 0 25%;
    flex: 0 0 25%;
    max-width: 50%;
 }  
} 

</style>