<template>
  <div class="home">
    <notifications group="notify" />
      <div class="container">
        <div class="row">

            <div class="col archive-options">       
                  <!-- settings dropdown -->
                  <div class="btn-group" >
                      <!--
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
                                <input v-model="naziv_arhive" id="changeNameHeader" style="color:#2c3e50;"/> 
                              </div>
                          </div>
                        
                          <div class="dropdownBody body-settings" >                       
                              <div id="pristupNaslov">
                                <h6 id="pristupNaslovHeader"><b>Osobe sa pristupom</b></h6>
                              </div>
                              <div>  

                                <userData v-bind:key="card.id" v-bind:info="card" v-for="card in user.email_list" />

                                <div class="userData "  >
                                    <div class="personIcon"><i class="far fa-user"></i> </div>
                                    <input v-model="shared_email" class="mailOsobe addUserName"  /> 
                                    <button v-on:click ="share_arc()" class="opcijaPopis addUserButton">dodaj</button>  
                                </div>
                              
                              </div>
                            </div>
                          
                          <div class="dropdownFooter addButtonDiv">
                            <button v-if="this.check_if_owner_of_archive" type="submit" @click="changeArchiveName()" class="btn btn-primary my-2 my-sm-0" id="saveButtonSettings" > Spremi</button>
                            <button @click="closeShareDropDown()" type="submit" class="btn btn-primary my-2 my-sm-0" id="closeShareDropdownButton" > Zatvori</button>
                          </div>
                      </div>
                    -->
                  </div>

                  
                  <!-- choose Archive (Dropdown umjesto selecta zbog veće mogućnosti customizacije -- prebaciti css u css--                  
                  <div class="chooseArchive">
                      <i class="far fa-file fa-lg" ></i>
                      <select id="archiveSelector">
                          <option value="Archive_1">Internet</option>
                          <option value="Archive_2">Struja</option>
                          <option value="Archive_3">Voda</option>
                          <option value="Archive_4">Ostalo</option>
                        </select>
                  </div>
                  -->
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
                                <input type="radio" class="custom-control-input" id="datDodavanjaVeciOd" name="selectedFilter" checked>
                                <label for="datDodavanjaVeciOd" class="custom-control-label">Datum dodavanja veći od:</label>
                                <input v-model ="filter_params.datum_dodavanja__greater" type="text" id="datDodavanjaVeciOd" name="selectedFilter"><br>
                              </div>
                              <div class="filterOptions custom-control custom-checkbox " >
                                <input type="radio" class="custom-control-input" id="datDodavanjaManjiOd" name="selectedFilter">
                                <label for="datDodavanjaManjiOd" class="custom-control-label">Datum dodavanja manji od:</label>
                                <input v-model ="filter_params.datum_dodavanja__lesser" type="text" id="datDodavanjaManjiOd" name="selectedFilter"><br>
                              </div>
                              <div class="filterOptions custom-control custom-checkbox ">
                                <input type="radio" class="custom-control-input" id="datIzdavanjaVeciOd" name="selectedFilter">
                                <label for="datIzdavanjaVeciOd" class="custom-control-label">Datum izdavanja veći od:</label>
                                <input v-model ="filter_params.datum_izdavanja__greater" type="text" id="datIzdavanjaVeciOd" name="selectedFilter"><br>
                              </div>
                              <div class="filterOptions custom-control custom-checkbox ">
                                <input type="radio" class="custom-control-input" id="datIzdavanjaManjiOd" name="selectedFilter">
                                <label for="datIzdavanjaManjiOd" class="custom-control-label">Datum izdavanja manji od:</label>
                                <input v-model ="filter_params.datum_izdavanja__lesser" type="text" id="datIzdavanjaManjiOd" name="selectedFilter"><br>
                              </div>
                              <div class="filterOptions custom-control custom-checkbox ">
                                <input type="radio" class="custom-control-input" id="datDospijecaVeciOd" name="selectedFilter">
                                <label for="datDospijecaVeciOd" class="custom-control-label">Datum dospijeća veći od:</label>
                                <input v-model ="filter_params.datum_dospijeca__greater" type="text" id="datDospijecaVeciOd" name="selectedFilter"><br>
                              </div>
                              <div class="filterOptions custom-control custom-checkbox ">
                                <input type="radio" class="custom-control-input" id="datDospijecaManjiOd" name="selectedFilter">
                                <label for="datDospijecaManjiOd" class="custom-control-label">Datum dospijeća manji od:</label>
                                <input v-model ="filter_params.datum_dospijeca__lesser" type="text" id="datDospijecaManjiOd" name="selectedFilter"><br>
                              </div>
                              <div class="filterOptions custom-control custom-checkbox ">
                                <input type="radio" class="custom-control-input" id="nazDobavljaca" name="selectedFilter">
                                <label for="nazDobavljaca" class="custom-control-label" >Naziv dobavljača:</label>
                                <input v-model ="filter_params.naziv_dobavljaca__is" type="text" id="nazDobavljaca" name="selectedFilter"><br>
                              </div>
                              <div class="filterOptions custom-control custom-checkbox">
                                <input type="radio" class="custom-control-input" id="vrstaUsluge" name="selectedFilter">
                                <label for="vrstaUsluge" class="custom-control-label">Vrsta usluge:</label>
                                <input v-model ="filter_params.vrsta_usluge__is" type="text" id="vrstaUsluge" name="selectedFilter"><br>
                              </div>
                               <div class="filterOptions custom-control custom-checkbox ">
                                <input type="radio" class="custom-control-input" id="iznosVeciOd" name="selectedFilter">
                                <label for="iznosVeciOd" class="custom-control-label">Iznos veći od:</label>
                                <input v-model ="filter_params.iznos__greater" type="number" id="iznosVeciOd" name="selectedFilter"><br>
                              </div>                    
                              <div class="filterOptions custom-control custom-checkbox ">
                                <input type="radio" class="custom-control-input" id="iznosManjiOd" name="selectedFilter">
                                <label for="iznosManjiOd" class="custom-control-label">Iznos manji od:</label>
                                <input v-model ="filter_params.iznos__lesser" type="number" id="iznosManjiOd" name="selectedFilter"><br>
                              </div>
                            
                          </div>
                          <div class="addButtonDiv">
                                <button v-on:click = "filter_documents" type="submit" class="btn btn-primary my-2 my-sm-0" id="addButtonFilter"> Traži </button>
                                <button v-on:click = "clear_filter" type="submit" class="btn btn-primary my-2 my-sm-0" id="removeButtonFilter"> Očisti filter</button>
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
                  <div style="width: 100%;" id="headlineDiv"><h1 id="headline">{{this.naziv}}</h1></div>
                  <button v-if="this.check_if_owner_of_archive" type="button" class="btn btn-primary my-2 my-sm-0" id="deleteButton"  data-toggle="modal" data-target="#delete_confirmation">Izbriši</button>
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
                        <div v-on:click="delete_archive" data-dismiss="modal" style="font-size:20px; color:#707070">Ok</div>
                    </div>
                
                  </div>
              </div>
            </div>

            <!-- add user success confirmation -->
            <div class="modal fade" id="adding_user_success_confirmation" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
              <div class="modal-dialog modal-dialog-centered" role="document" >
                
                <div class="modal-content" style="solid; text-align: center; border-radius: 7.5px; ">
                    <div class="modal-body" style="font-size: 30px; color:#00A2FF;">
                        Pristup dozvoljen
                        <hr/>
                        <div data-dismiss="modal" style="font-size:20px; color:#707070">Ok</div>
                    </div>
                </div>

              </div>
            </div>

            <!-- error confirmation during adding user to archive -->
            <div class="modal fade" id="unsuccess_confirmation_adding_user" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
              <div class="modal-dialog modal-dialog-centered" role="document" >
                
                <div class="modal-content" style="solid; text-align: center; border-radius: 7.5px; ">
                    <div class="modal-body" style="font-size: 30px; color:#00A2FF;">
                        Došlo je do pogreške. Provjerite da li ste unijeli ispravan mail.
                        <hr/>
                        <div data-dismiss="modal" style="font-size:20px; color:#707070">Ok</div>
                    </div>
                  </div>

              </div>
            </div>

        <div class="row">
            <div class="col archive">
              <Document v-bind:key="card.id" v-bind:info="card" v-for="card in documentData" /> 
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
import { Auth } from "@/services";
import _ from "lodash";
import toastr from "toastr"

export default {
  data(){
    return {
      user: Auth.getUser(),
      documentData: '',
      naziv: this.$route.params.naziv_arhive,  //naziv_arhive -> varijabla u /router/index.js
      searchTerm: '',
      tempDoc: '',
      naziv_arhive: 'Moja_arhiva',
      shared_email: '',
      store,

      alias_email: null, //da ne baca error
      filter_params: {}
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

    clear_filter(){
      this.filter_params = {}
      this.extract_documents()
    },

    filter_documents(){
      this.extract_documents()
      let filtered_docs = this.documentData
      
      for(let i = 0; i < Object.keys(this.filter_params).length; i++){
        let key_ = Object.keys(this.filter_params)[i]
        let value = this.filter_params[key_]
        
        let [key, comparison] = key_.split("__")

        if(comparison == 'is'){
          filtered_docs = filtered_docs.filter((doc) => doc[key] == value)
        }
        else if(comparison == 'greater'){
          filtered_docs = filtered_docs.filter((doc) => doc[key] > value)
        }
        else if(comparison == 'lesser'){
          filtered_docs = filtered_docs.filter((doc) => doc[key] < value)
        }
      }

      this.documentData = filtered_docs
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

    async delete_archive(){
      let subarchive_id = ''
      for(let i = 0; i < this.store.currentArchiveData.subarchives.length; i++){
        if(this.store.currentArchiveData.subarchives[i].name == this.naziv){
          subarchive_id = this.store.currentArchiveData.subarchives[i].subarchive_id
          await app.deleteSubarchive(this.user.personal_archive_id,subarchive_id)
        }
      }
      let archives = await app.getArchives(this.user.email,this.user.archive_ids)
      localStorage.setItem('userArchives',JSON.stringify(archives))
      this.store.updateCurrentUserArchive(archives)
      this.store.documentData = ''
      this.$router.push({ name: 'Home' })
    },

    extract_documents(){
      let subarchives = this.store.currentArchiveData.subarchives

      subarchives.forEach((subarc) => {
        if(subarc.name == this.naziv) this.documentData = subarc.documents
      }) 
    },

    addingUserConfirmation(success){
      if(success) $("#adding_user_success_confirmation").modal()

      else $("#unsuccess_confirmation_adding_user").modal()
    },

    closeShareDropDown(){
      $('#closeShareDropdownButton').trigger("click");
    },

    async share_arc() {
      if(this.shared_email != ''){
        let success = false
        let result = await app.share_archive(this.user.email,this.shared_email)
        if(result){
          this.user.archive_ids.push(result[0])
          this.user.email_list.push(result[1])
          localStorage.setItem("user",JSON.stringify(this.user))
          let archives = await app.getArchives(this.user.email,this.user.archive_ids)
          localStorage.setItem('userArchives',JSON.stringify(archives))
          success = true
        }
        this.shared_email = ''
        this.addingUserConfirmation(success);
      }
    },

    async searchArchives(pretraga){
      pretraga = this.searchTerm
      let archives = await app.getSearchArchives(pretraga, this.user.archive_ids,this.store.currentArchiveData._id)
      localStorage.setItem('userArchives',JSON.stringify(archives))
      this.store.updateCurrentUserArchive(archives)
    },

    async changeArchiveName(){
      await app.changeArchiveName(this.store.currentArchiveData._id,this.store.currentArchiveData.name)
      let archives = await app.getArchives(this.user.email,this.user.archive_ids)
      localStorage.setItem('userArchives',JSON.stringify(archives))
      $('#closeShareDropdownButton').trigger("click");
    },

    async closeSortDropdown(){
      let sortby = ''
      if(document.getElementById("defaultInline1").checked) sortby = 'datum_pregleda_silazno'
      else if(document.getElementById("defaultInline2").checked) sortby = 'abecedno_silazno'
      else if(document.getElementById("defaultInline3").checked) sortby = 'datum_pregleda_uzlazno'
      else if(document.getElementById("defaultInline4").checked) sortby = 'abecedno_uzlazno'
      let archives = await app.sort_Archives(sortby,this.user.archive_ids,this.store.currentArchiveData._id)
      localStorage.setItem('userArchives',JSON.stringify(archives))
      this.store.updateCurrentUserArchive(archives)
      $('#SortDropDown').trigger("click"); //https://stackoverflow.com/questions/10941540/how-to-hide-twitter-bootstrap-dropdown
    },

    addingUserConfirmation(success){
      if(success) 
        $("#adding_user_success_confirmation").modal()
      else 
        $("#unsuccess_confirmation_adding_user").modal()
    },


  },

  computed:{
    check_if_owner_of_archive(){
      if(this.store.currentArchiveData._id == this.user.personal_archive_id) return true
      else return false
    }
  },

  async mounted() {

    if(this.store.currentArchiveData == ''){
      let archives = JSON.parse(localStorage.getItem('userArchives'))
      this.store.updateCurrentUserArchive(archives)
    }

    //Ispis dokumenata podarhive
    this.extract_documents()
    if(this.documentData == '') console.log("Korisnik nema dokumenta")
    
    //Update examination date
    for(let i = 0; i < this.store.currentArchiveData.subarchives.length; i++){
      if(this.store.currentArchiveData.subarchives[i].name == this.naziv){
        let subarchive_name = this.store.currentArchiveData.subarchives[i].name
        await app.update_exDate(this.store.currentArchiveData._id, subarchive_name)
      }
    }


    //https://www.npmjs.com/package/vue-notification
    this.$notify({
        group: 'notify',
        type: 'info',
        title: 'Ne možete pronaći dokument?',
        text: 'Isprobajte naš filter!',
        duration: 7000,
        position:'top right'
    });
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

#changeNameHeader{
  font-size:20px;
  height: 30px;
  border:none;
  width:150px;
  text-align:center;
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
  background:white; 
  border-left:none; 
  border-top:none; 
  border-right:none;
}

.opcijaPopis{
  display:inline-block; 
  color:#FF0000; 
  width: 75px;
  text-align: center;
  border:none;
  background:white;
}

#addButtonSettings, #createArchiveButton{
  margin: 5px; 
  border-radius:5px; 
  border:0; 
}

#removeButtonSettings, #closeButtonArchive{
  margin: 5px; 
  border-radius:5px; 
  border:0;
  background-color:#888888;
}

#saveButtonSettings{
  background-color:#00a2ff;
  margin:2.5px;
  border:none;
}

#closeShareDropdownButton{
  background-color: #888888;
  margin:2.5px;
  border:none;
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
  
  
}

.filterOptions > label{
  width:50%;
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
  margin-left: 2px;
  width:45%;
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
