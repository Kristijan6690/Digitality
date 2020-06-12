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
                              <div>  

                                <UserData />
                                <UserData />
                                <UserData />

                                <div class="userData "  >
                                     <div class="personIcon"><i class="far fa-user"></i> </div>
                                     <input v-model="alias_email" class="mailOsobe addUserName"  /> 
                                     <button v-on:click ="add_access()" class="opcijaPopis addUserButton">Dodaj</button>  
                                </div>
                              
                              </div>
                            </div>
                          <div class="dropdownFooter addButtonDiv">
                                <button type="submit" class="btn btn-primary my-2 my-sm-0" id="addButtonSettings" > Spremi </button>
                                <button type="submit" @click="closeSortDropdown" class="btn btn-primary my-2 my-sm-0" id="removeButtonSettings" > Poništi</button>
                          </div>
                      </div>
                    </div>

                    <!-- choose Archive (Dropdown umjesto selecta zbog veće mogućnosti customizacije -- prebaciti css u css--> 
                     <div class="btn-group  dropdown" >
                       
                       <button class="btn btn-light dropdown-toggle chooseArchive" type="button" id="dropdownMenuArchive" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" >
                        <div id="fileIconDiv"><i class="far fa-file fa-lg" ></i></div>
                        <div id="currArchiveName"> {{store.currentArchiveData.name}} </div>
                      </button>
                      <div class="dropdown-menu dropdown-menu-left menu-settings">
                          <div class="dropdownHeader"  @click.stop=''> 
                              <h2 id="chooseArchiveHeader"> Odaberite arhivu </h2> 
                          </div>
                  
                          <div class="dropdownBody body-settings" id="chooseArchiveBody">                       
                            
                              <div id="pristupPopis">  
                               <form id="archiveForm" name="archiveForm">
                                <div class="filterOptions custom-control custom-radio " >
                                  <input  v-model="currentArchive" checked="checked" type="radio" class="custom-control-input" id="Arhiva_1" name="Archive" value="Arhiva_1">
                                  <label for="Arhiva_1" class="custom-control-label">Arhiva_1</label>
                                </div>
                                <div class="filterOptions custom-control custom-radio " >
                                  <input  v-model="currentArchive" type="radio" class="custom-control-input" id="Arhiva_2" name="Archive" value="Arhiva_2">
                                  <label for="Arhiva_2" class="custom-control-label">Arhiva_2</label>
                                </div>
                                <div class="filterOptions custom-control custom-radio " >
                                  <input v-model="currentArchive"  type="radio" class="custom-control-input" id="Arhiva_3" name="Archive" value="Arhiva_3">
                                  <label for="Arhiva_3" class="custom-control-label">Arhiva_3</label>
                                </div>
                                <div class="filterOptions custom-control custom-radio " >
                                  <input v-model="currentArchive" type="radio" class="custom-control-input" id="Arhiva_4" name="Archive" value="Arhiva_4">
                                  <label for="Arhiva_4" class="custom-control-label">Arhiva_4</label>
                                </div>
                                <div class="filterOptions custom-control custom-radio " >
                                  <input v-model="currentArchive" type="radio" class="custom-control-input" id="Arhiva_5" name="Archive" value="Arhiva_5">
                                  <label for="Arhiva_5" class="custom-control-label">Arhiva_5_Dugi_Naziv</label>
                                </div>
                               </form>
                              </div>
                            </div>
                          <div class="dropdownFooter addButtonDiv"  @click.stop=''>
                                <button type="submit" class="btn btn-primary my-2 my-sm-0" id="changeArchiveButton"> Dodaj </button>
                                <button type="submit" class="btn btn-primary my-2 my-sm-0"  @click="closeSortDropdown" id="closeButtonArchive"> Poništi</button>
                          </div>
                      </div>
                    </div>
            
                       <!-- sort dropdown prebaciti css u css i popraviti nazive-->
                      <div id ="SortDropDown" class="btn-group" >
                        <button type="button" class="btn btn-secondary sort" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" >
                          <div id="sortIcon" ><i class="fas fa-sort-amount-down fa-lg"></i></div>
                        </button>

                        <div class="dropdown-menu dropdown-menu-right" @click.stop=''>
                          <div class="dropdownHeader" >
                              <h2 style="height:42px;">Organiziraj arhivu</h2> 
                          </div>

                          <div class="dropdownBody" id="sortArchiveBody">              
                            <div style="margin: 0 10px 0 10px">         
                                <!-- Default inline 1 bootstrap-->
                              <div class="custom-control custom-checkbox custom-control-inline">
                                <input type="radio" name="check" class="custom-control-input" id="defaultInline1" >
                                <label class="custom-control-label" for="defaultInline1" style="padding-right:5px;">
                                  Datum pregleda silazno 
                                  <i class="fas fa-sort-amount-down"></i>       
                                </label>  
                              </div>

                              <!-- Default inline 2-->
                              <div class="custom-control custom-checkbox custom-control-inline" id="defaultInline2Div" >
                                <input type="radio" name="check" class="custom-control-input" id="defaultInline2">
                                <label class="custom-control-label" for="defaultInline2" style="padding-right:5px;">
                                  Abecedno silazno
                                  <i class="fas fa-sort-amount-up"></i>    
                                </label>       
                              </div>
                            </div>
                             
                            <div style="margin: 0 10px 0 10px">    
                              <!-- Default inline 3-->
                              <div class="custom-control custom-checkbox custom-control-inline">
                                <input type="radio" name="check" class="custom-control-input" id="defaultInline3">
                                <label class="custom-control-label" for="defaultInline3" style="padding-right:5px;">
                                  Datum pregleda uzlazno
                                  <i class="fas fa-sort-numeric-down-alt"></i>
                                </label>
                               
                              </div>
                              <!-- Default inline 4-->
                              <div class="custom-control custom-checkbox custom-control-inline"> 
                                <input type="radio" name="check" class="custom-control-input" id="defaultInline4" checked>
                                <label class="custom-control-label" for="defaultInline4" style="padding-right:5px;">
                                  Abecedno uzlazno
                                  <i class="fas fa-sort-numeric-up-alt"></i>
                                </label>         
                              </div>
                            </div>
                                                   
                          </div>
                          <div class="addButtonDiv">
                                <button type="submit" @click="closeSortDropdown()" class="btn btn-primary my-2 my-sm-0" id="sortButton"> Potvrdi </button>
                          </div>
                      </div>
                     </div>
                    

                  <form class="search">
                      <input v-model = "searchTerm" id="searchBar" type="search" placeholder="Traži..."/>
                      <i class="fas fa-search fa-lg" id="searchIcon"></i>
                  </form>
                  
            </div>         
        </div>

        <div class="row">
          <div class="col archive">
            <SubArchiveCard v-bind:key="card.id" v-bind:info="card" v-for="card in store.currentArchiveData.subarchives" />

            <div class="subArchivePlus" data-toggle="modal" data-target="#helpModal" style="border:none;">
                <div class="folder"><i class="fas fa-folder-plus fa-7x" ></i></div>
                <div class="folderName">Dodaj podarhivu</div>
          </div>
        </div>


        <!-- Modal za kreiranje arhive -->
          <div class="modal fade" id="helpModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered" role="document">
              <div class="modal-content">
                <div class="modal-header" style="display:block;">
                  <h3 class="'col-12 modal-title text-center'" id="exampleModalLongTitle" style="color:#000000;">Kreiraj podarhivu</h3>
                </div>
                <div class="modal-body">
                  <input v-model = "createArchiveName" placeholder="Unesite ime podarhive" onfocus="this.placeholder = ''" onblur="this.placeholder = 'Unesite ime podarhive'" style="border:none; color:#00A2FF; padding: 0 10px 0 10px; text-align:center;" />
                </div>
                <div class="modal-footer" style="text-align:center; display:block;">
                  <button v-on:click="create_archive()" type="button" class="btn btn-secondary" data-toggle="modal" data-dismiss="modal" style="background-color:#00A2FF">Dodaj</button>
                  <button v-on:click="add_archive_cancel()" type="button" class="btn btn-secondary"  data-dismiss="modal" style="background-color:#00A2FF">Odustani</button>
                </div>
              </div>
            </div>
          </div>

          <!-- Modal za popunjavanje podataka koji nedostaju -->
          <div class="modal fade" id="formModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered" role="document">
              <div class="modal-content">
                <div class="modal-header" style="display:block;">
                  <h3 class="'col-12 modal-title text-center'" id="exampleModalLongTitle" style="color:#000000;">Dodatni podaci</h3>
                </div>
                <div class="modal-body">
                  <small id="emailHelp" class="form-text text-muted" style="margin-bottom:10px;">
                    Poštovani, kako bi naš sustav radio pravilno, molimo Vas da popunite sljedeće podatke:
                  </small>
                  <form>
                    <div class="form-group">
                      <input type="text" class="form-control" placeholder="OIB">
                    </div>
                     <div class="form-group">
                      <input type="text" class="form-control" placeholder="IBAN">
                    </div>
                     <div class="form-group">
                      <input type="text" class="form-control" placeholder="Poštanski broj">
                    </div>
                                 
                  </form>
                </div>
                <div class="modal-footer" style="text-align:center; display:block;">
                  <button type="button" class="btn btn-secondary" data-toggle="modal" data-dismiss="modal" style="background-color:#00A2FF">Dodaj</button>
                  <button type="button" class="btn btn-secondary"  data-dismiss="modal" style="background-color:red">Odustani</button>
                </div>
              </div>
            </div>
          </div>

        <!-- success confirmation -->
      <div class="modal fade" id="success_confirmation" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document" >
          
          <div class="modal-content" style="solid; text-align: center; border-radius: 7.5px; ">
              <div class="modal-body" style="font-size: 30px; color:#00A2FF;">
                   Arhiva uspješno kreirana
                  <hr/>
                  <div data-dismiss="modal" style="font-size:20px; color:#707070">Ok</div>
              </div>
          </div>

        </div>
      </div>

      <!-- error confirmation -->
      <div class="modal fade" id="unsuccess_confirmation" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document" >
          
          <div class="modal-content" style="solid; text-align: center; border-radius: 7.5px; ">
              <div class="modal-body" style="font-size: 30px; color:#00A2FF;">
                   Došlo je do pogreške,arhiva već postoji
                  <hr/>
                  <div data-dismiss="modal" style="font-size:20px; color:#707070">Ok</div>
              </div>
            </div>

        </div>
      </div>

        </div>

        <button type="button" class="btn btn-secondary"  data-dismiss="modal" data-toggle="modal" data-target="#formModal" >Testni gumb da se pokrene modal</button>
        <!-- footer
        <div class="row">
            <div class="col archive"></div>
        </div>
        -->
      </div>

  </div>
</template>
<!-- popraviti : logo na title kartici,mobile dva subarchiva u jednom redu,settings email overflow, search bottom padding elip, effecti elips, header vise nalik prototipu?, da dugi nazivi neidu izvan, poredak elemenata, mobile responsive, footer? active navbar, bolji način za pozicioniranje filter ikone-->
<script>

import SubArchiveCard from '@/components/SubArchiveCard.vue';
import UserData from '@/components/UserData.vue';
import { app } from "@/services";
import { Auth } from "@/services";
import store from "@/store.js";
import _ from "lodash";

export default {
  data(){
    return {
      user: Auth.getUser(),
      searchTerm: '',
      store,
      createArchiveName: '',
      currentArchive: '',
      alias_email: ''
    }
  },

  name: 'Home',
  components: {
    SubArchiveCard,
    UserData
  },

  watch: {
    "searchTerm": _.debounce(function(val) {
      this.searchArchives(val);
    }, 500)
  },
  
  methods:{
    async searchArchives(pretraga){
      pretraga = this.searchTerm
      let archives = await app.getSearchArchives(pretraga, this.user.archive_ids,this.store.currentArchiveData._id)
      localStorage.setItem('userArchives',JSON.stringify(archives))
      this.store.currentArchiveData = this.store.get_users_arhive(archives,this.user.archive_ids) 
    },

    async create_archive() {
      let flag = false

      if(this.createArchiveName != '') {
        this.createArchiveName = this.createArchiveName.toLowerCase()
        for(let i = 0; i < this.store.currentArchiveData.subarchives.length; i++){
          if(this.createArchiveName == this.store.currentArchiveData.subarchives[i].name.toLowerCase()){
            flag = true
          }
        }
        if(flag) {
          this.createArchiveName = ''
          $("#unsuccess_confirmation").modal() //https://www.w3schools.com/bootstrap/bootstrap_ref_js_modal.asp?fbclid=IwAR1ptJTxChvevYy03LanxDkM-lggA5XAq1gSSXntekFr1UOBEyW0TOl1vJk
        }
        else {
          await app.createSubarchive(this.createArchiveName, this.user.personal_archive_id)
          let archives = await app.getArchives(this.user.email,this.user.archive_ids)
          localStorage.setItem('userArchives',JSON.stringify(archives))
          this.store.currentArchiveData = this.store.get_users_arhive(archives,this.user.archive_ids)
          this.createArchiveName = ''
          $("#success_confirmation").modal() //https://www.w3schools.com/bootstrap/bootstrap_ref_js_modal.asp?fbclid=IwAR1ptJTxChvevYy03LanxDkM-lggA5XAq1gSSXntekFr1UOBEyW0TOl1vJk
        }
      }
    },

    add_archive_cancel() {
      this.createArchiveName = ''
    },
  
    async closeSortDropdown(){
      let sortby = ''
      if(document.getElementById("defaultInline1").checked) sortby = 'datum_pregleda_silazno'
      else if(document.getElementById("defaultInline2").checked) sortby = 'abecedno_silazno'
      else if(document.getElementById("defaultInline3").checked) sortby = 'datum_pregleda_uzlazno'
      else if(document.getElementById("defaultInline4").checked) sortby = 'abecedno_uzlazno'
      let archives = await app.sort_Archives(sortby,this.user.archive_ids,this.store.currentArchiveData._id)
      localStorage.setItem('userArchives',JSON.stringify(archives))
      this.store.currentArchiveData = this.store.get_users_arhive(archives,this.user.archive_ids)
      $('#SortDropDown').trigger("click"); //https://stackoverflow.com/questions/10941540/how-to-hide-twitter-bootstrap-dropdown
    },

    async add_access() {
      let alias = await app.add_alias(this.alias_email,this.user.email)
      if(alias){
        this.user.alias_list.push(alias[0])
        this.user.archive_ids.push(alias[1])
        localStorage.setItem("user",JSON.stringify(this.user))
        let archives = await app.getArchives(this.user.email,this.user.archive_ids)
        localStorage.setItem('userArchives',JSON.stringify(archives))
        this.store.currentArchiveData = this.store.get_users_arhive(archives,this.user.archive_ids)
        console.log("Uspijeh")
      } else console.log("Greska")
    },
  },

  async mounted(){
    let temp = JSON.parse(localStorage.getItem('userArchives'))
    this.store.currentArchiveData = this.store.get_users_arhive(temp,this.user.archive_ids)
  }
}


</script>

<style scoped>


/* home menu */
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
  height: 600px;
  float:left;
  /*border-radius: 10px;  -> varijanta za white archive options*/
  padding-left:15px;  /* varijanta bez paddinga? */
  padding-right:15px;
  /* border-bottom: 2px solid  #00A2FF;  -border za footer */
}

