<template>
  <div class="home">
      <div class="container">
        <div class="row">
            <div class="col archive-options">

                   <!-- settings dropdown -->
                      <div class="btn-group" >
                        <button type="button" class="btn btn-secondary settings" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" >
                          <div id="settingsIcon" ><i class="fas fa-cog fa-lg"></i></div>
                        </button>

                        <div class="dropdown-menu dropdown-menu-left menu-settings" @click.stop=''>
                          <div class="dropdownHeader" > 
                              <h2 id="dropdownHeaderHeadline"> Postavke </h2> 
                          </div>
                          <div id="archiveName" >
                              <div class="editIcon">
                                <i class="far fa-edit"></i>
                              </div>
                              <div class="changeName" >
                                <h5 id="changeNameHeader"> Moja_arhiva </h5> 
                              </div>
                          </div>
                          <div class="dropdownBody body-settings" >                       
                              <div id="pristupNaslov">
                                <h6 id="pristupNaslovHeader"><b>Osobe sa pristupom</b></h6>
                              </div>
                                <div id="pristupPopis">  

                                <UserData />
                                <UserData />
                                <UserData />

                                <div class="userData "  >
                                     <div class="personIcon"><i class="far fa-user"></i> </div>
                                     <div class="mailOsobe addUserName">example@email.com</div> 
                                     <div class="opcijaPopis addUserButton">dodaj</div>  
                                </div>
                              
                              </div>
                            </div>
                          <div class="dropdownFooter addButtonDiv">
                                <button type="submit" class="btn btn-primary my-2 my-sm-0" id="addButtonSettings" style="margin: 5px; border-radius:5px; border:0" > Spremi </button>
                                <button type="submit" class="btn btn-primary my-2 my-sm-0" id="removeButtonSettings" style="margin: 5px;  border-radius:5px; background-color: #888888; border:0"> Poništi</button>
                          </div>
                      </div>
                    </div>
                    
                  <div class="chooseArchive">
                      <i class="far fa-file fa-lg" ></i>
                      <select id="archiveSelector">
                          <option value="Archive_1">Internet</option>
                          <option value="Archive_2">Struja</option>
                          <option value="Archive_3">Voda</option>
                          <option value="Archive_4">Ostalo</option>
                        </select>
                  </div>
                   <!-- filter i filter dropdown -->
                      <div class="btn-group" >
                        <button type="button" class="btn btn-secondary filter glowEffect" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                          <div id="filterIcon" ><i class="fa fa-filter  fa-lg"  aria-hidden="true" ></i></div>
                        </button>

                        <div class="dropdown-menu dropdown-menu-right" @click.stop=''>
                          <div class="dropdownHeader" > 
                              <h2 >Filter</h2> 
                          </div>

                          <div class="dropdownBody">                       
                              <div class="filterOptions custom-control custom-checkbox " >
                                <input v-model ="store.filter_checks.datum_dodavanja_check" type="checkbox" class="custom-control-input" id="datDodavanja" name="datDodavanja" value="datDodavanja">
                                <label for="datDodavanja" class="custom-control-label">Datum dodavanja:</label>
                                <input v-model ="store.filter.datum_dodavanja" type="text" id="datDodavanja" name="datDodavanja"><br>
                              </div>
                              <div class="filterOptions custom-control custom-checkbox ">
                                <input v-model ="store.filter_checks.naziv_dobavljača_check" type="checkbox" class="custom-control-input" id="nazDobavljaca" name="nazDobavljaca" value="nazDobavljaca">
                                <label for="nazDobavljaca" class="custom-control-label" >Naziv dobavljača:</label>
                                <input v-model ="store.filter.naziv_dobavljača" type="text" id="nazDobavljaca" name="nazDobavljaca"><br>
                              </div>
                              <div class="filterOptions custom-control custom-checkbox ">
                                <input v-model ="store.filter_checks.datum_izdavanja_check" type="checkbox" class="custom-control-input" id="datIzdavanja" name="datIzdavanja" value="datIzdavanja">
                                <label for="datIzdavanja" class="custom-control-label">Datum izdavanja:</label>
                                <input v-model ="store.filter.datum_izdavanja" type="text" id="datIzdavanja" name="datIzdavanja"><br>
                              </div>
                              <div class="filterOptions custom-control custom-checkbox ">
                                <input v-model ="store.filter_checks.datum_dospijeća_check" type="checkbox" class="custom-control-input" id="datDospijeca" name="datDospijeca" value="datDospijeca">
                                <label for="datDospijeca" class="custom-control-label">Datum dospijeća:</label>
                                <input v-model ="store.filter.datum_dospijeća" type="text" id="datDospijeca" name="datDospijeca"><br>
                              </div>
                              <div class="filterOptions custom-control custom-checkbox ">
                                <input v-model ="store.filter_checks.vrsta_usluge_check" type="checkbox" class="custom-control-input" id="vrstaUsluge" name="vrstaUsluge" value="vrstaUsluge">
                                <label for="vrstaUsluge" class="custom-control-label">Vrsta usluge:</label>
                                <input v-model ="store.filter.vrsta_usluge" type="text" id="vrstaUsluge" name="vrstaUsluge"><br>
                              </div>
                              <div class="filterOptions custom-control custom-checkbox ">
                                <input v-model ="store.filter_checks.kolicina_check" type="checkbox" class="custom-control-input" id="kolicina" name="kolicina" value="kolicina">
                                <label for="kolicina" class="custom-control-label">Kolicina:</label>
                                <input v-model ="store.filter.kolicina" type="text" id="kolicina" name="kolicina"><br>
                              </div>
                              <div class="filterOptions custom-control custom-checkbox ">
                                <input v-model ="store.filter_checks.iznos_check" type="checkbox" class="custom-control-input" id="iznos" name="iznos" value="iznos">
                                <label for="iznos" class="custom-control-label">Iznos:</label>
                                <input v-model ="store.filter.iznos" type="text" id="iznos" name="iznos"><br>
                              </div>
                            
                          </div>
                          <div class="addButtonDiv">
                                <button v-on:click = "filter_trazi()" type="submit" class="btn btn-primary my-2 my-sm-0" id="addButtonFilter"> Traži </button>
                                <button v-on:click = "filter_obrisi()" type="submit" class="btn btn-primary my-2 my-sm-0" id="removeButtonFilter"> Očisti filter</button>
                          </div>
                      </div>
                    </div>
                  <form class="search">
                      <input v-model = "searchTerm" id="searchBar" type="text" placeholder="Traži..."/>
                      <i class="fas fa-search fa-lg" id="searchIcon"></i>
                  </form>
                  
            </div>         
        </div>
        <div class="row">
            <div class="col heading">
                  <!-- maknuti submit iz buttona? -->
                  <button type="submit" v-on:click="go_back()" class="btn btn-pr imary my-2 my-sm-0" id="backButton">Natrag</button>             
                  <div style="width: 100%;" id="headlineDiv"><h1 id="headline">Internet</h1></div>
                  <button type="button" class="btn btn-primary my-2 my-sm-0" id="deleteButton"  data-toggle="modal" data-target="#delete_confirmation">Izbriši</button>
            </div>         
        </div>

            <!-- Delete modal -->
            <div class="modal fade" id="delete_confirmation" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
              <div class="modal-dialog modal-dialog-centered" role="document">
                <div class="modal-content" style="border-radius: 7.5px;">
                  <div class="modal-header">
                    <h5 class="col-12 modal-title text-center" id="exampleModalLongTitle" style="font-size: 30px;  color:#00A2FF;"> Potvrdite brisanje </h5>
                  </div>
                  <!-- <div class="modal-body"> </div> -->
                  <div class="modal-footer">
                    <div  style="display: inline-block; font-size: 25px; width: 50%; color: green" data-dismiss="modal" data-toggle="modal" data-target="#success_confirmation"><i class="fas fa-check"></i></div>
                    <div style="display: inline-block; font-size: 25px; width: 50%; color: red"  data-dismiss="modal"><i class="fas fa-times"></i></div>  
                  </div>
                </div>
              </div>
            </div>

            <!-- delete success confirmation -->
            <div class="modal fade" id="success_confirmation" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered" role="document" >
                
                <div class="modal-content" style="solid; text-align: center; border-radius: 7.5px; ">
                    <div class="modal-body" style="font-size: 30px; color:#00A2FF;">
                        Uspješno izbrisano
                        <hr/>
                        <div data-dismiss="modal" style="font-size:20px; color:#707070">Ok</div>
                    </div>
                
                  </div>
              </div>
            </div>
        <div class="row">
            <div class="col archive">
              <Document v-bind:key="card.id" v-bind:info="card" v-for="card in store.documentData" /> 
              <!-- sastav komponente
              <div class="document" >
                  <div class="documentName">Lorem ipsum</div>
                  <div class="documentPicDiv">
                        <img src="align-justify.png" class="documentPic" />
                  </div>
                  <div class="documentDate">01/01/2020 at 00:00</div>
              </div>
              -->
            </div>


        </div>
        <!-- footer
        <div class="row">
            <div class="col archive"></div>
        </div>
        -->
      </div>
  </div>
