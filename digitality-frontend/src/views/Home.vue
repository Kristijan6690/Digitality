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
                               
                                <div class="userData" >
                                    <div class="personIcon"><i class="far fa-user"></i></div>
                                    <div class="mailOsobe">example@email.com</div> 
                                    <div class="opcijaPopis">ukloni</div>  
                                </div>
                                <div class="userData">
                                    <div class="personIcon"><i class="far fa-user"></i> </div>
                                    <div class="mailOsobe">example@email.com</div> 
                                    <div class="opcijaPopis">ukloni</div>  
                                </div>
                                <div class="userData" >
                                     <div class="personIcon"><i class="far fa-user"></i> </div>
                                     <div class="mailOsobe">example@email.com</div> 
                                     <div class="opcijaPopis">ukloni</div>  
                                </div>
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

                    <!-- choose Archive (Dropdown umjesto selecta zbog veće mogućnosti customizacije -- prebaciti css u css--> 
                     <div class="btn-group  dropdown" >
                       
                       <button class="btn btn-light dropdown-toggle chooseArchive" type="button" id="dropdownMenuArchive" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="color: #00A2FF; margin-left:0px; text-align:left; vertical-align: top;">
                        <div style="display:inline-block; padding: 0px 5px; width:20%; vertical-align: top;"><i class="far fa-file fa-lg" ></i></div>
                        <div style="display:inline-block; padding: 0px 10px; width:70%; overflow:hidden; text-overflow: ellipsis;  vertical-align: top;"> {{store.currentArchive}} </div>
                      </button>
                      <div class="dropdown-menu dropdown-menu-left menu-settings">
                          <div class="dropdownHeader"  @click.stop=''> 
                              <h2 id="archiveHeader" style="font-size: 1.5rem; margin:5px 20px 0 20px; height:35px;"> Odaberite arhivu </h2> 
                          </div>
                  
                          <div class="dropdownBody body-settings" style="border: solid 1px #D3D3D3; margin: 0px 40px 0 40px; padding: 0 0 0 0;">                       
                            
                              <div id="pristupPopis" style="padding: 5px 5px 30px 5px; ">  
                               <form id="archiveForm" name="archiveForm">
                                <div class="filterOptions custom-control custom-radio " >
                                  <input  v-model="store.currentArchive" checked="checked" type="radio" class="custom-control-input" id="Arhiva_1" name="Archive" value="Arhiva_1">
                                  <label for="Arhiva_1" class="custom-control-label">Arhiva_1</label>
                                </div>
                                <div class="filterOptions custom-control custom-radio " >
                                  <input  v-model="store.currentArchive" type="radio" class="custom-control-input" id="Arhiva_2" name="Archive" value="Arhiva_2">
                                  <label for="Arhiva_2" class="custom-control-label">Arhiva_2</label>
                                </div>
                                <div class="filterOptions custom-control custom-radio " >
                                  <input v-model="store.currentArchive"  type="radio" class="custom-control-input" id="Arhiva_3" name="Archive" value="Arhiva_3">
                                  <label for="Arhiva_3" class="custom-control-label">Arhiva_3</label>
                                </div>
                                <div class="filterOptions custom-control custom-radio " >
                                  <input v-model="store.currentArchive" type="radio" class="custom-control-input" id="Arhiva_4" name="Archive" value="Arhiva_4">
                                  <label for="Arhiva_4" class="custom-control-label">Arhiva_4</label>
                                </div>
                                <div class="filterOptions custom-control custom-radio " >
                                  <input v-model="store.currentArchive" type="radio" class="custom-control-input" id="Arhiva_5" name="Archive" value="Arhiva_5">
                                  <label for="Arhiva_5" class="custom-control-label">Arhiva_5_Dugi_Naziv</label>
                                </div>
                               </form>
                              </div>
                            </div>
                          <div class="dropdownFooter addButtonDiv"  @click.stop=''>
                                <button type="submit" class="btn btn-primary my-2 my-sm-0" id="addButtonSettings" style="margin: 5px; border-radius:5px; border:0" > Dodaj </button>
                                <button type="submit" class="btn btn-primary my-2 my-sm-0" id="removeButtonSettings" style="margin: 5px;  border-radius:5px; background-color: #888888; border:0"> Poništi</button>
                          </div>
                      </div>
                    </div>
            
                  
                       <!-- sort dropdown prebaciti css u css i popraviti nazive-->
                      <div class="btn-group" >
                        <button type="button" class="btn btn-secondary sort" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" >
                          <div id="sortIcon" ><i class="fas fa-sort-amount-down fa-lg"></i></div>
                        </button>

                        <div class="dropdown-menu dropdown-menu-right" @click.stop=''>
                          <div class="dropdownHeader" >
                              <h2 style="height:42px;">Organiziraj arhivu</h2> 
                          </div>

                          <div class="dropdownBody" style="padding-top:10px; font-size: 15px;">              
                            <div style="margin: 0 10px 0 10px">         
                                <!-- Default inline 1 bootstrap-->
                              <div class="custom-control custom-checkbox custom-control-inline">
                                <input @click="selectOnlyThis(this.id)"  name="myCheckbox" value="1" type="checkbox" class="custom-control-input" id="defaultInline1" >
                                <label class="custom-control-label" for="defaultInline1" style="padding-right:5px;">
                                  Datum pregleda silazno 
                                  <i class="fas fa-sort-amount-down"></i>       
                                </label>  
                              </div>

                              <!-- Default inline 2-->
                              <div class="custom-control custom-checkbox custom-control-inline" id="defaultInline2Div" >
                                <input onclick="selectOnlyThis(this.id)"  name="myCheckbox" value="2" type="checkbox" class="custom-control-input" id="defaultInline2">
                                <label class="custom-control-label" for="defaultInline2" style="padding-right:5px;">
                                  Abecedno silazno
                                  <i class="fas fa-sort-amount-up"></i>    
                                </label>       
                              </div>
                            </div>
                             
                            <div style="margin: 0 10px 0 10px">    
                              <!-- Default inline 3-->
                              <div class="custom-control custom-checkbox custom-control-inline">
                                <input onclick="selectOnlyThis(this.id)"  name="myCheckbox" value="3" type="checkbox" class="custom-control-input" id="defaultInline3">
                                <label class="custom-control-label" for="defaultInline3" style="padding-right:5px;">
                                  Datum pregleda uzlazno
                                  <i class="fas fa-sort-numeric-down-alt"></i>
                                </label>
                               
                              </div>
                              <!-- Default inline 4-->
                              <div class="custom-control custom-checkbox custom-control-inline"> 
                                <input onclick="selectOnlyThis(this.id)"  name="myCheckbox" value="4" type="checkbox" class="custom-control-input" id="defaultInline4">
                                <label class="custom-control-label" for="defaultInline4" style="padding-right:5px;">
                                  Abecedno uzlazno
                                  <i class="fas fa-sort-numeric-up-alt"></i>
                                </label>         
                              </div>
                            </div>
                                                   
                          </div>
                          <div class="addButtonDiv">
                                <button type="submit" class="btn btn-primary my-2 my-sm-0" id="sortButton"> Potvrdi </button>
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
            <ArchiveCard v-bind:key="card.id" v-bind:info="card" v-for="card in store.archiveData" />
            <div class="subArchivePlus" >
                <div class="folder"><i class="fas fa-folder-plus fa-7x" ></i></div>
                <div class="folderName">Dodaj podarhivu</div>
          </div>
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
<!-- popraviti : logo na title kartici,mobile dva subarchiva u jednom redu,settings email overflow, search bottom padding elip, effecti elips, header vise nalik prototipu?, da dugi nazivi neidu izvan, poredak elemenata, mobile responsive, footer? active navbar, bolji način za pozicioniranje filter ikone-->
<script>

import ArchiveCard from '@/components/ArchiveCard.vue';
import { app } from "@/services";
import store from "@/store.js";
import _ from "lodash";

export default {
  data(){
    return {
      searchTerm: '',
      store
    }
  },

  name: 'Home',
  components: {
    ArchiveCard
  },

  watch: {
    "searchTerm": _.debounce(function(val) {
      this.searchArchives(val);
    }, 500)
  },
  
  methods:{
    async searchArchives(pretraga){
      pretraga = this.searchTerm
      this.store.archiveData = await app.getSearchArchives(pretraga)
    },

  //https://stackoverflow.com/questions/6724064/only-one-selected-checkbox
  selectOnlyThis(id){
    var myCheckbox = document.getElementsByName("myCheckbox");
    Array.prototype.forEach.call(myCheckbox,function(el){
    el.checked = false;
     });
    id.checked = true;  
    },
    
  },

  async mounted() {
    let result = await app.getArchives() // jos nadogradit da vuce za određenog usera
    if (result) this.store.archiveData = result
    else console.log("Prazan collection")
    let datum = this.store.current_date();
    console.log(datum)
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
  height: 600px;
  float:left;
  /*border-radius: 10px;  -> varijanta za white archive options*/
  padding-left:15px;  /* varijanta bez paddinga? */
  padding-right:15px;
  /* border-bottom: 2px solid  #00A2FF;  -border za footer */
}

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

#archiveSelection > h2 {
  text-align:center; 
  color: #00A2FF; 
  position:relative;
}

#archiveSelection {
  height: 50px; 
  position: relative;
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


#archiveHeader::before {
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

.fa-file{
  width:10%;
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


#addButton{
  font-size:17.5px; 
  width:100px;
  border-radius: 10px;
}

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

#archiveSelector{
  background-color: white;
}

#searchIcon{
  	padding-left: 3px;
}

/* sort dropdown */

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
</style>