/* archive folders */
.subArchivePlus{
  width:120px;
  height: 140px;
  margin-top:25px;
  margin-left: 50px;
  margin-right: 10px;
  display: block; 
  float: left;
  /* varijanta manji razmak i centrirane
  margin-left: 10px;
  margin-right: 10px;
  display: inline-block; */
}

.folder{
  width:120px;
  height: 100px;
  background-color: #EEEEEE;
  
}

.folderName{
  width: 120x;
  height: 20px;
  background-color: #EEEEEE;
  text-overflow: ellipsis; 
  overflow: hidden; 
  white-space: nowrap;white-space: nowrap;
}

.fa-folder-plus{
  text-shadow: 0 0 10px #00A2FF;
  color: #888888;  
}

.fa-folder-plus{
  background: linear-gradient(to bottom, #EEEEEE, #EEEEEE 33.33%, #00A2FF 33.33%, #00A2FF 80%, #EEEEEE 20%); 
}

a{
  color: #2c3e50; 
}

/* choose archive dropdown */
.chooseArchive{
  width: 150px;
  height: 30px;
  background-color: white;
  display: block;
  margin: 10px 0 10px 0;
  float: left;
  border-radius: 5px;
  border: 2px solid  #00A2FF;
  padding: 3px;
  color: #00A2FF; 
  margin-left:0px; 
  text-align:left;
  /*vertical-align:top;*/
}

#fileIconDiv{
  display:inline-block; 
  padding: 0px 5px; 
  width:20%; 
  vertical-align: top;
}