</template>
<!-- popraviti :  clear custom filters ikona ,da dugi nazivi neidu izvan mobile responsive, footer? back i delete buttoni na mobitelu -> back btn netreba na mobu, delete u settings?-->
<!-- waves effect <div class="form-group waves-light waves-effect waves-light" style="width:100%;">  -->
							
<script>

import Document from '@/components/Document.vue';
import UserData from '@/components/UserData.vue';
import store from '@/store.js';
import { app } from "@/services";
import _ from "lodash";

export default {
  data(){
    return {
      naziv: this.$route.params.naziv_arhive,  //naziv_arhive -> varijabla u /router/index.js
      searchTerm: '',
      tempDoc: '',
      store
    }
  },

  name: 'SubArchive',  //krivo ?
  components: {
    Document,
    UserData
  },

  watch: {
    "searchTerm": _.debounce(function(val) {
      this.searchDocuments(val);
    }, 500)
  },

  methods : {
    go_back(){
      return this.$router.go(-1);
    },

    filter_obrisi(){
      let varijable_filtera = Object.keys(this.store.filter)

      for(let i = 0; i < varijable_filtera.length; i++) {
        if(this.store.filter[varijable_filtera[i]] != '') {
          this.store.filter[varijable_filtera[i]] = ''
        }
      }
    },

    filter_trazi() {
      let filter_podaci = {}
      let varijable_filtera = Object.keys(this.store.filter)
      let varijable_filtera_checks = Object.keys(this.store.filter_checks)

      for(let i = 0; i < varijable_filtera.length; i++) {
        if(this.store.filter_checks[varijable_filtera_checks[i]]) {
          filter_podaci[varijable_filtera[i]] = this.store.filter[varijable_filtera[i]]
        }
      }
      //samo primjer filtriranja za sada:
      if(Object.keys(filter_podaci).length > 0) {
        let regex = new RegExp (`^(${filter_podaci.naziv_dobavljača.toLowerCase()})`)
        this.store.documentData = {}
        console.log(this.store.documentData)

        for(let j = 0; j < Object.keys(this.tempDoc).length; j++){
          if(this.tempDoc[j].naziv.toLowerCase().match(regex)){
            this.store.documentData[j] = this.tempDoc[j] 
          }
        }
      }
    },

    async searchDocuments(pretraga){
      if(this.searchTerm) {
        pretraga = this.searchTerm.toLowerCase()
        let regex = new RegExp (`^(${pretraga})`)
        this.store.documentData = {}

        for(let i = 0; i < Object.keys(this.tempDoc).length; i++){
          if(this.tempDoc[i].naziv.toLowerCase().match(regex)){
            this.store.documentData[i] = this.tempDoc[i] 
          }
        }
      } else {
        this.store.documentData = this.tempDoc
      }
    },

  },

  async mounted() {
    let result = await app.getDocuments(this.naziv);  // Još nadograditi da vuce doc za određenog usera
    if (result) {
      this.store.documentData = result
      this.tempDoc = result
    }
    else {
      this.store.documentData = ''
      console.log("Korisnik nema dokumenta")
    }
    $('#element').popover('show')
  }
}
</script>

