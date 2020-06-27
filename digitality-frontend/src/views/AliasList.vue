<template>
  <div class="home">
    <div class="container">
      <div class="row" style="margin-bottom:0px;">
      <div class="col heading">        
        <div  id="headlineDiv"><h1 id="headline">Popis aliasa</h1></div>
          <button type="button" class="glowEffect" data-toggle="modal" data-target="#helpModal" style="border:none;"><i class="fas fa-info-circle fa-2x" ></i></button>
        </div>         
      </div>
            
      <RemoveAlias v-bind:key="card.id" v-bind:info="card" v-for="card in user.alias_list" />
            
      <form>
        <div class="row main"  >
            <div class="data">
              <label for="Ime">Ime:</label>
              <input v-model="alias.ime" type="text" id="Ime" name="Alias" required>
            </div>
            <div class="data">
              <label for="Prezime">Prezime:</label>
              <input v-model="alias.prezime" type="text" id="Prezime" name="Alias" required>
            </div> 
            <div class="data">
              <label for="OIB">OIB:</label>
              <input v-model="alias.oib" type="text" id="OIB" name="Alias" required>
            </div> 
            <div class="data">
              <label for="IBAN">IBAN:</label>
              <input v-model="alias.iban" type="text" id="IBAN" name="Alias" required>
            </div> 
            <div class="dataLong">
              <label for="PostanskBroj">Poštanski broj:</label>
              <input v-model="alias.postanski_broj" type="text" id="PostanskiBroj" name="Alias" required>
            </div> 
            <div class="button">
              <button @click="addUserAlias" type="button" style="border:none;"><i class="fa fa-plus" aria-hidden="true" style="color:#00A2FF"></i></button>
            </div> 
        </div>
      </form>
      
      <div class="row" style="padding-top:50px; display:inline-block; text-align:center; width:100%;"> 
        <div>Moj korisnički račun: <span style="color:black"> {{user.email}} </span></div>
        <button data-toggle="modal" data-target="#password_modal" style="color:#FF6347; border:none; display:inline-block;">Obriši Korisnički račun!</button>      
      </div>
      <!-- Modal -->
      <div class="modal fade" id="helpModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
          <div class="modal-content">
            <div class="modal-header" style="display:block;">
              <h3 class="'col-12 modal-title text-center'" id="exampleModalLongTitle" style="color:#000000;">Pomoć</h3>
            </div>
            <div class="modal-body" style="border: 1px solid black; margin-left: 10px; margin-right: 10px;">
              <p> 
                Popis aliasa služe kako bi se detektirali računi koji nisu nužno na vlasnika, nego primjerice na ženu itd...
              </p> 
            </div>
            <div class="modal-footer" style="text-align:center; display:block;">
              <button type="button" class="btn btn-secondary" data-dismiss="modal" style="background-color:#00A2FF">Zatvori</button>
            </div>
          </div>
        </div>
      </div>

      <div class="modal fade" id="password_modal" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
          <div class="modal-content" style="solid; text-align: center; border-radius: 7.5px; ">
            
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalLabel">Upišite vašu lozinku za potvrdu brisanja</h5>
            </div>

            <div class="modal-body" style="font-size: 30px; color:#00A2FF;">
              <form>
                <div class="form-group">
                  <input v-model="password" type="password" class="form-control" style="text-align:center" id="recipient-name" required>
                </div>
              </form>
            </div>

            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">Zatvori</button>
              <button v-on:click="delete_user" type="button" class="btn btn-primary" data-dismiss="modal" style="background: red; color: white;">Obriši</button>
            </div>

          </div>
        </div>
      </div>

      <!-- success confirmation -->
      <div class="modal fade" id="deletion_success" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document" >
          
          <div class="modal-content" style="solid; text-align: center; border-radius: 7.5px; ">
              <div class="modal-body" style="font-size: 30px; color:#00A2FF;">
                   Korisnički račun obrisan zajedno sa arhivom!
                  <hr/>
                  <div data-dismiss="modal" style="font-size:20px; color:#707070">Ok</div>
              </div>
          
            </div>
        </div>
      </div>

      <div class="modal fade" id="success_confirmation" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document" >
          
          <div class="modal-content" style="solid; text-align: center; border-radius: 7.5px; ">
              <div class="modal-body" style="font-size: 30px; color:#00A2FF;">
                   Alias uspiješno dodan na vaš popis
                  <hr/>
                  <div data-dismiss="modal" style="font-size:20px; color:#707070">Ok</div>
              </div>
          
            </div>
        </div>
      </div>

      <!-- error confirmation -->
      <div class="modal fade" id="error_confirmation" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document" >
          
          <div class="modal-content" style="solid; text-align: center; border-radius: 7.5px; ">
              <div class="modal-body" style="font-size: 30px; color:#00A2FF;">
                   Došlo je do greške.
                  <hr/>
                  <div data-dismiss="modal" style="font-size:20px; color:#707070">Ok</div>
              </div>
          
            </div>
        </div>
      </div>

    </div>
  </div>
