<template>
  <div class="home">
      <div class="container">
            <div class="row">
                <!-- mjesto za header ako ce ici -->
            </div>
            <div class="row">
                 <div class="col heading">        
                    <div  id="headlineDiv" ><h1 id="headline">Univerzalni nalog</h1></div>
                    <button type="button" class="glowEffect" data-toggle="modal" data-target="#pictureModal" style="border:none;"><i class="fa fa-picture-o fa-2x"></i></button>
                    <button type="button" class="glowEffect" data-toggle="modal" data-target="#helpModal" style="border:none;"><i class="fas fa-info-circle fa-2x" ></i></button>
                </div>         
            </div>
            <form action="/action_page.php">
                <div class="row main" >
                        <div class="box one archive">
                            <div class="data">
                                <label for="nazDobavljaca">Naziv dobavljača:</label>
                                <input type="text" v-model="this.current_document.naziv_dobavljaca" id="nazDobavljaca" name="nazDobavljaca" disabled><br>
                            </div>
                            <div class="data">
                                <label for="nazKupca">Naziv kupca:</label>
                                <input type="text" v-model="this.current_document.naziv_kupca" id="nazKupca" name="nazKupca" disabled ><br><br>
                            </div>
                            <div class="data">
                                <label for="brojRacuna">Broj računa:</label>
                                <input type="text" v-model="this.current_document.broj_racuna" id="brojRacuna" name="brojRacuna" disabled ><br><br>
                            </div>
                            <div class="data">
                                <label for="datIzdavanja">Datum izdavanja:</label>
                                <input type="text" v-model="this.current_document.datum_izdavanja" id="datIzdavanja" name="datIzdavanja" disabled ><br>
                            </div>
                            <div class="data">
                                <label for="mjestoIzdavanja">Mjesto izdavanja:</label>
                                <input type="text" v-model="this.current_document.mjesto_izdavanja" id="mjestoIzdavanja" name="mjestoIzdavanja" disabled ><br>
                            </div>
                            <div class="data">
                                <label for="vrstaUsluge" >Vrsta usluge:</label>
                                <input type="text" v-model="this.current_document.vrsta_usluge" id="vrstaUsluge" name="vrstaUsluge" disabled ><br>
                            </div>
                            <div class="data">
                                <label for="netoIznos">Neto iznos:</label>
                                <input type="text" v-model="this.current_document.neto" id="netoIznos" name="netoIznos" disabled ><br>
                            </div>
                            <div class="data">
                                <label for="pozNaBroj">Poziv na broj:</label>
                                <input type="text" v-model="this.current_document.poziv_na_broj" id="pozNaBroj" name="pozNaBroj" disabled ><br>
                            </div>
                            <div class="data">
                                <label for="IBANplatitelja">IBAN platitelja:</label>
                                <input type="text" v-model="this.current_document.iban_platitelja" id="IBANplatitelja" name="IBANplatitelja" disabled ><br>
                            </div>
                        </div>
                        <div class="box two archive">
                             <div class="data">
                                <label for="OIBdobavljaca">OIB dobavljača:</label>
                                <input type="text" v-model="this.current_document.oib_dobavljaca" id="OIBdobavljaca" name="OIBdobavljaca"  disabled ><br>
                            </div>
                            <div class="data">
                                <label for="OIBkupca">OIB kupca:</label>
                                <input type="text" v-model="this.current_document.oib_kupca" id="OIBkupca" name="OIBkupca"  disabled ><br><br><br><br>
                            </div>
                            <div class="data datumDospijeca">
                                <label for="datDospijeca">Datum dospijeća:</label>
                                <input type="text" v-model="this.current_document.datum_dospijeca" id="datDospijeca" name="datDospijeca"  disabled ><br><br><br><br>
                            </div>
                            <div class="data">
                                <label for="pdv">PDV:</label>
                                <input type="text" v-model="this.current_document.pdv" id="pdv" name="pdv"  disabled ><br>
                            </div>
                            <div class="data">
                                <label for="iznos">Iznos:</label>
                                <input type="text" v-model="this.current_document.iznos" id="iznos" name="iznos"  disabled ><br>
                            </div>
                            <div class="data">
                                <label for="IBANprimatelja">IBAN primatelja:</label>
                                <input type="text" v-model="this.current_document.iban_primatelja" id="IBANprimatelja" name="IBANprimatelja"  disabled ><br>
                            </div> 
                        </div>
        
                </div>
                <div class="row addButtonDiv">
                  <router-link v-bind:to="'/editdocument/' + this.current_document.id_dokumenta">
                    <button type="button" class="btn btn-primary my-2 my-sm-0" id="addButton" > Uredi </button>
                  </router-link>
                </div> 
            </form>

            <!-- Document picture Modal -->
              <div class="modal fade" id="pictureModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
                <div class="modal-dialog modal-dialog-centered" role="document">
                  <div class="modal-content">
                    <div class="modal-body">
                      <img style="max-width: 100%;max-height: 100%;" v-bind:src="this.current_document.photo"/>
                    </div>
                    <div class="modal-footer" style="display:block;">
                      <button type="button" class="btn btn-secondary" data-dismiss="modal" style="background-color:#00A2FF">Zatvori</button>
                    </div>
                  </div>
                </div>
              </div>

            <!-- Help Modal -->
                <div class="modal fade" id="helpModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
                  <div class="modal-dialog modal-dialog-centered" role="document">
                    <div class="modal-content">
                      <div class="modal-header" style="display:block;">
                        <h3 class="'col-12 modal-title text-center'" id="exampleModalLongTitle" style="color:#000000;">Pomoć</h3>
                      </div>
                      <div class="modal-body" style="border: 1px solid black; margin-left: 10px; margin-right: 10px;">
                        <p> 
                          Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus,
                          porta ac consectetur ac, vestibulum at eros. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus
                          sagittis lacus vel augue laoreet rutrum faucibus dolor auctor. Aenean lacinia bibendum nulla sed consectetur. 
                        </p>
                        <p>
                          Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus 
                          auctor fringilla. Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget 
                          quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Praesent commodo cursus magna
                        </p>
                        <p>
                          Vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.
                          Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et.
                           Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.
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
      </div>
  </div>
</template>

<script>
import store from "@/store.js";
import { Auth } from "@/services";
export default {
  data(){
    return {
      store,
      document_id : this.$route.params.id,
      user: Auth.getUser(),
      current_document : ''
    }
  },
  computed:{
    check_if_owner_of_archive(){
      if(this.store.currentArchiveData._id == this.user.personal_archive_id) return true
      else return false
    }
  },
  mounted(){
    let temp = JSON.parse(localStorage.getItem('userArchives'))
    this.store.currentArchiveData = this.store.get_users_arhive(temp,this.user.archive_ids)
    for(let i = 0; i < this.store.currentArchiveData.subarchives.length; i++){
      for(let j = 0; j < this.store.currentArchiveData.subarchives[i].documents.length; j++){
        if(this.document_id == this.store.currentArchiveData.subarchives[i].documents[j].id_dokumenta){
          this.current_document = this.store.currentArchiveData.subarchives[i].documents[j]
          break;
        }
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
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
    color:black;
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
  padding: 7.5px 7.5px 7.5px 10px;
}
.fa-picture-o{
  color:#00A2FF; 
  float: right;
  padding: 7.5px;
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