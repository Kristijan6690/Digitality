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
                          <option value="Archive_1">Internet</option>
                          <option value="Archive_2">Struja</option>
                          <option value="Archive_3">Voda</option>
                          <option value="Archive_4">Ostalo</option>
                        </select>
                  </div>
                  <div class="filter">
                      <i class="fa fa-filter  fa-lg"  aria-hidden="true" ></i>
                  </div>
                  <div class="search">
                      <input id="searchBar" type="text" placeholder="Traži..."/>
                      <i class="fas fa-search fa-lg" id="searchIcon"></i>
                  </div>
                  
            </div>         
        </div>
        <div class="row">
            <div class="col heading">
                  <!-- maknuti submit iz buttona? -->
                  <button type="submit" class="btn btn-pr imary my-2 my-sm-0" id="backButton">Natrag</button>             
                  <div style="width: 100%;" id="headlineDiv"><h1 id="headline">Internet</h1></div>
                  <button type="submit" class="btn btn-primary my-2 my-sm-0" id="deleteButton">Izbriši</button>
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
<!-- popraviti :  da dugi nazivi neidu izvan mobile responsive, footer? back i delete buttoni na mobitelu -> back btn netreba na mobu, delete u settings?-->
<!-- waves effect <div class="form-group waves-light waves-effect waves-light" style="width:100%;">  -->
							
<script>

import Document from '@/components/Document.vue';
import axios from 'axios';

export default {
  data(){
    return{
      naziv: this.$route.params.naziv_arhive,  //naziv_arhive -> varijabla u /router/index.js
      documentData: ""   // podaci za svaki dokument sa arhive
    }
  },

  name: 'SubArchive',  //krivo ?
  components: {
    Document
  },

  mounted(){
    axios.post("http://127.0.0.1:5000/dokumenti", {
      naziv: this.naziv
      }).then((response) =>{
        this.documentData = response.data
      }).catch((err) =>{
        console.log(err)
      })
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
