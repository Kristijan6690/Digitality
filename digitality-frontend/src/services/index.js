import axios from "axios";
import $router from '@/router'

let Service = axios.create({
    baseURL: "http://localhost:5000/"
});


Service.interceptors.request.use((request) => {
    try {
        request.headers['Authorization'] = 'Bearer ' + Auth.getToken();
    } catch (e) {
        console.error(e);
    }
    return request;
});

Service.interceptors.response.use( (response) => {return response},
    (error) => {
        if (error.response.status == 401) {
            Auth.logout();
            $router.go();
        }
    }
);


let Auth = {
    async register(ime, prezime, eposta, lozinka){
        await Service.post('/register',{
            name: ime,
            surname: prezime,
            email: eposta,
            password: lozinka
        })
    },

    async login(eposta, lozinka){
        let response = await Service.post('/login', {email: eposta, password: lozinka})
        
        if(response.data){
            let user = response.data;
            let archives = await app.getArchives(user.email,user.archive_ids)
            localStorage.setItem('userArchives',JSON.stringify(archives))
            localStorage.setItem('user', JSON.stringify(user));
            return true
        }
        console.log("Failed to login!")
        return false
              
    },

    logout() {
        localStorage.removeItem('user');
        localStorage.removeItem('userArchives')
    },

    getToken() {
        let user = Auth.getUser();
        if (user && user.token) {
            return user.token;
        }
        else
            return null
    },

    getUser() {
        return JSON.parse(localStorage.getItem('user'));
    },

    authenticated() {
        let user = Auth.getUser();
        if (user && user.email) {
            return true;
        }
        return false;
    },

    state: {
        get user() {
            return Auth.getUser();
        },
        get authenticated() {
            return Auth.authenticated();
        },
    }
}

let app = {
    async getArchives(eposta,dostupne_arhive_korisniku) {
        let response = await Service.post('/GetArchives', {
            email: eposta,
            archive_ids: dostupne_arhive_korisniku
        });
        if (response.data){
            return response.data;
        }
        return false
    },

    async sendDocument(urlDokumenta){
        let response = await Service.post('/send_document',{
            doc_url : urlDokumenta
        })
        return response.data
    },

    async getSearchArchives(pretraga,dostupne_arhive_korisniku,id_trenutne_arhive){
        let response = await Service.post('/search/lista_arhiva',{
            searchTerm : pretraga,
            archive_ids: dostupne_arhive_korisniku,
            currentArchive_id: id_trenutne_arhive
        })
        return response.data;
    },

    async createSubarchive(naziv, id_korisnikove_arhive){
        
        await Service.post('/archives/createSubarchive', {
            archive_name : naziv,
            personal_archive_id : id_korisnikove_arhive
        })
    },

    async deleteSubarchive(id_korisnikove_arhive,id_podarhive){
        await Service.post('/archive/deleteSubarchive', {
            personal_archive_id : id_korisnikove_arhive,
            subarchive_id : id_podarhive
        })
    },

    async update_exDate(id_trenutne_arhive,id_podarhive){
        await Service.post('/archive/UpdateExaminationDate',{
            currentArchive_id: id_trenutne_arhive,
            subarchive_id: id_podarhive
        })
    },

    async sort_Archives(check_value,dostupne_arhive_korisniku,id_trenutne_arhive){
        let response = await Service.post('/archives/SortArchives', {
            sorttype: check_value,
            archive_ids: dostupne_arhive_korisniku,
            currentArchive_id: id_trenutne_arhive
        })
        return response.data;
    },

    async share_archive(eposta_korisnika,eposta_share){
        let response = await Service.post('/archives/share', {
            user_email: eposta_korisnika,
            shared_email: eposta_share
        })
        return response.data;
    },

    async delete_shared_archive(eposta_korisnika,eposta_share){
        let response = await Service.post('/archives/shareDelete', {
            user_email: eposta_korisnika,
            shared_email: eposta_share
        })
        return response.data
    },

    async add_alias(eposta_korisnika,ime,prezime,oib,iban,postanski_broj){
        await Service.post('/addAlias', {
            user_email: eposta_korisnika,
            name: ime,
            surname: prezime,
            oib: oib,
            iban: iban,
            postal_code: postanski_broj
        })
    }
};

export { app, Service, Auth };