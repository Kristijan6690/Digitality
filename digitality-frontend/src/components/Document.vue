<template>
    <router-link v-bind:to="'/internet/' + 1">>
        <div class="document" >
            <div class="documentName">{{info.tekst}}</div>
            <div class="documentPicDiv">
                <img src="align-justify.png" class="documentPic" />
            </div>
            <div class="documentDate">01/01/2020 at 00:00</div>
        </div>
    </router-link>
</template>

<script>
export default {
  name: 'Document',
  props: ["info"]
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

.document{
    width: 250px;
    height: 300px;
    display:block;
    background-color:white;
    margin-top:25px;
    margin-left: 22.5px;
    display: block; 
    float: left;
    border: 2px solid  #707070;
    
}

.documentName{
    background-color: white;
    height: 15%;
    line-height: 50px;
    font-size: 25px;
    color : #707070
}

.documentPicDiv{
    background-color: white;
    height: 75%;
}

.documentDate{
    height: 10%;
    background-color: white;
    font-size: 17.5px;
    color  : #707070;
}

</style>
