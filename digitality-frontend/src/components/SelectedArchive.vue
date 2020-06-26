<template>
    <div class="filterOptions custom-control custom-radio">
        <button v-on:click="$emit('get_archive', info._id)">{{info.name}}</button>
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
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
button{
  border: none;
}

.filterOptions{
  padding-left: 0px;
}


</style>
