<template>
  <div class="container" >
    <!--
     <div class="row">
      <div class="alert alert-warning alert-dismissible fade show" role="alert">
            <strong>Holy guacamole!</strong> You should check in on some of those fields below.
            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
      </div>
     </div>
     -->
     <croppa class="croppa1"
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
      
    <!-- success confirmation -->
      <div class="modal fade" id="success_confirmation" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document" >
          
          <div class="modal-content" style="solid; text-align: center; border-radius: 7.5px; ">
              <div class="modal-body" style="font-size: 30px; color:#00A2FF;">
                   Dokument dodan u arhivu _____
                  <hr/>
                  <div data-dismiss="modal" style="font-size:20px; color:#707070">Ok</div>
              </div>
          
            </div>
        </div>
      </div>

      <!-- error confirmation -->
      <div class="modal fade" id="success_confirmation" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document" >
          
          <div class="modal-content" style="solid; text-align: center; border-radius: 7.5px; ">
              <div class="modal-body" style="font-size: 30px; color:#00A2FF;">
                   Došlo je do greške prilikom učitavanja dokumenta
                  <hr/>
                  <div data-dismiss="modal" style="font-size:20px; color:#707070">Ok</div>
              </div>
          
            </div>
        </div>
      </div>

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
      placeholderFontSize: 1,
      placeholder: 'Drag and drop your file here'
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

    myEventHandler(e) {
      if(screen.width < 757){
        this.placeholder = 'Choose a file';
      }

      else{
        this.placeholder = 'Drag and drop your file here';
      }
    }

  },

  created() {
    window.addEventListener("resize", this.myEventHandler);
  },

  destroyed() {
    window.removeEventListener("resize", this.myEventHandler);
  },

};


//popraviti: na mobitelu i kompu drugaciji prikaz, dodati forgot password, popraviti za neke ekrane small tag se ne ponasa kako treba, staviti ikonu za brisanje maila?
</script>

<style scoped>

.container {
  display: -webkit-box;
  justify-content: center;
  align-items: center;
}

.croppa-container {
  /* https://kovart.github.io/dashed-border-generator/ */
  background-image: url("data:image/svg+xml,%3csvg width='100%25' height='100%25' xmlns='http://www.w3.org/2000/svg'%3e%3crect width='100%25' height='100%25' fill='none' stroke='%2300A2FFFF' stroke-width='6' stroke-dasharray='23' stroke-dashoffset='0' stroke-linecap='square'/%3e%3c/svg%3e");
}

@media screen and (min-width: 768px){
 .croppa-container.croppa1 {
  margin: 50px auto;
 }

 .container {
  display: -webkit-box;
  justify-content: center;
  align-items: center;
  }
}


@media screen and (min-width : 0px) and (max-width : 767px){

.croppa-container.croppa1 {
  width: 100%;
  height: 300px;
  margin: 50px auto;
  display: block;
 }
}

canvas{
  width:20px !important;  
}

.container {
  display: -webkit-box;
  justify-content: center;
  align-items: center;

}

.alert-warning {
    color: white;
    background-color: mediumseagreen;
    border-color: #ffeeba;
}

</style>