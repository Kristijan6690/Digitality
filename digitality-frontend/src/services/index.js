import axios from "axios";

let Service = axios.create({
    baseURL: "http://localhost:5000/"
});

let app = {
    async registracija(ime_prezime,eposta,lozinka){
        let response = await Service.post('/register',{
            ime: ime_prezime[0],
            prezime: ime_prezime[1],
            email: eposta,
            password: lozinka
        })
        console.log(response)
    },

    async login(eposta,lozinka){
        let response = await Service.post('/login',{
            email: eposta,
            password: lozinka
        })
        return response.data;
    },

    async getArchives() {
        let response = await Service.get('/archives');
        return response.data;
    },

    async getDocuments(naziv_arhive){
        let response = await Service.post('/documents',{
            naziv: naziv_arhive
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

    async createSubarchive(naziv,userID){
        await Service.post('/archives/createSubarchive', {
            archive_name : naziv,
            archive_access_user_ID : userID
        })
    },

    async deleteSubarchive(naziv_arhive){
        await Service.post('/archive/deleteSubarchive', {
            archive_name : naziv_arhive
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

export { app, Service };