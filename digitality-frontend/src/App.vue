<template>
  <div id="app">
        <!-- navbar -->
        <nav v-if="this.$route.name !== 'Login' && this.$route.name !== 'Signup' " class="navbar navbar-expand-lg navbar-light bg-light border " >
              <a class="navbar-brand" id="navbarDesktop" href="/">
                <div class="logo-brand ">
                   <img src="/Images/logo.png"/>
                </div>
              </a> 
              <!-- logo na mobitelu (kvalitetniji prikaz nego png) -->
              <a class="navbar-brand" id="navbarMob" href="/">
                <div class="logo-brand ">
                  Digitality
                </div>
              </a> 
            
              <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>

              <div class="collapse navbar-collapse" id="navbarSupportedContent">
                  <ul class="navbar-nav mr-auto">
                    <li class="nav-item active">
                      <router-link to="/" class="nav-link" > Arhiva <span class="sr-only">(current)</span></router-link>  <!-- current?-->
                    </li>
                    <li class="nav-item active"> 
                        <router-link to="/scan" class="nav-link"> Skeniraj <span class="sr-only">(current)</span></router-link>    
                    </li>

                    <li class="nav-item active">
                        <router-link to="/manualscan" class="nav-link"> Ručno dodavanje <span class="sr-only">(current)</span></router-link>    
                    </li>
                  </ul>
                  <button class="btn btn-primary my-2 my-sm-0" type="submit" style="border-radius: 5px;">Odjavi se</button> <!-- maknuti da nije submit -->
              </div>
          </nav>
    <router-view/>
  </div>
</template>

<script>
import store from '@/store.js';
import { app } from "@/services";

export default {
  data(){
    return {
      store
    }
  },

  async mounted() {
    let result = await app.getArchives() // jos nadogradit da vuce za određenog usera
    if (result) this.store.archiveData = result
    else console.log("Prazan collection")
  }
}
</script>

<style lang="scss">

// popraviti : povezati putanje route u index.js , hover i active na izbore menija, backend logotipa, navbar fiksan?

#app {
  font-family:  'Montserrat', Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.navbar-brand{
  font-family: BillabongW00-Regular;
  font-size:50px;
  letter-spacing: 0;
  opacity: 1;
}

.logo-brand{
  margin: -10px 20px -30px 0px;
}

.nav-item {
  padding-right: 10px;
  padding-left: 10px;
  font-size: 20px;
}

.border {
  border: 2px solid #00a2ff !important;
}

.navbar-light {
    background-color: white !important;
}

/*
router-link:hover{
   color: #00FF00; 
} 
*/

@media screen and (min-width: 1024px){
 #navbarMob{
   display:none;
 }
}

/*###Tablet(medium)###*/
@media screen and (min-width : 768px) and (max-width : 1023px){
#navbarMob{
   display:none;
 }
 
}

/*### Smartphones (portrait and landscape)(small)### */
@media screen and (min-width : 0px) and (max-width : 767px){
  
#navbarDesktop{
   display:none;
 }

#navbarMob{
  padding-top: 0px;
  padding-bottom: 10px;
}


}
</style>
