<template>
  <div class="home">
      <div class="container">
            <div class="row">
                <!-- mjesto za header ako ce ici -->
            </div>
            <div class="row">
                 <div class="col heading">        
                    <div  id="headlineDiv" ><h1 id="headline">Popis aliasa</h1></div>
                    <button type="button" class="glowEffect" data-toggle="modal" data-target="#helpModal" style="border:none;"><i class="fas fa-info-circle fa-2x" ></i></button>
                </div>         
            </div>
            <form action="/action_page.php">

                <RemoveAlias />
                
                <div class="row main"  >
                    
                    <div class="data">
                        <label for="Ime">Ime:</label>
                        <input v-model="Ime" type="text" id="Ime" name="Alias" required>
                    </div>
                    <div class="data">
                        <label for="Prezime">Prezime:</label>
                        <input v-model="Prezime" type="text" id="Prezime" name="Alias" required>
                    </div> 
                    <div class="data">
                        <label for="OIB">OIB:</label>
                        <input v-model="OIB" type="text" id="OIB" name="Alias" required>
                    </div> 
                    <div class="data">
                        <label for="IBAN">IBAN:</label>
                        <input v-model="IBAN" type="text" id="IBAN" name="Alias" required>
                    </div> 
                    <div class="dataLong">
                        <label for="PostanskBroj">Poštanski broj:</label>
                        <input v-model="PostanskiBroj" type="text" id="PostanskiBroj" name="Alias" required>
                    </div> 
                    <div style="display:inline-block">
                        <button style="border:none;"><i class="fa fa-plus" aria-hidden="true" style="color:#00A2FF"></i></button>
                    </div> 

                </div>
            </form>

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
            
            <!-- footer
            <div class="row">
                <div class="col archive"></div>
            </div>
            -->
<!-- success confirmation -->
      <div class="modal fade" id="success_confirmation" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document" >
          
          <div class="modal-content" style="solid; text-align: center; border-radius: 7.5px; ">
              <div class="modal-body" style="font-size: 30px; color:#00A2FF;">
                   Dokument dodan u arhivu _____
                  <hr/>
                  <div data-dismiss="modal" style="font-size:20px; color:#707070">Ok</div>
              </div>
          
            </div>
        </div>
      </div>

      
      <!-- error confirmation -->
      <div class="modal fade" id="success_confirmation" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document" >
          
          <div class="modal-content" style="solid; text-align: center; border-radius: 7.5px; ">
              <div class="modal-body" style="font-size: 30px; color:#00A2FF;">
                   Došlo je do greške prilikom učitavanja dokumenta
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

export default {
  data(){
    return {
      store
    }
  },
  name: 'Home',
  components: {
    RemoveAlias
  },

  methods:{
    
  }
  
}
</script>

<style scoped>

/* clickable icon in input field: https://stackoverflow.com/questions/6933941/clickable-icon-inside-input-field */
.input-with-icon {
  position: relative;
  width: 25rem;
  box-sizing: border-box;
}

.input-with-icon .form-control {
    height: 100%;
    width: 70%;
    padding-right: 5%;
    box-sizing: border-box;
}

.input-with-icon .icon {
  position: absolute;
  right: 0.3rem;
  top: 0.3rem;
  width: 2.6rem;
  height: 20px;
  border-radius: 0.3rem;
  display: flex;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
}
/* */

.row{
    margin-right: 0px;
    margin-left: 0px;
    background-color:#eeeeee;
}

.main{
  width:100%;
  margin:auto;
}
.box{
  vertical-align: top;
  display: inline-block;
  box-sizing: border-box;
  height: 170px;
}

.one {
  width: 50%;
}

.two { 
  width: 50%;
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

.chooseArchive{
  width: 150px;
  height: 30px;
  background-color: white;
  display: block;
  margin: 10px 0 10px 0;
  float: left;
  border-radius: 5px;
  border: 2px solid  #00A2FF;
}

.settings{
  width: 30px;
  height: 30px;
  background-color: white;
  display: block;
  margin: 10px 5px;
  float: left;
  border-radius: 5px;
  border: 2px solid  #00A2FF;
  padding-top:3px;
  
}

.search{
  width: 180px;
  height: 30px;
  background-color: white;
  display: block;
  margin: 10px 0 10px 0;
  float: right;
  border-radius: 5px;
  border: 2px solid  #00A2FF;
}


.filter{
  width: 30px;
  height: 30px;
  background-color: white;
  display: block;
  margin : 10px 5px  10px 5px; 
  float: right;
  border-radius: 5px;
  border: 2px solid  #00A2FF;
  padding-top: 4px;
  color:#00A2FF;
  
}

#searchBar{
  width: 80%;
  height: 100%;
  color:#00a2ff;
  outline: none;
  border: 0px;
}

#searchIcon{ 
  color:#00A2FF;
  padding-left: 7.5px;
}

 ::placeholder {
  color: #7B7C73;
  margin-left: -20px;
}   

.fa-info-circle{
  color:#00A2FF; 
  float: right;
}


#archiveSelector{
  width: 80%;
  height: 100%;
  color:#00a2ff;
  border: 0px;
  outline: none;
  border: 0px;
}

.fa-cog{
  color:#00a2ff;
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

.datumDospijeca{
    padding-top: 12px;
}

.addButtonDiv{
display: flex; 
align-items: center; 
justify-content: center; 
height: 75px; 
background-color: #f6f6f2;
}

#addButton{
  font-size:20px; 
  width:150px;
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

/*   exchange icon positioning */

/* enable absolute positioning */
.inner-addon { 
    position: relative; 
}

/* style icon */
.inner-addon .fas {
  position: absolute;
  padding: 5px;
  pointer-events: none;
}

/* align icon */
.right-addon .fas { right: 0px;}

/* add padding  */
.right-addon input { padding-right: 30px; }

/* y@media screen and (min-width: 1024px){} */

@media screen and (min-width : 992px) and (max-width : 1200px){
 input{
    display:inline-block;
    width:65%;
    border-radius: 5px;
    border: 1px solid  #00A2FF;
    padding-left: 10px;
    padding-right: 10px;
}

label{
    color:black;
    display:inline-block;
    width:35%;
    margin-bottom: 0px;
    text-align:left;
    font-size: 15px;
}
}

@media screen and (min-width : 768px) and (max-width : 991px){
  input,  #billTypeDropdown{
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
    text-align:left;
    font-size: 15px;
}

}

/*### Smartphones (portrait and landscape)(small)### */
@media screen and (min-width : 0px) and (max-width : 767px){
 
.box{
    display: block;
    height: auto;
  }

.one {
    width: 100%;
}

.two {
    width: 100%;
}

br {
    display:none; 
} 

.datumDospijeca{
    padding-top: 0px;
}

input, #billTypeDropdown{
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
    text-align:left;
    font-size: 15px;
}

.container{
    padding-right: 0px; 
    padding-left: 0px;
}

.addButtonDiv{
   background-color: #EEEEEE;
}

#headline{
  font-size:30px;
}

.heading{
  line-height: 0px;
  height: 100px;
}


/* clickable icon in input field: https://stackoverflow.com/questions/6933941/clickable-icon-inside-input-field */
.input-with-icon {
  position: relative;
  box-sizing: border-box;
  text-align: left;
  width: 100%;
}

.input-with-icon .form-control {
    height: 100%;
    width: 55%;
    box-sizing: border-box;
    
}

.input-with-icon .icon {
  position: absolute;
  right: 0.3rem;
  top: 0.3rem;
  width: 2.6rem;
  height: 20px;
  border-radius: 0.3rem;
  display: flex;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
}
/* */

}
</style>
