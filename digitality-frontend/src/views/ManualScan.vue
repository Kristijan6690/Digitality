<template>
  <div class="home">
      <div class="container">
            <div class="row">
                <!-- mjesto za header ako ce ici -->
            </div>
            <div class="row">
                 <div class="col heading">        
                  <div  id="headlineDiv" ><h1 id="headline">Univerzalni nalog</h1></div>
                  <div><i class="fas fa-info-circle fa-2x" ></i></div>
                </div>         
            </div>
            <form action="/action_page.php">
                <div class="row main" >
                        <div class="box one archive">
                            <div class="data">
                                <label for="fname">Naziv dobavljača:</label>
                                <input type="text" id="fname" name="fname"><br>
                            </div>
                            <div class="data">
                                <label for="fname">Naziv kupca:</label>
                                <input type="text" id="fname" name="fname"><br><br>
                            </div>
                            <div class="data">
                                <label for="fname">Broj računa:</label>
                                <input type="text" id="fname" name="fname"><br><br>
                            </div>
                            <div class="data">
                                <label for="fname">Mjesto izdavanja:</label>
                                <input type="text" id="fname" name="fname"><br>
                            </div>
                            <div class="data">
                                <label for="fname">Datum izdavanja:</label>
                                <input type="text" id="fname" name="fname"><br>
                            </div>
                            <div class="data">
                                <label for="fname" >Vrsta usluge:</label>
                                <input type="text" id="fname" name="fname" placeholder="internet / struja / mobilni operater..."><br>
                            </div>
                            <div class="data">
                                <label for="fname">Količina:</label>
                                <input type="text" id="fname" name="fname"><br>
                            </div>
                            <div class="data">
                                <label for="fname">Poziv na broj:</label>
                                <input type="text" id="fname" name="fname"><br>
                            </div>
                            <div class="data">
                                <label for="fname">IBAN platitelja:</label>
                                <input type="text" id="fname" name="fname"><br>
                            </div>
                        </div>
                        <div class="box two archive">
                             <div class="data">
                                <label for="fname">OIB dobavljača:</label>
                                <input type="text" id="fname" name="fname"><br>
                            </div>
                            <div class="data">
                                <label for="fname">OIB kupca:</label>
                                <input type="text" id="fname" name="fname"><br><br><br><br>
                            </div>
                            <div class="data datumDospijeca">
                                <label for="fname">Datum dospijeća:</label>
                                <input type="text" id="fname" name="fname"><br><br><br><br>
                            </div>
                            <div class="data">
                                <label for="fname">PDV:</label>
                                <input type="text" id="fname" name="fname"><br>
                            </div>
                            <div class="data">
                                <label for="fname">Iznos:</label>
                                <input type="text" id="fname" name="fname"><br>
                            </div>
                            <div class="data">
                                <label for="fname">IBAN primatelja:</label>
                                <input type="text" id="fname" name="fname"><br>
                            </div> 
                        </div>
        
                </div>
                <div class="row addButtonDiv">
                    <button type="submit" class="btn btn-primary my-2 my-sm-0" id="addButton" >Dodaj</button>
                </div> 
            </form>
            <!-- footer
            <div class="row">
                <div class="col archive"></div>
            </div>
            -->
      </div>
  </div>
</template>
<!-- popraviti :  mobile responsive, footer?, hovere na sve-->
<script>

import SubArchive from '@/components/SubArchive.vue'

export default {
  name: 'Home',
  components: {
    SubArchive
  }
}
</script>

<style scoped>

.row{
    margin-right: 0px;
    margin-left: 0px;
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

input{
    display:inline-block;
    width:70%;
    border-radius: 5px;
    border: 1px solid  #00A2FF;
    padding-left: 10px;
    padding-right: 10px;
}

label{
    color:black;
    display:inline-block;
    width:30%;
    margin-bottom: 0px;
    text-align:left

}

.data{
    display:block;
    margin-bottom: .5rem; 
    width: 100%;
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
  padding-left:33px;
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

}
</style>
