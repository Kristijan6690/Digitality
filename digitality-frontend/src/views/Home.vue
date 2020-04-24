<template>
  <div class="home">
      <div class="container">
        <div class="row">

            <div class="col archive-options">
                <!-- filter i filter dropdown -->
                      <div class="btn-group" >
                        <button type="button" class="btn btn-secondary settings" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" >
                          <div id="filterIcon" ><i class="fas fa-cog fa-lg"></i></div>
                        </button>

                        <div class="dropdown-menu dropdown-menu-left" @click.stop=''>
                          <div class="dropdownHeader" > 
                              <h2> Postavke </h2> 
                          </div>
                          <div id="archiveSelection">
                            <i class="far fa-edit"></i>
                            <h2> Moja_arhiva </h2> 
                          </div>
                          <div class="dropdownBody">                       
                            <div id="pristupNaslov">
                              Osobe sa pristupom
                            </div>
                              <div id="pristupPopis">
                                  <div class="mailOsobe">adasdasdasda@adasdasd.com</div> <div class="opcijaPopis">ukloni</div>  
                                  <div class="mailOsobe">adassda@adasdasd.com</div> <div class="opcijaPopis">ukloni</div>  
                                  <div class="mailOsobe">adasddasda@adasdasd.com</div> <div class="opcijaPopis">ukloni</div>  
                              </div>
                            
                          </div>
                          <div class="dropdownFooter addButtonDiv">
                                <button type="submit" class="btn btn-primary my-2 my-sm-0" id="addButton" style="padding-right: 5px;"> Traži</button>
                                <button type="submit" class="btn btn-primary my-2 my-sm-0" id="addButton" style="padding-left: 5px;"> Poništi</button>
                          </div>
                      </div>
                    </div>

                  <div class="chooseArchive">
                      <i class="far fa-file fa-lg" ></i>
                      <select id="archiveSelector">
                          <option value="Archive_1">Arhiva_1</option>
                          <option value="Archive_2">Arhiva_2</option>
                          <option value="Archive_3">Arhiva_3</option>
                          <option value="Archive_4">Arhiva_4</option>
                        </select>
                  </div>
                      <!-- filter i filter dropdown -->
                      <div class="btn-group" >
                        <button type="button" class="btn btn-secondary filter" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" >
                          <div id="filterIcon" ><i class="fa fa-filter  fa-lg"  aria-hidden="true" ></i></div>
                        </button>

                        <div class="dropdown-menu dropdown-menu-right" @click.stop=''>
                          <div class="dropdownHeader" > 
                              <h2 >Filter</h2> 
                          </div>

                          <div class="dropdownBody">                       
                              <div class="filterOptions custom-control custom-checkbox " >
                                <input type="checkbox" class="custom-control-input" id="datDodavanja" name="datDodavanja" value="datDodavanja">
                                <label for="datDodavanja" class="custom-control-label">Datum dodavanja:</label>
                                <input type="text" id="datDodavanja" name="datDodavanja"><br>
                              </div>
                              <div class="filterOptions custom-control custom-checkbox ">
                                <input type="checkbox" class="custom-control-input" id="nazDobavljaca" name="nazDobavljaca" value="nazDobavljaca">
                                <label for="nazDobavljaca" class="custom-control-label" >Naziv dobavljača:</label>
                                <input type="text" id="nazDobavljaca" name="nazDobavljaca"><br>
                              </div>
                              <div class="filterOptions custom-control custom-checkbox ">
                                <input type="checkbox" class="custom-control-input" id="datIzdavanja" name="datIzdavanja" value="datIzdavanja">
                                <label for="datIzdavanja" class="custom-control-label">Datum izdavanja:</label>
                                <input type="text" id="datIzdavanja" name="datIzdavanja"><br>
                              </div>
                              <div class="filterOptions custom-control custom-checkbox ">
                                <input type="checkbox" class="custom-control-input" id="datDospijeca" name="datDospijeca" value="datDospijeca">
                                <label for="datDospijeca" class="custom-control-label">Datum dospijeća:</label>
                                <input type="text" id="datDospijeca" name="datDospijeca"><br>
                              </div>
                              <div class="filterOptions custom-control custom-checkbox ">
                                <input type="checkbox" class="custom-control-input" id="vrstaUsluge" name="vrstaUsluge" value="vrstaUsluge">
                                <label for="vrstaUsluge" class="custom-control-label">Vrsta usluge:</label>
                                <input type="text" id="vrstaUsluge" name="vrstaUsluge"><br>
                              </div>
                              <div class="filterOptions custom-control custom-checkbox ">
                                <input type="checkbox" class="custom-control-input" id="kolicina" name="kolicina" value="kolicina">
                                <label for="kolicina" class="custom-control-label">Kolicina:</label>
                                <input type="text" id="kolicina" name="kolicina"><br>
                              </div>
                              <div class="filterOptions custom-control custom-checkbox ">
                                <input type="checkbox" class="custom-control-input" id="iznos" name="iznos" value="iznos">
                                <label for="iznos" class="custom-control-label">Iznos:</label>
                                <input type="text" id="iznos" name="iznos"><br>
                              </div>
                            
                          </div>
                          <div class="dropdownFooter addButtonDiv">
                                <button type="submit" class="btn btn-primary my-2 my-sm-0" id="addButton" > Traži</button>
                          </div>
                      </div>
                    </div>

                  <div class="search">
                      <input id="searchBar" type="text" placeholder="Traži..."/>
                      <i class="fas fa-search fa-lg" id="searchIcon"></i>
                  </div>
                  
            </div>         
        </div>

        <div class="row">
          <div class="col archive">
            <ArchiveCard v-bind:key="card.id" v-bind:info="card" v-for="card in store.archiveData" />
            <div class="subArchive" >
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
    <router-link to="/login">Login</router-link>
  </div>
</template>
<!-- popraviti :  search bottom padding elip, effecti elips, header vise nalik prototipu?, da dugi nazivi neidu izvan, poredak elemenata, mobile responsive, footer? active navbar, bolji način za pozicioniranje filter ikone-->
<script>

import ArchiveCard from '@/components/ArchiveCard.vue'
import store from "@/store.js";

export default {
  data(){
    return {
      store
    }
  },

  name: 'Home',
  components: {
    ArchiveCard
  },
  
  methods:{
    
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

.subArchive{
  width:120px;
  height: 140px;
  margin-top:25px;
  margin-left: 48px;
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

.addButtonDiv{
display: flex; 
align-items: center; 
justify-content: center; 
height: 60px; 
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

/* filter dropdown */

.filterOptions {
  width:auto;
}

.filterOptions > label{
  width:40%;
  font-size: 75%;
}

.filterOptions > input{
  width:60%;
}

}
</style>