</template>
<!-- popraviti :  label value,mobile responsive, footer?, hovere na sve-->
<script>

import store from '@/store.js';
import RemoveAlias from '@/components/RemoveAlias.vue'
import { app } from "@/services";
import { Auth } from "@/services";

export default {
  data(){
    return {
      store,
      user: Auth.getUser(),
      alias: {},
      password: null
    }
  },
  name: 'Home',
  components: {
    RemoveAlias
  },

  methods:{
    async addUserAlias(){
      await app.add_alias(this.alias)
      this.alias = {}
    },

    async delete_user(){
      let res = await app.delete_user(this.password)
      
      if(res){
        Auth.logout()
        this.$router.go();
      } 
      this.deletion_modal(res)
    },

    deletion_modal(success){
      if(success) 
        $("#deletion_success").modal()
      else 
        $("#error_confirmation").modal()
    }

  }
}
</script>

<style scoped>
.deletion_buttons{
  background: none;
  border: none;
  border-radius: 5px;

  font-size:20px; 
  color: #707070
}

.row{
    margin-right: 0px;
    margin-left: 0px;
    background-color:#eeeeee;
}

.main{
  width:100%;
  margin:auto;
}


.archive-options{
  height: 50px;
  text-align: center;
  display: inline-block;
  position:relative;
  padding-right: 10px;
  padding-left: 10px;

}

.archive{
  background-color: #EEEEEE;
  height: 400px;
  float:left;
  /*border-radius: 10px;  -> varijanta za white archive options*/
  padding-left:15px;  /* varijanta bez paddinga? */
  padding-right:15px;
  /* border-bottom: 2px solid  #00A2FF;  -border za footer */
}

input, #billTypeDropdown{
    display:inline-block;
    width:55%;
    border-radius: 5px;
    border: 1px solid  #00A2FF;
    padding-left: 10px;
    padding-right: 10px;
    height:28px; 
}

label{
    color:black;
    display:inline-block;
    margin-bottom: 0px;
    text-align:left;
    width: 45%;
    text-align: center;

}

.data{
    display:inline-block;
    margin-bottom: .5rem; 
    width:170px;  
}

.dataLong{
    display:inline-block;
    margin-bottom: .5rem; 
    width:350px;  
}

a{
  color: #2c3e50; 
}


 ::placeholder {
  color: #7B7C73;
  margin-left: -20px;
}   

.fa-info-circle{
  color:#00A2FF; 
  float: right;
}



.heading{
  background-color: #EEEEEE;
  line-height: 75px !important;
  text-align: center;
  display: inline-block;
  position:relative;
  padding-right: 37.5px;
  padding-left: 37.5px; 
  display: flex; 
  align-items: center; 
  text-align:center; 
}

#headline{
  display:inline-block; 
  color: #000000; 
  font-size: 40px;
  margin-bottom: 0px;
  text-align:center; 
}

#headlineDiv{
  width: 100%; 
  padding-left:44px;
  text-align:center; 
}


#button{
  display:inline-block; 
  width:340px;
  
}


@keyframes glow {
  80%, 100% {
      text-shadow: 0 0 5px #00A2FF;
  }
}

.glowEffect {
  animation: glow 2s 4;
  overflow-x: hidden;
  overflow-y: hidden;
  opacity: 1; 
}


/*### Smartphones (portrait and landscape)(small)### */
@media screen and (min-width : 0px) and (max-width : 767px){

.row{
  margin-bottom: 20px;
}
 
input{
    display:inline-block;
    width:55%;
    border-radius: 5px;
    border: 1px solid  #00A2FF;
    padding-left: 10px;
    padding-right: 10px;
}

label{
    color:black;
    display:inline-block;
    width:45%;
    margin-bottom: 0px;
    font-size: 15px;
}

.container{
    padding-right: 0px; 
    padding-left: 0px;
}


#headline{
  font-size:30px;
}

.heading{
  line-height: 0px;
  height: 100px;
}

.dataLong{
    display:inline-block;
    margin-bottom: .5rem; 
    width:340px;  
}

.button{
  display:block; 
  width:100%;
  
}

}
</style>
