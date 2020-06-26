export default {
  currentArchiveData: '',
  
  filter: {
    datum_dodavanja: '',
    naziv_dobavljača: '',
    datum_izdavanja: '',
    datum_dospijeća: '',
    vrsta_usluge: '',
    neto_iznos: '',
    iznos: '',
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
  },

  updateCurrentUserArchive(allArchives){
    let userArchive = JSON.parse(localStorage.getItem('currentUserArchive'))
    for(let i = 0; i < allArchives.length; i++){
      if(userArchive._id == allArchives[i]._id) userArchive = allArchives[i]
    }
    this.currentArchiveData = userArchive
    localStorage.setItem("currentUserArchive", JSON.stringify(userArchive))
  },

  //trenutno dok ne napravimo componentu za arhive:
  get_users_arhive(all_archives, user_archive_ids){
    for(let i = 0; i < all_archives.length; i++){
      for(let j = 0; j < user_archive_ids.length; j++){
        if(all_archives[i]._id == user_archive_ids[j]) return all_archives[i]
      }
    }
  }

}