#currArchiveName{
  display:inline-block; 
  padding: 0px 10px; 
  width:70%; 
  overflow:hidden; 
  text-overflow: ellipsis;  
  vertical-align: top;
}

#chooseArchiveBody{
  border: solid 1px #D3D3D3; 
  margin: 0px 40px 0 40px; 
  padding: 0 0 0 0;
}

#pristupPopis{
  padding: 5px 5px 30px 5px;
}

#archiveSelection > h2 {
  text-align:center; 
  color: #00A2FF; 
  position:relative;
}

#archiveSelection {
  height: 50px; 
  position: relative;
}


/* settings dropdown */
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

#addButtonSettings, #changeArchiveButton{
  margin: 5px; 
  border-radius:5px; 
  border:0; 
}

#removeButtonSettings, #closeButtonArchive{
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

.fa-cog{
  color:#00a2ff;
}

/*
.dropdownFooter{
  height: 70px !important;
}
*/

/* dropdown filter*/
.sort{
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

.sortOptions{
  margin: 0 5px 5px 5px;
  width: 410px;
  
}

.sortOptions > label{
  width:40%;
  padding-right: 5px;
}

.sortOptions > input > text{
  width:40%;
}


.sortOptions > input{
  color: black;
  border-radius: 5px;
  border: 2px solid #888888;
  padding-left: 5px;
  padding-right: 5px;
}

.sortOptions > input > checkbox {
  width:40%;
  color:blue;
  background-color: pink;
}

#defaultInline2Div{
  margin-left: 5px;
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

#chooseArchiveHeader{
  font-size: 1.5rem; 
  margin:5px 20px 0 20px; 
  height:35px;
}