<style scoped>

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
  height: 1400px;
  float:left;
  margin-top: 0px;
  /*border-radius: 10px;  -> varijanta za white archive options*/
  padding-left:15px;  /* varijanta bez paddinga? */
  padding-right:15px;
  /* border-bottom: 2px solid  #00A2FF;  -border za footer */
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
  font-size: 60px;
  margin-bottom: 0px;
}

.document{
    width: 250px;
    height: 300px;
    display:block;
    background-color:white;
    margin-top: 0px;
    margin-left: 22.5px;
    margin-bottom: 25px;
    display: block; 
    float: left;
    border: 2px solid  #707070;
    
}

.documentName{
    background-color: white;
    height: 15%;
    line-height: 50px;
    font-size: 25px;
}

.documentPicDiv{
    background-color: white;
    height: 75%;
}

.documentDate{
    height: 10%;
    background-color: white;
    font-size: 17.5px;
}

.fa-folder, .fa-folder-plus{
  text-shadow: 0 0 10px #00A2FF;
  color: #888888; 
  font-size: 200px; 
}

.fa-folder-plus{
  background: linear-gradient(to bottom, #EEEEEE, #EEEEEE 33.33%, #00A2FF 33.33%, #00A2FF 80%, #EEEEEE 20%); 
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
  color:#00a2ff;
  margin-left: -20px;
}   

.fa-file{
  width:20%;
  color:#00a2ff;
  background-color: white;
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


.wide{
  margin-left: 0px;
  margin-left: 0px;
}

#backButton{
  border-radius: 5px;  
  float:left; 
  background-color: #00A2FF; 
  color:white; 
}

#deleteButton{
   border-radius: 5px; 
   float:right; 
   background-color:#FF0000; 
   border:0px;
}


