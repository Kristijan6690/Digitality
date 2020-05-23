<template>
  <div class="container" >
    
     <div class="row" style="display:inline-block;">

        <div class="alert alert-success alert-dismissible fade show" id="successAlert">
          <button type="button" class="close" data-dismiss="alert">&times;</button>
          <strong>Uspjeh!</strong> Vaš dokument je uspješno obrađen i spremljen u arhivu "xyz".
        </div>
        
        <div class="alert alert-warning alert-dismissible fade show" id="warningAlert">
          <button type="button" class="close" data-dismiss="alert">&times;</button>
          <strong>Greška!</strong> Došlo je do greške prilikom obrade dokumenta.
        </div>
      
    </div>
     
     <croppa class="c1"
        v-model="myCroppa"
        :width="700"
        :height="500"
        :placeholder= this.placeholder
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
        auto-sizing
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
      myCroppa: null,
      placeholder: 'Drag and drop your file here'
    };
  },

  methods: {
    getImageBlob(){
      return new Promise((resolve,reject) => {
        this.myCroppa.generateBlob(blobData => {
          if(blobData != null) {
            resolve(blobData)
            $('#successAlert').show();
          }
          else {
            reject("Error with getting blob")
             $('#warningAlert').show();
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
  },

  myEventHandler(e) {
      if(screen.width < 757){
        this.placeholder = 'Choose a file';
      }

      else{
        this.placeholder = 'Drag and drop your file here';
      }
    },

  created() {
    window.addEventListener("resize", this.myEventHandler);
  },

  

  mounted(){
    $('#successAlert').hide();
    $('#warningAlert').hide();
  }

};


//popraviti: na mobitelu i kompu drugaciji prikaz, dodati forgot password, popraviti za neke ekrane small tag se ne ponasa kako treba, staviti ikonu za brisanje maila?
</script>

<style scoped>

.croppa-container.c1 {
  width: 750px;
  height: 550px;
  margin: 50px auto;
  display: block;
}

.croppa-container {
  /* https://kovart.github.io/dashed-border-generator/ */
  background-image: url("data:image/svg+xml,%3csvg width='100%25' height='100%25' xmlns='http://www.w3.org/2000/svg'%3e%3crect width='100%25' height='100%25' fill='none' stroke='%2300A2FFFF' stroke-width='6' stroke-dasharray='23' stroke-dashoffset='0' stroke-linecap='square'/%3e%3c/svg%3e");
}

.alert-success, .alert-warining{
  width: 700px;
}

@media screen and (min-width: 768px){
  .croppa-container.c1 {
  width: 750px;
  height: 550px;
  margin: 50px auto;
  display: block;
  }


} 

@media screen and (min-width : 0px) and (max-width : 767px){

  .croppa-container.c1 {
    width: 325px;
    height: 300px;
    display: block;
  }


}

  .alert-success[data-v-6a73f337], .alert-warining[data-v-6a73f337] {
      width: 360px;
  }



</style>