#chooseArchiveHeader::before {
  left: 5%;
  width: 90%;
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

#sortIcon{
  display:inline-block; 
  position: absolute; 
  left: 3px; 
  top: 4px;
}

#sortButton{
  margin: 5px; 
  border-radius:5px; 
  border:0;
}

.addButtonDiv{
display: flex; 
align-items: center; 
justify-content: center; 
height: 60px; 
}

/*     */

/* search bar */
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

#searchBar{
  width: 80%;
  height: 100%;
  color:#00a2ff;
  outline: none;
  border: 0px;
  padding-right: 2px;
  padding-left: 2px;
}

#searchIcon{ 
  color:#00A2FF;
  padding-left: 7.5px;
}

 ::placeholder {
  color:#00a2ff;
  margin-left: -20px;
}   

.form-group > ::placeholder {
  color: #2c3e50; 
  margin-left: -20px;
}  

.fa-file{
  width:10%;
  color:#00a2ff;
  background-color: white;
}

/*
#archiveSelector{
  width: 80%;
  height: 100%;
  color:#00a2ff;
  border: 0px;
  outline: none;
  border: 0px;
}
*/


@media screen and (min-width: 1024px){
 .archive-options{
  background-color:  blue;
  
  }  
}

/*###Tablet(medium)###*/
@media screen and (min-width : 768px) and (max-width : 1023px){
.archive-options{
  background-color:  blue;
  
  }  
}

/*### Smartphones (portrait and landscape)(small)### */
@media screen and (min-width : 0px) and (max-width : 767px){
  .archive{
  height: 1000px;
}

.archive-options{
  background-color:  white ; /* blue */
  
  } 

 .search{
  width: 135px;
}

.chooseArchive{
  width: 120px;
 }

/*
#archiveSelector{
  background-color: white;
}
*/

#searchIcon{
  	padding-left: 3px;
}

/* sort dropdown */

#sortArchiveBody{
  padding-top:10px; 
  font-size: 15px;
}

.sortOptions {
  width:auto;
}

.sortOptions > label{
  width:40%;
  font-size: 75%;
}

.sortOptions > input{
  width:60%;
}

#defaultInline2Div{
  margin-left: 0px;
}


/*  */

.subArchivePlus{
  width:120px;
  height: 140px;
  margin-top:25px;
  margin-left: 25px;
  margin-right: 10px;
  display: block; 
  float: left;
  /* varijanta manji razmak i centrirane
  margin-left: 10px;
  margin-right: 10px;
  display: inline-block; */
}

.dropdown-toggle::after{
  display: none;
}


}

.subArchivePlus:hover{
  cursor: pointer;
}
</style>