/* settings dropdown */

#settingsIcon{
  display:inline-block; 
  position: absolute; 
  left: 3px; 
  top: 4px;
}

#archiveName > h2 {
  text-align:center; 
  color: #00A2FF; 
  position:relative;
}

#archiveName {
  height: 50px; 
  position: relative;
  text-align: center; 
  padding-top: 5px; 
  padding-bottom: 5px;
}

.userData{
  display: flex;
}

.changeName{
  display:inline-block; 
  color:#888888; 
}

.editIcon{
  background-color: #00A2FF; 
  display:inline-block; 
  border-radius:3px; 
  margin: 2.5px;
}

.fa-edit{
  color:white; 
  padding: 2.5px;
}

#changeNameHeader{
  border-bottom: 2px solid #BEBEBE;
} 

.body-settings{
  padding-right:50px; 
  padding-left:50px;
}

#pristupNaslov {
  text-align: center;
}

#pristupNaslovHeader{
  line-height:30px;
}

#dropdownHeaderHeadline{
  height:45px;
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
}

#addButtonSettings{
  margin: 5px; 
  border-radius:5px; 
  border:0;
}

#removeButtonSettings{
  margin: 5px; 
  border-radius:5px; 
  border:0;
  background-color: #888888;
}

.addUserButton{
  color: #23CA00;
}

.addUserName{
  color: #888888;
  
  text-decoration: underline;
}

/*
.dropdownFooter{
  height: 70px !important;
}
*/

/* dropdown filter*/
.filter{
  width: 30px;
  height: 30px;
  background-color: white;
  margin : 10px 5px  10px 5px; 
  float: right;
  border-radius: 5px;
  border: 2px solid  #00A2FF;
  padding-top: 4px;
  color:#00A2FF;
  
}

.filterOptions{
  margin: 0 5px 5px 5px;
  width: 410px;
  
}

.filterOptions > label{
  width:40%;
}

.filterOptions > input > text{
  width:40%;
}


.filterOptions > input{
  color: black;
  border-radius: 5px;
  border: 2px solid #888888;
  padding-left: 5px;
  padding-right: 5px;
}

.filterOptions > input > checkbox {
  width:40%;
  color:blue;
  background-color: pink;
}

@keyframes glow {
  80%, 100% {
      text-shadow: 0 0 5px #00A2FF;
  }
}

.glowEffect {
  animation: glow 2s 5;
  overflow-x: hidden;
  overflow-y: hidden;
  opacity: 1; 
}


.btn-group{
  display:block;
}


.btn-group>.btn:first-child {
  margin-left: 5px;
  border-radius: 5px;
}

h2::before{
  content: '';
  display: block;
  position: absolute;
  bottom: 0;
  width: 70%;
  left: 15%;
  border-top: 2px solid #707070;
  /* order-bottom: 2px solid  #707070; i bez before-a za full bottom border */

}


.dropdown-menu{
  border: 2px solid  #00A2FF;
}

.dropdownHeader > h2 {
  text-align:center; 
  color: #00A2FF; 
  position:relative;
}

.dropdownHeader {
  height: 50px; 
  position: relative;
}



#filterIcon{
  display:inline-block; 
  position: absolute; 
  left: 3px; 
  top: 4px;
}

#addButtonFilter{
  margin: 5px; 
  border-radius:5px; 
  border:0;
}

#removeButtonFilter{
  margin: 5px; 
  border-radius:5px; 
  border:0;
  background-color: #888888;
}

.addButtonDiv{
display: flex; 
align-items: center; 
justify-content: center; 
height: 60px; 
}


@media screen and (min-width: 1024px){
 .archive-options{
  background-color:  blue;
  
  }  
}

/*###Tablet(medium)###*/
@media screen and (min-width : 768px) and (max-width : 1023px){
/*Style*/
}

/*### Smartphones (portrait and landscape)(small)### */
@media screen and (min-width : 0px) and (max-width : 767px){
  .archive{
  height: 3000px;
}

.archive-options{
  background-color:  white ; /* blue */
  
  } 

.subArchive{
  width:120px;
  height: 140px;
  margin-top:25px;
  margin-left: 25px;
  margin-right: 10px;
  display: inline-block; 
 }

 .search{
  width: 135px;
}

.chooseArchive{
  width: 120px;
 }

#archiveSelector{
  background-color: white;
}

#searchIcon{
  	padding-left: 3px;
}


#backButton, #deleteButton {
  display:none;
}

.headlineDiv{
  display:inline-block;
}

.document{
  margin-left: 40px;
}

}
</style>
