<template>
    <div class="userData" >
        <div class="personIcon"><i class="far fa-user"></i></div>
        <div class="mailOsobe">example@email.com</div> 
        <div class="opcijaPopis">ukloni</div>  
    </div>
</template>

<script>
import store from "@/store.js";

export default {
  data() {
    return {
      store
    };
  },
  props: ["info"]
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

.userData{
  display: flex;
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

</style>
