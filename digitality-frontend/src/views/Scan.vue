<template>
    <div class="container">
      <croppa v-model="myCroppa"
         
        :width="700"
        :height="500"
         placeholder="Drag and drop your file here"
        :placeholder-font-size="40"
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

.container {
  display: -webkit-box;
  justify-content: center;
  align-items: center;
  height: 700px;
}


.croppa-container{
  /* https://kovart.github.io/dashed-border-generator/ */
  background-image: url("data:image/svg+xml,%3csvg width='100%25' height='100%25' xmlns='http://www.w3.org/2000/svg'%3e%3crect width='100%25' height='100%25' fill='none' stroke='%2300A2FFFF' stroke-width='6' stroke-dasharray='23' stroke-dashoffset='0' stroke-linecap='square'/%3e%3c/svg%3e")
  
}

</style>