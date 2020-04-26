<template>
  <div class="container">
    <croppa 
        v-model="myCroppa"
        :width="700"
        :height="500"
        :placeholder="'Drag and drop your file here'"
        :placeholder-font-size="40"
        :quality="2"
        :zoom-speed="3"
        :disabled="false"
        :disable-drag-and-drop="false"
        :disable-click-to-choose="false"
        :disable-drag-to-move="true"
        :disable-scroll-to-zoom="true"
        :disable-rotation="true"
        :prevent-white-space="false"
        :reverse-scroll-to-zoom="false"
        :show-remove-button="false"
        :initial-image="'path/to/initial-image.png'"
        @new-image-drawn="onLoad()"
      ></croppa>
  </div>
</template>

<script>
import store from "@/store.js";
import "vue-croppa/dist/vue-croppa.css";
import { app } from "@/services";

export default {
  data() {
    return {
      myCroppa: null
    };
  },

  methods: {
    getImageBlob(){
      return new Promise((resolve,reject) => {
        this.myCroppa.generateBlob(blobData => {
          if(blobData != null) {
            resolve(blobData)
          }
          else {
            reject("Error with getting blob")
          }
        })
      })
    },

    async onLoad() {
      let blobData = await this.getImageBlob()
      let url_dokumenta = "nesto"   // osmislit od kud cemo vuci url
      console.log(blobData,url_dokumenta)
      await app.sendDocument(blobData,url_dokumenta)
    },

  }
};
//popraviti: na mobitelu i kompu drugaciji prikaz, dodati forgot password, popraviti za neke ekrane small tag se ne ponasa kako treba, staviti ikonu za brisanje maila?
</script>

<style scoped>
.container {
  display: -webkit-box;
  justify-content: center;
  align-items: center;
  height: 700px;
}

.croppa-container {
  /* https://kovart.github.io/dashed-border-generator/ */
  background-image: url("data:image/svg+xml,%3csvg width='100%25' height='100%25' xmlns='http://www.w3.org/2000/svg'%3e%3crect width='100%25' height='100%25' fill='none' stroke='%2300A2FFFF' stroke-width='6' stroke-dasharray='23' stroke-dashoffset='0' stroke-linecap='square'/%3e%3c/svg%3e");
}
</style>