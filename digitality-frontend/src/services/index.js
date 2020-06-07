import axios from "axios";

let Service = axios.create({
    baseURL: "http://localhost:5000/"
});


let Auth = {
    async register(ime_prezime, eposta, lozinka){
        await Service.post('/register',{
            name: ime_prezime[0],
            surname: ime_prezime[1],
            email: eposta,
            password: lozinka
        })
    },

    async login(eposta, lozinka){
        let response = await Service.post('/login', {email: eposta, password: lozinka})
        
        try{
            let user = response.data;
            localStorage.setItem('user', JSON.stringify(user));
            return true
        }
        catch(e){
            return false
        }        
    },

    logout() {
        localStorage.removeItem('user');
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
    async getArchives(email) {
        let response = await Service.post('/GetArchives',{
            email: email
        });
        return response.data;
    },

    async getDocuments(naziv_podarhive,id_korisnikove_arhive){
        let response = await Service.post('/documents',{
            subArchive_name: naziv_podarhive,
            personal_archive_id: id_korisnikove_arhive
        });
        return response.data;
    },

    async sendDocument(urlDokumenta){
        await Service.post('/send_document',{
            doc_url : urlDokumenta
        })
    },

    async getSearchArchives(pretraga){
        let response = await Service.post('/search/lista_arhiva',{
            searchTerm : pretraga
        })
        return response.data;
    },

    async createSubarchive(naziv,id_korisnikove_arhive){
        await Service.post('/archives/createSubarchive', {
            archive_name : naziv,
            personal_archive_id : id_korisnikove_arhive
        })
    },

    async deleteSubarchive(id_korisnikove_arhive,id_podarhive,naziv_podarhive){
        await Service.post('/archive/deleteSubarchive', {
            personal_archive_id : id_korisnikove_arhive,
            subarchive_id : id_podarhive,
            subarchive_name: naziv_podarhive
        })
    },

    async update_exDate(naziv_arhive){
        await Service.post('/archive/UpdateExaminationDate',{
            archive_name: naziv_arhive
        })
    },

    async sort_Archives(check_value){
        let response = await Service.post('/archives/SortArchives', {
            sorttype: check_value
        })
        return response.data;
    }
};

export { app, Service, Auth };