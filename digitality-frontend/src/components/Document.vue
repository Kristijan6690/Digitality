<template>
  <router-link v-bind:to="'/SubArchive.DocumentInfo/' + info.id_dokumenta">
    <div class="document">
      <div class="documentName">{{info.iban_platitelja}}</div>
      <div class="documentPicDiv">
        <img src='/Images/align-justify.png'/>
      </div>
      <div class="documentDate">{{info.datum_dospijeca.slice(0,-3)}}</div>
    </div>
  </router-link>
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
.document {
  width: 250px;
  height: 300px;
  display: block;
  background-color: white;
  margin-top: 25px;
  margin-left: 22.5px;
  display: block;
  float: left;
  border: 2px solid #707070;
}

.documentName {
  background-color: white;
  height: 15%;
  line-height: 50px;
  font-size: 25px;
  color: #707070;
}

.documentPicDiv {
  background-color: white;
  height: 75%;
}

.documentDate {
  height: 10%;
  background-color: white;
  font-size: 17.5px;
  color: #707070;
}

@media screen and (min-width : 0px) and (max-width : 767px){
  .document{
    margin-left: 40px;
    margin-right: 40px;
  }
}
</style>
