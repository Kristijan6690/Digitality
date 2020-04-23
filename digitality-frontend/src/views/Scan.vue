<template>
  <div class="scanDiv">
      jioasjdioajsidjosa
      <croppa v-model="myCroppa"
        :width="500"
        :height="500"
        placeholder="Drag and drop your file here"
        :placeholder-font-size="33"
        :disabled="false"
        :prevent-white-space="false"
        :show-remove-button="true"
       >                                          
    </croppa > 
  </div>
</template>

<script>
import axios from "axios";
import store from '@/store.js';
  import 'vue-croppa/dist/vue-croppa.css'



export default {
  data(){
    return {
      myCroppa:{}
    }
  },

  methods: {
     uploadCroppedImage() {
       this.myCroppa.generateBlob((blob) => {
         // write code to upload the cropped image file (a file is a blob)
       }, 'image/jpeg', 0.8) // 80% compressed jpeg file
     }
   }
}
//popraviti: na mobitelu i kompu drugaciji prikaz, dodati forgot password, popraviti za neke ekrane small tag se ne ponasa kako treba, staviti ikonu za brisanje maila?
</script>

<style scoped>



</style>