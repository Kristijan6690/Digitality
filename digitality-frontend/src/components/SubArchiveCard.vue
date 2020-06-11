<template>
  <router-link v-bind:to="'SubArchive/' + info.name">
    <div class="subArchive" >
        <div class="folder"><i class="fas fa-folder fa-7x" ></i></div>
        <div class="folderName">{{info.name}}</div>
    </div>
  </router-link>
</template>

<script>
export default {
  props: ["info"]
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.subArchive{
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

.fa-folder, .fa-folder-plus{
  text-shadow: 0 0 10px #00A2FF;
  color: #888888;  
}

@media screen and (min-width : 0px) and (max-width : 767px){
.subArchive{
  width:120px;
  height: 140px;
  margin-top:25px;
  margin-left: 25px;
  margin-right: 10px;
  display: block; 
  float: left;
  }

}

</style>
