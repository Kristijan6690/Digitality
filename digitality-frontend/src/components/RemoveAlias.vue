<template>
    <div class="row main"  >           
                    
        <div class="data">
            <label for="Ime">Ime:</label>
            <input v-model="Ime" type="text" id="Ime" name="Alias" readonly>
        </div>
        <div class="data">
            <label for="Prezime">Prezime:</label>
            <input v-model="Prezime" type="text" id="Prezime" name="Alias" readonly>
        </div> 
        <div class="data">
            <label for="OIB">OIB:</label>
            <input v-model="OIB" type="text" id="OIB" name="Alias" readonly>
        </div> 
        <div class="data">
            <label for="IBAN">IBAN:</label>
            <input v-model="IBAN" type="text" id="IBAN" name="Alias" readonly>
        </div> 
        <div class="dataLong">
            <label for="PostanskBroj">Poštanski broj:</label>
            <input v-model="PostanskiBroj" type="text" id="PostanskiBroj" name="Alias" readonly>
        </div> 
        <div class="button" style="display:block; text-align:center;">
            <button style="border:none;"><i class="fa fa-window-close" aria-hidden="true" style="color:red;"></i></button>
        </div> 

    </div>
</template>

<script>
import store from "@/store.js";

export default {
  data() {
    return {
      store,
      Ime,
      Prezime,
      OIB,
      IBAN,
      PostanskiBroj
    };
  },
  props: ["info"],

  methods:{
    
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

.row{
    margin-right: 0px;
    margin-left: 0px;
    background-color:#eeeeee;
}


input{
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
    width: 45%;

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

@media screen and (min-width : 0px) and (max-width : 767px){
.dataLong{
    display:inline-block;
    margin-bottom: .5rem; 
    width:340px;  
}

.button{
    display:block; 
    width:100%;
}

}

</style>
