<template>
  <div class="home">
      <div class="container">
        <div class="row">

            <div class="col archive-options">
                  <div class="settings">
                      <i class="fas fa-cog fa-lg"></i>
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
                
                      <div class="btn-group">
                      <button type="button" class="btn btn-secondary filter" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="text-align:center;">
                        <div id="filterIcon" style="display:inline-block; position: absolute; left: 3px; top: 4px;"><i class="fa fa-filter  fa-lg"  aria-hidden="true" ></i></div>
                      </button>
                      <div class="dropdown-menu dropdown-menu-right">
                        <button class="dropdown-item" type="button">Action</button>
                        <button class="dropdown-item" type="button">Another action</button>
                        <button class="dropdown-item" type="button">Something else here</button>
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
                <SubArchive v-bind:key="card.id" v-bind:info="card" v-for="card in this.store.arhiveData" />
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
<!-- popraviti :  header vise nalik prototipu?, da dugi nazivi neidu izvan, poredak elemenata, mobile responsive, footer?-->
<script>

import SubArchive from '@/components/SubArchive.vue'
import axios from 'axios';
import store from "@/store.js";

export default {

  data() {
    return {
      store
    }
  },

  name: 'Home',
  components: {
    SubArchive
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
  margin : 10px 5px  10px 5px; 
  float: right;
  border-radius: 5px;
  border: 2px solid  #00A2FF;
  padding-top: 4px;
  color:#00A2FF;
  
}

.btn-group{
  display:block;
}

.btn-group>.btn:first-child {
  margin-left: 5px;
  border-radius: 5px;
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

}


</style>
