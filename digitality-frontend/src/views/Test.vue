<template>
  <div class="container" style="width:500px, height:500px; background:blue;">

    <form @submit.prevent="submit" class="vld-parent" ref="formContainer" >
        <!-- your form inputs goes here-->
        <label><input type="checkbox" v-model="fullPage">Full page?</label>
        <button type="button" @click="startLoading" >Login</button>
    </form>
    

  </div>
</template>

<script>
import store from "@/store.js";
import "vue-croppa/dist/vue-croppa.css";
import { app } from "@/services";
import Loading from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/vue-loading.css';


export default {
  data() {
    return {
      fullPage: true,
      myCroppa: null,
      placeholder: 'Drag and drop your file here',
      store
    };
  },

  methods: {
            startLoading() {
                let loader = this.$loading.show({
                  // Optional parameters
                  container: this.fullPage ? null : this.$refs.formContainer,
                  canCancel: true,
                  onCancel: this.onCancel,
                });
                // simulate AJAX
                setTimeout(() => {
                  loader.hide()
                },5000)                 
            },
            onCancel() {
              console.log('User cancelled the loader.')
            }                      
        }
 

};


//popraviti: na mobitelu i kompu drugaciji prikaz, dodati forgot password, popraviti za neke ekrane small tag se ne ponasa kako treba, staviti ikonu za brisanje maila?
</script>

<style scoped>


.croppa-container {
  /* https://kovart.github.io/dashed-border-generator/ */
  background-image: url("data:image/svg+xml,%3csvg width='100%25' height='100%25' xmlns='http://www.w3.org/2000/svg'%3e%3crect width='100%25' height='100%25' fill='none' stroke='%2300A2FFFF' stroke-width='6' stroke-dasharray='23' stroke-dashoffset='0' stroke-linecap='square'/%3e%3c/svg%3e");
}


@media screen and (min-width: 768px){
 .row{
   display:inline-block; 
   height:50px; 
   width:750px;
 }

  .croppa-container.c1 {
  width: 750px;
  height: 550px;
  margin: auto;
  display: block;
  }

.alert-success, .alert-warning{
  width: 750px;
 }

} 

@media screen and (min-width : 0px) and (max-width : 767px){
  .row{
   display:inline-block; 
   height:100px; 
   width:auto;
 }

  .croppa-container.c1 {
    width: 325px;
    height: 300px;
    display: block;
  }

.alert-success, .alert-warning{
  width: auto;
 }

}

</style>