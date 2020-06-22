<template>
    <div class="filterOptions custom-control custom-radio " >
        <input checked="checked" type="radio" class="custom-control-input" id="Arhiva_1" name="Archive" value="Arhiva_1">
        <label for="Arhiva_1" class="custom-control-label"> {{info.name}} </label> 
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
  props: ["info"],

  methods:{
    
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">



</style>
