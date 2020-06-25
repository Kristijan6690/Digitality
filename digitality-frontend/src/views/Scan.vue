<template>
  <div class="container">
    
     <div class="row">

        <div class="alert alert-success alert-dismissible fade show" id="successAlert">
          <button type="button" class="close" data-dismiss="alert">&times;</button>
          <strong>Uspjeh!</strong> Vaša slika je uspješno učitana i trenutno se obrađuje. Bit ćete preusmjereni na rezultate. Ako ima praznih
                                   polja znači da ih nije uspjelo prepoznati pa ćete ih popuniti ručno.
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
        loading-start
        loading-end
      ></croppa>
      

  </div>
</template>

<script>
import store from "@/store.js";
import "vue-croppa/dist/vue-croppa.css";
import { app } from "@/services";
import { Auth } from "@/services";
import Loading from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/vue-loading.css';

export default {
  data() {
    return {
      user: localStorage.getItem('user'),
      fullPage: true,
      myCroppa: null,
      placeholder: 'Drag and drop your file here',
      store
      
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

  //još urediti kod i funkcionalnost
  //https://vuejsexamples.com/vue-js-component-for-full-screen-loading-indicator/
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
       },20000)                 
      },
      onCancel() {
        console.log('User cancelled the loader.')
    },

   async onLoad() {
      this.startLoading();
      let blobData = await this.getImageBlob()
      let url = this.user.email + "/" + Date.now() + ".png";
      let result = await storage.ref(url).put(blobData);
      let url_dokumenta = await result.ref.getDownloadURL();
      let temp = await app.sendDocument(url_dokumenta);
      localStorage.setItem('scan_doc_data',JSON.stringify(temp))
      this.$router.push({ name: 'ManualScan' })
    },

                 
  },

  myEventHandler(e) {
      if(screen.width < 757){ 
        this.placeholder = 'Choose a file';
        console.log('manji')
      }

      else{
        this.placeholder = 'Drag and drop your file here';
        console.log('veci')
      }
    },

  created() {
    window.addEventListener("resize", this.myEventHandler);
  },
  destroyed() {
    window.removeEventListener("resize", this.myEventHandler);
  },


  mounted(){
    $('#successAlert').hide();
    $('#warningAlert').hide();
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