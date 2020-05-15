export default {
  currentArchive: 'Arhiva_1',

  userData: '',   //Podaci ulogiranog korisnika
  archiveData: '', //Podaci za arhive (voda,struja...)
  documentData: '', //Podaci za svaki dokument sa arhive
  
  filter: {
    datum_dodavanja: '',
    naziv_dobavljača: '',
    datum_izdavanja: '',
    datum_dospijeća: '',
    vrsta_usluge: '',
    kolicina: '',
    iznos: '',
  },
  filter_checks: {
    datum_dodavanja_check: false,
    naziv_dobavljača_check: false,
    datum_izdavanja_check: false,
    datum_dospijeća_check: false,
    vrsta_usluge_check: false,
    kolicina_check: false,
    iznos_check: false,
  },

  //Funkcije------------------------------------------------------
  current_date(){
      let today = new Date();
      let dd = String(today.getDate()).padStart(2, '0');
      let mm = String(today.getMonth() + 1).padStart(2, '0');
      let yyyy = today.getFullYear();
     
      return yyyy + '/' + mm + '/' + dd; 
      //https://stackoverflow.com/questions/1531093/how-do-i-get-the-current-date-in-javascript
    },
  current_time(){
    let today = new Date();
    return today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds(); 
    //https://tecadmin.net/get-current-date-time-javascript/
  }

}